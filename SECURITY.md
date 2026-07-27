# Security Policy

## What this project is

Instructional skill + local JSONL schema + a stdlib-only validator. It does **not** phone home, open network ports, or require API keys.

## Data you must not put in run records

Treat `.runs/runs.jsonl` (or equivalent) as **semi-sensitive**:

- Do **not** store secrets: API keys, tokens, passwords, cookies, private URLs with credentials.
- Do **not** store raw PII, medical/financial identifiers, or unpublished confidential datasets.
- Do **not** dump full prompts, full model outputs, or training corpora into the record — use hashes, lengths, and paths instead.
- Do **not** commit run logs that contain proprietary weights paths + internal hostnames if your org forbids it; add `.runs/` to `.gitignore` when needed.

## Agent / skill safety

- The skill must **not** instruct agents to exfiltrate environment variables or `.env` files into run records.
- Prefer hashes (`config_hash`, `data_hash`, `prompt_template_hash`) over verbatim configs when configs may embed secrets.
- Validation scripts must stay **local filesystem only** (no upload helpers in this repo).

## Reporting issues

Open a GitHub issue describing the safety concern. Do not paste live secrets into the issue.
