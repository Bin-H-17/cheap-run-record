---
name: cheap-run-record
description: >-
  Append opportunistic, tiny run metadata (stage timings, peak memory, scale,
  seed/commit, claimed complexity, metric summary) after math or AI experiments,
  benchmarks, ablations, evals, and proof/search runs. Use when running
  experiments, scoring models, timing pipeline stages, logging reproducibility
  crumbs, or when the user mentions 不记白不记, cheap metrics, run log, or
  runs.jsonl. Does not replace MLflow/W&B or full research-loop skills.
---

# cheap-run-record

Record **crumbs that are already in hand** while a run executes. One JSON line per run. Prefer this over rebuilding timelines from memory later.

This skill is a **convention + agent contract**, synthesizing common experiment-logging and cheap-instrumentation practices. It does **not** claim novelty for those ideas. See [ATTRIBUTION.md](ATTRIBUTION.md); full prior-art notes live in the repository `PRIOR_ART.md` / `REFERENCES.md` when present.

## When to apply

Apply automatically when any of these happen:

- Train / eval / ablation / benchmark / hyperparameter sweep
- Math numerics, solver, discrete search, or proof/check pipeline
- LLM / VLM scoring, prompting bake-off, or agent eval harness
- User asks to “顺手记一下时间/内存/复杂度” or similar

Skip when the user only wants a design discussion with **no** execution.

## Hard contract

1. **Before** long runs: note `name`, intended `seed`, and config identity (`config_hash` or path).
2. **During** runs: time coarse stages (load / preprocess / train|search / eval|check / io).
3. **After** every run (success or failure): append **one** JSON object to `.runs/runs.jsonl` (create `.runs/` if needed).
4. If required fields are missing and cannot be recovered → set `"status": "incomplete"` and list gaps in `missing`.
5. Never block on perfect data: record what you have; mark incomplete rather than inventing numbers.

## Default path

```text
.runs/runs.jsonl          # append-only
.runs/README.md           # optional: one-line pointer to this skill
```

Add `.runs/` to `.gitignore` when logs may contain internal paths your org should not publish. Prefer committing **schema examples** only.

## Minimal record (required + strongly recommended)

```json
{
  "schema_version": 1,
  "ts": "2026-07-27T00:50:00+08:00",
  "name": "exp_baseline_lr",
  "status": "ok",
  "git": "a1b2c3d",
  "seed": 42,
  "config_hash": "sha256:…",
  "n": {"samples": 10000, "params": 11000000},
  "stages_s": {"load": 1.2, "train": 45.0, "eval": 3.1},
  "duration_s": 49.5,
  "peak_rss_mb": 812,
  "peak_gpu_mem_mb": 2048,
  "hw": {
    "peak_gpu_temp_c": 76,
    "peak_cpu_temp_c": 62,
    "peak_gpu_util": 97,
    "avg_gpu_util": 91,
    "peak_cpu_util": 72,
    "avg_cpu_util": 45,
    "peak_power_w": 250,
    "thermal_throttled": false
  },
  "artifact_mb": 24.5,
  "complexity": {"time": "O(n log n)", "space": "O(n)"},
  "metrics": {"acc": 0.91, "f1": 0.88},
  "note": "lr 3e-4 vs baseline 1e-3"
}
```

### Required fields

| Field | Rule |
|-------|------|
| `ts` | ISO-8601 timestamp |
| `name` | Short run id / slug |
| `status` | `ok` \| `fail` \| `timeout` \| `oom` \| `nan` \| `crash` \| `incomplete` |
| Timing | `stages_s` (object) **or** `duration_s` (number) — prefer both |

### Strongly recommended (mark `incomplete` if omitted without reason)

| Field | Purpose |
|-------|---------|
| `git` | Commit short SHA when in a git repo |
| `seed` | RNG seed if stochastic |
| `n` | Scale: samples, tokens, nodes, dim, params, … |
| `peak_rss_mb` and/or `peak_gpu_mem_mb` | Measured resource crumb |
| `metrics` | Primary score(s) if the run was meant to score |
| `complexity` | Claimed big-O (string); optional, cheap to jot |

### Domain optional fields

**ML / LLM:** `model`, `data_hash`, `dtype`, `tokens_in`, `tokens_out`, `est_cost_usd`, `prompt_template_hash`, `decode` (sampling params; `decode.temperature` ≠ hardware temp)

**Math / numerics / proof:** `residual`, `iters`, `proved` (bool), `timeout_s`, `assumption` (short string)

**Hardware (optional, best-effort):** `hw` object — see below. Omit entirely if sensors unavailable; do **not** mark `incomplete` solely for missing `hw`.

**Compare:** `baseline`, `delta_metrics`, `delta_duration_s`

### `hw` crumbs (temperature & friends)

Record **peaks / flags over the run**, not a time series (series blow the size budget).

| Field | Meaning |
|-------|---------|
| `peak_gpu_temp_c` | Max GPU temperature (°C) |
| `peak_cpu_temp_c` | Max CPU package/core temp if cheap to read |
| `peak_gpu_util` | Peak GPU utilization % (0–100) |
| `avg_gpu_util` | Mean GPU utilization % over the run (optional) |
| `peak_cpu_util` | Peak CPU utilization % (0–100; all-cores or process — note which in `note` if unusual) |
| `avg_cpu_util` | Mean CPU utilization % over the run (optional) |
| `peak_power_w` | Peak board/package power (W) if available |
| `thermal_throttled` | `true` if OS/driver reported thermal throttle |

Sources (best-effort): `nvidia-smi` / NVML, `rocm-smi`, Windows Performance Counters, `psutil.cpu_percent` / `psutil.sensors_*`. Sample every few seconds; store peaks (and optional means). No sensor → omit `hw`.

Full field list: [schema.md](schema.md). Examples: [examples.md](examples.md). Safety: [safety.md](safety.md).

## Agent checklist (copy and tick)

```text
Run record:
- [ ] stages_s or duration_s written
- [ ] status set (not silently omitted)
- [ ] git / seed / n when applicable
- [ ] peak memory crumb when measurable
- [ ] hw temp/util/power if sensors are one command away (else skip)
- [ ] metrics or explicit N/A in note
- [ ] no secrets / full prompts / raw datasets in the line
- [ ] appended to .runs/runs.jsonl
- [ ] validated if scripts/validate_run_record.py is available
```

## How to measure (keep it cheap)

- **Wall time:** `time.perf_counter()` (Python) around stages; sum ≈ `duration_s`.
- **RSS:** best-effort (`resource.getrusage`, `psutil`, OS tools). If unavailable, omit and say so in `note` — do not fabricate.
- **GPU mem:** framework APIs (`torch.cuda.max_memory_allocated`) when already using that stack.
- **Temp / util / power:** e.g. `nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,power.draw --format=csv,noheader,nounits` plus `psutil.cpu_percent(interval=None)` (or OS counters) on a timer; store peaks and optional averages. No sensor → omit `hw`.
- **Hashes:** hash config files / split manifests; do not paste secrets into hash inputs if avoidable.
- **Complexity:** human/agent-stated asymptotic class; never pretend it equals wall-clock.

## Validation

From repo root (or any checkout that includes the script):

```bash
python scripts/validate_run_record.py .runs/runs.jsonl
python scripts/validate_run_record.py .runs/runs.jsonl --strict
```

`--strict` requires strongly recommended fields for `status` in `ok`/`fail`.

## Interop

- **Alongside MLflow/W&B:** still write the JSONL crumb; optionally mirror metrics to the tracker.
- **Alongside ResearcherSkill / autoresearch:** those own the keep/discard loop; this skill only ensures stage-cost crumbs exist.
- **Paper tables:** aggregate from JSONL later; do not expand this skill into paper-writing.

## Anti-goals

- Do not store full traces, activations, or datasets in the JSONL line.
- Do not invent high-cardinality “metrics” for every internal counter.
- Do not present this skill as the first or only experiment-tracking method.
