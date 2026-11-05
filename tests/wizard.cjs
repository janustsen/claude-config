// Run with Node 22+; only the template's library is executed, never its setup stages.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { parseEnv } = require('node:util');
const library = fs.readFileSync(path.join(__dirname, '../skills/wizard/template.sh'), 'utf8').split('# STAGES:')[0];
const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'wizard-test-'));
const envFile = path.join(scratch, '.env');
function run(script, values = {}, input = '') {
  return spawnSync('bash', ['-c', library + '\n' + script], {
    cwd: scratch, env: { ...process.env, ENV_FILE: envFile, ...values }, input, encoding: 'utf8',
  });
}
const cases = {
  'hash characters survive dotenv parsing'() {
    assert.equal(run('write_env VALUE "$TEST_VALUE"', { TEST_VALUE: 'abc#def' }).status, 0);
    assert.equal(parseEnv(fs.readFileSync(envFile, 'utf8')).VALUE, 'abc#def');
  },
  'saved quotes are decoded before reuse'() {
    fs.writeFileSync(envFile, 'VALUE="test_example"\n');
    assert.equal(run('_existing VALUE').stdout, 'test_example');
    const result = run('ask_secret VALUE "Value:"; printf "RESULT:%s" "$VALUE"', {}, '\n');
    assert.equal(result.status, 0);
    assert.ok(result.stdout.endsWith('RESULT:test_example'));
  },
  'punctuation and whitespace round trip without evaluating values'() {
    for (const value of ['', '  spaced  ', 'abc#def', "it's#literal", 'say "hello"#', '`literal`', '$HOME $(exit 99)', String.raw`literal\n\r\path`, 'both\'"quotes#']) {
      fs.writeFileSync(envFile, 'OTHER=keep\n');
      const result = run('write_env VALUE "$TEST_VALUE" >/dev/null; _existing VALUE', { TEST_VALUE: value });
      assert.equal(result.status, 0, result.stderr);
      assert.equal(result.stdout, value);
      assert.deepEqual({ ...parseEnv(fs.readFileSync(envFile, 'utf8')) }, { OTHER: 'keep', VALUE: value });
    }
  },
  'unsupported values leave existing data unchanged'() {
    for (const value of ['all\'"`quotes', 'two\nlines', 'carriage\rreturn']) {
      const before = 'VALUE=original\nOTHER=keep\n';
      fs.writeFileSync(envFile, before);
      assert.notEqual(run('write_env VALUE "$TEST_VALUE"', { TEST_VALUE: value }).status, 0);
      assert.equal(fs.readFileSync(envFile, 'utf8'), before);
    }
  },
};
let failures = 0;
try {
  for (const [name, test] of Object.entries(cases)) {
    try { test(); console.log('PASS:', name); }
    catch (error) { failures++; console.error('FAIL:', name, error.message); }
  }
} finally { fs.rmSync(scratch, { recursive: true, force: true }); }
process.exitCode = failures ? 1 : 0;
