# Contributing

## Norms

1. **Honesty first.** Do not reword README/PRIOR_ART to claim invention of experiment tracking or cheap metrics. Keep citations in `REFERENCES.md` current when you knowingly rely on a new upstream.
2. **Keep the skill small.** `SKILL.md` should stay concise; put detail in `schema.md` / `examples.md` / `safety.md`.
3. **Safety.** No scripts that upload run logs. No examples containing real secrets.
4. **Compatibility.** Validator must remain Python stdlib-only unless there is a strong reason and docs are updated.

## Suggested workflow

1. Edit schema + skill together when adding fields.
2. Add a line to `examples/sample_runs.jsonl`.
3. Run `python scripts/validate_run_record.py examples/sample_runs.jsonl --strict`.
4. Note prior-art impact in `PRIOR_ART.md` if the change narrows/widens overlap with another project.

## Forms welcome

- Skill text improvements
- Schema fields for math/AI domains
- Adapters that *export* crumbs to MLflow/W&B (optional, separate folder)
- Translations of `SKILL.md` (keep English canonical for agent triggers unless dual-maintained)
