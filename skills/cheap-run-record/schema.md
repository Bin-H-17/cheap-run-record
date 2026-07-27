# Run record schema (human)

Machine schema: [`../../schemas/run-record.schema.json`](../../schemas/run-record.schema.json)

`schema_version` is currently `1`.

## Status enum

`ok` | `fail` | `timeout` | `oom` | `nan` | `crash` | `incomplete`

Use `incomplete` when the agent could not obtain required/strongly recommended crumbs.

## Core

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `schema_version` | int | recommended | Default `1` |
| `ts` | string | yes | ISO-8601 |
| `name` | string | yes | Slug / run id |
| `status` | string | yes | Enum above |
| `stages_s` | object of number | one of timing | Seconds per stage |
| `duration_s` | number | one of timing | Total wall seconds |
| `missing` | string[] | if incomplete | What was not recorded |
| `note` | string | no | One short line |
| `git` | string | strong | Short SHA |
| `seed` | number \| string | strong | |
| `config_hash` | string | no | |
| `config_path` | string | no | Prefer path + hash over inline secrets |
| `n` | object \| number | strong | Scale dictionary preferred |
| `peak_rss_mb` | number | strong | |
| `peak_gpu_mem_mb` | number | strong if GPU | |
| `hw` | object | optional | Thermal / util / power peaks; see below |
| `artifact_mb` | number | no | Outputs size |
| `complexity` | object | no | `{ "time": "O(…)", "space": "O(…)" }` |
| `metrics` | object | strong if scoring | Flat numbers/strings |
| `baseline` | string | no | Prior run name |
| `delta_metrics` | object | no | |
| `delta_duration_s` | number | no | |

## ML / LLM extras

`model`, `data_hash`, `dtype`, `tokens_in`, `tokens_out`, `est_cost_usd`, `prompt_template_hash`, `decode` (object; sampling temperature ≠ `hw` temps)

## Math / proof extras

`residual`, `iters`, `proved`, `timeout_s`, `assumption`

## Hardware extras (`hw`)

Optional. Missing `hw` never forces `incomplete`.

| Field | Type | Notes |
|-------|------|-------|
| `peak_gpu_temp_c` | number | °C |
| `peak_cpu_temp_c` | number | °C |
| `peak_gpu_util` | number | 0–100 |
| `avg_gpu_util` | number | 0–100, optional |
| `peak_cpu_util` | number | 0–100 |
| `avg_cpu_util` | number | 0–100, optional |
| `peak_power_w` | number | Watts |
| `thermal_throttled` | boolean | Any thermal throttle during run |

Do **not** embed temperature time series in the JSONL line.

## Size budget

One line should stay small (aim **&lt; 4 KiB**). If larger, you are logging too much — hash and truncate.
