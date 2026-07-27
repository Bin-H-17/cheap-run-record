# Security Policy

## What this project is

Instructional skill + local JSONL schema + a stdlib-only validator. It does **not** phone home, open network ports, or require API keys.

## Data you must not put in run records

Treat `.runs/runs.jsonl` (or equivalent) as **semi-sensitive**:

- Do **not** store secrets: API keys, tokens, passwords, cookies, private URLs with credentials.
- Do **not** store raw PII, medical/financial identifiers, or unpublished confidential datasets.
- Do **not** dump full prompts, full model outputs, or training corpora into the record — use hashes, lengths, and paths instead.
- **Always** keep `.runs/` in `.gitignore` for real projects (this repo’s root `.gitignore` already lists `.runs/`). Prefer private storage if logs must be retained.

## Agent / skill safety

- The skill must **not** instruct agents to exfiltrate environment variables or `.env` files into run records.
- Prefer hashes (`config_hash`, `data_hash`, `prompt_template_hash`) over verbatim configs when configs may embed secrets.
- Validation scripts must stay **local filesystem only** (no upload helpers in this repo).
- Conventions are not sandboxes: constrain your agent’s filesystem/network policy separately if you handle secrets.

## Reporting a vulnerability or leak

1. **Do not** paste live secrets, tokens, or personal data into a public issue.
2. Prefer GitHub **Private vulnerability reporting** / Security advisory for this repository (Security tab), or open an issue with only a **redacted summary** (what class of problem, which file path pattern—not the secret itself).
3. If a secret was committed: **rotate/revoke it immediately**, then remove it from git history (e.g. [`git filter-repo`](https://github.com/newren/git-filter-repo) or [BFG](https://rtyley.github.io/bfg-repo-cleaner/)) and force-push only if you understand the impact on collaborators.

## CI guard

This repository’s workflow rejects trees that contain a tracked `.runs/` directory. Enable GitHub **Secret scanning** and **Push protection** on the repo for additional safety.
