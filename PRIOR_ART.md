# Prior Art & Overlap Check

**Check date:** 2026-07-27 (Asia/Shanghai)  
**Scope:** GitHub agent skills, experiment-tracking skills, ML run-logging conventions, related READMEs/posts.  
**Method:** Web search over GitHub `SKILL.md` / experiment-tracking repos; manual comparison of purpose, schema, and agent contract. `gh` CLI search was unavailable (not authenticated); conclusions rely on public web + raw file fetches.

## Verdict

**Feasible to publish.** Closest projects cover *full* experiment tracking or *autonomous research loops*. None match this repo’s narrow niche:

> **Opportunistic, tiny run metadata** (stage timings, peak memory, scale, seed/commit, claimed complexity) as a **default agent habit** for **math + AI** runs — with an explicit **incomplete-if-missing** contract and **safety redlines**.

This is a **convention pack + agent skill**, not a claim of inventing experiment logging.

## Closest projects (related, not duplicates)

| Project | What it is | Overlap | Difference from this skill |
|---------|------------|---------|------------------------------|
| [krzysztofdudek/ResearcherSkill](https://github.com/krzysztofdudek/researcherskill) (and forks) | Autonomous keep/discard experiment loop; `.lab/results.tsv` includes `duration_s`, metric, commit | Records duration & status | Full research *loop* + guardrails; not a minimal sidecar schema for math/AI stage costs |
| [kinhluan/skills `experiment-tracking`](https://github.com/kinhluan/skills/blob/main/.agent-skills/experiment-tracking/SKILL.md) | PhD-style experiment YAML, paper tables, W&B, cloud GPU | Seed, wall time, results | Broad research workflow; heavier per-run docs; not “cheap crumbs only” |
| [Cosmic-Game-studios/deepresearch](https://github.com/Cosmic-Game-studios/deepresearch) | Multi-level research orchestration + `experiments.jsonl` | JSONL run log, optional `duration_seconds` | Large system; different goal |
| [paulrberg/agent-skills `autoresearch`](https://github.com/paulrberg/agent-skills) / Karpathy-style autoresearch | Metric-driven search loops | Elapsed seconds, keep/discard | Optimization loop, not opportunistic metadata |
| MLflow / W&B / SwanLab | Productized experiment tracking | Params, metrics, env | Platforms; this skill is the *minimum agent checklist* that can feed them |
| Prometheus [instrumentation practices](https://prometheus.io/docs/practices/instrumentation/) | “Instrument everything”; cheap counters | Cheap metrics philosophy | Production services, not math/AI run crumbs |

## Name / schema collision

- No public skill found named `cheap-run-record` with this schema (`stages_s`, `peak_rss_mb`, `complexity`, math/LLM fields, incomplete gate).
- Field names are intentionally plain (`git`, `seed`, `metrics`) — common vocabulary, not copied from a single upstream file.

## Positioning (honest)

| We synthesize | We do **not** claim |
|---------------|---------------------|
| Cheap metrics / log-what-is-already-in-hand habit | Novelty of “record experiment duration” |
| Reproducibility basics (seed, commit, data hash) | Replacement for MLflow/W&B |
| Agent trigger + incomplete contract | First experiment-tracking skill ever |

See [REFERENCES.md](REFERENCES.md) for citations and [NOTICE](NOTICE) for attribution language.
