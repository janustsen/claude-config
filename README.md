# Claude configuration

My public Claude configuration for an agent workflow coordinated through Firstmate.

- `CLAUDE.md` sets the working style, model routing, verification, and delivery rules.
- `skills/` contains diagnosing-bugs, domain-modeling, find-docs, grill-with-docs, grilling, humanizer, resolving-merge-conflicts, and wizard. Each includes its MIT license; source attribution is kept where supplied. The wizard template has fixes for quoted values, and merge-conflict guidance limits staging to the work being resolved.
- `skills/` also contains three design skills: product-ui (app interfaces), ai-interaction-patterns (AI surfaces such as composers, streaming, approvals and citations) and website-design (distinctive websites). They come from teardowns of T3 Code, twenty AI-forward products and 41 websites, and they route to the emil-*, apple-design and animation skills for component craft. [docs/design-guide.md](docs/design-guide.md) is the readable front of all three.
- `skills/mobile-ui` is the iPhone companion of product-ui: measured iOS defaults, thumb-first placement, sheets, lists and quick capture, from case studies of about 40 iPhone apps and real-device walks.
- `skills/ux-flows` covers whole jobs rather than screens: step budgets, the next action at every stop, confirmation, undo, errors and returning, for 14 standard jobs walked across 25 apps on desktop and iPhone. Its walk-the-job check is required by the product-ui review checklist for every UI change.
- `hooks/` checks Bash commands against dangerous-command patterns and scans edited files with Gitleaks and Semgrep.
- `settings.json` connects those hooks and lists the current plugins.

Review the files before copying them into `~/.claude/`. The hooks need Bash and jq; edit scanning also needs Gitleaks and Semgrep. Semgrep uses its `auto` rules and needs access to its rule registry. The command guard uses a pattern list and does not sandbox commands.

The full workflow also uses poteto-discipline, blast-radius, create-verification-skill, maintain-verification-skill, no-mistakes, and taste-verify. Those skills are omitted because their installed copies have no redistribution license. Firstmate, Ponytail, gh-axi, and chrome-devtools-axi are separate tools. This repository does not install them.

Personal and business skills, account settings, machine paths, and sync hooks are omitted. Merge these examples into your own configuration; the full local setup depends on tools and permissions outside this repository.

The wizard helpers support single-line `.env` values. They refuse multiline values or values that cannot be quoted losslessly before changing the file. Run the regression checks with `node tests/wizard.cjs` (Node 22+). The tests execute the library without opening browsers or changing GitHub settings.
