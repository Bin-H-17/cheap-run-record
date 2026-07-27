# Safety redlines

Follow these when writing run records. Full policy: [../../SECURITY.md](../../SECURITY.md).

## Never put in JSONL

- API keys, tokens, passwords, `Authorization` headers
- `.env` contents or cloud credentials
- Raw user PII / confidential corpora
- Full prompts, chain-of-thought dumps, or complete model outputs
- Entire checkpoints (record `artifact_mb` + path/hash only if path is non-sensitive)

## Prefer

- `*_hash` fields and short paths
- Aggregates: counts, lengths, scores
- `missing` + `incomplete` instead of guessing

## Local only

Do not upload `.runs/` unless the user explicitly asks. This skill has no telemetry.
