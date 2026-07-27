# cheap-run-record

**Opportunistic run metadata** for math & AI: tiny fields you should record while a run is already happening (stage timings, peak memory, optional GPU/CPU temp & power, scale, seed/commit, claimed complexity). Packaged primarily as an **Agent Skill** so coding agents append a one-line JSON record after experiments / evals / proof searches.

> This is a **convention pack**, not a claim that “logging duration” is a new invention. See [PRIOR_ART.md](PRIOR_ART.md), [REFERENCES.md](REFERENCES.md), and [NOTICE](NOTICE).

## Why a skill (and other forms)

| Form | Role |
|------|------|
| **Agent Skill** (`skills/cheap-run-record/`) | Best default: agents auto-apply when running experiments / scoring |
| **JSON Schema** (`schemas/run-record.schema.json`) | Machine-checkable contract; works without any agent |
| **Validator** (`scripts/validate_run_record.py`) | CI / local gate for required fields |
| Optional later | Cursor rule one-liner; MLflow/W&B adapter — out of scope for v0.1 |

A full experiment *platform* (MLflow, W&B) or *research loop* (ResearcherSkill) is complementary, not replaced.

## Install (Cursor / skills-compatible agents)

Copy or submodule the skill directory:

```text
skills/cheap-run-record/SKILL.md
```

into your project’s `.cursor/skills/cheap-run-record/` (or your agent’s skills path).

## Quick contract

After any experiment, benchmark, ablation, eval, or proof/search run, append **one JSON object** to `.runs/runs.jsonl`.

**Required:** `ts`, `name`, `status`, `stages_s` (or `duration_s`), plus identity crumbs when available (`git`, `seed`).

**Missing required crumbs ⇒ mark `status: incomplete`** (or fix before claiming the run finished).

Details: [skills/cheap-run-record/SKILL.md](skills/cheap-run-record/SKILL.md)

### Keep run logs out of git

Real project logs must not be committed:

```gitignore
.runs/
.env
```

This repository already ignores `.runs/`. Copy that line into your own project’s `.gitignore`. Publish only synthetic examples (see `examples/`).

## Validate

```bash
python scripts/validate_run_record.py examples/sample_runs.jsonl
python scripts/validate_run_record.py path/to/runs.jsonl --strict
```

Stdlib only; no network.

## Safety

Do not log secrets, full prompts/outputs, or PII. See [SECURITY.md](SECURITY.md) and the skill’s safety section. If logs might contain personal or regulated data, you are responsible for lawful use (minimization, consent/contract basis, retention, access control)—prefer hashes over raw content.

## License

MIT. Attribution for related work: [NOTICE](NOTICE) + [REFERENCES.md](REFERENCES.md).

## 免责声明 / Disclaimer

软件按现状提供（AS IS），不提供任何担保，作者不对因使用本软件造成的损失负责。

The software is provided “AS IS”, without warranty of any kind. The authors are not liable for any damages arising from use of this software. See [LICENSE](LICENSE) for the full MIT text.
