# Forms: skill vs alternatives

| Form | Use when | Notes |
|------|----------|-------|
| **Agent Skill** (this repo’s primary) | You want agents to *default* to logging after runs | Best trigger coverage |
| **JSON Schema + JSONL only** | Humans/CI only; no agent | Ship `schemas/` + `scripts/` |
| **Cursor User Rule** | Always-on one paragraph | Easy to ignore details; poorer progressive disclosure |
| **Template repo / cookiecutter** | New math/AI projects | Heavier; good later |
| **Tracker plugin (MLflow/W&B)** | Team already standardized on a platform | Complementary; not v0.1 |

Recommendation: publish as **skill + schema + validator**. Optional rule can say “follow cheap-run-record skill when running experiments.”
