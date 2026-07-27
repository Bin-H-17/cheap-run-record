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

## Redact long text (example)

```python
import hashlib

def crumb_hash(text: str, n: int = 16) -> str:
    digest = hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()
    return f"sha256:{digest[:n]}"

# store prompt_template_hash=crumb_hash(template), not the template itself
```

Reject obvious secret-shaped strings before append (heuristic only):

```python
import re
SECRETISH = re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*\S+")
if SECRETISH.search(line):
    raise ValueError("refusing to write suspected secret into run log")
```

## Local only

Keep `.runs/` in `.gitignore`. Do not upload `.runs/` unless the user explicitly asks. This skill has no telemetry.
