# Claude configuration

My public Claude configuration for an agent workflow coordinated through Firstmate.

- `CLAUDE.md` sets the working style, model routing, verification, and delivery rules.
- `skills/` contains diagnosing-bugs, domain-modeling, find-docs, grill-with-docs, grilling, humanizer, resolving-merge-conflicts, and wizard. Each includes its MIT license; source attribution is kept where supplied.
- `hooks/` checks Bash commands against dangerous-command patterns and scans edited files with Gitleaks and Semgrep.
- `settings.json` connects those hooks and lists the current plugins.

Review the files before copying them into `~/.claude/`. The hooks need Bash and jq; edit scanning also needs Gitleaks and Semgrep. Semgrep uses its `auto` rules and needs access to its rule registry. The command guard uses a pattern list and does not sandbox commands.

The full workflow also uses poteto-discipline, blast-radius, create-verification-skill, maintain-verification-skill, no-mistakes, and taste-verify. Those skills are omitted because their installed copies have no redistribution license. Firstmate, Ponytail, gh-axi, and chrome-devtools-axi are separate tools. This repository does not install them.

Personal and business skills, account settings, machine paths, and sync hooks are omitted. Merge these examples into your own configuration; the full local setup depends on tools and permissions outside this repository.
