# Contributing

## License of contributions

By submitting a pull request or otherwise contributing to this repository, you agree that your contribution is provided under the [MIT License](LICENSE) (same terms as the project). You confirm you have the right to contribute the material (including that your employer allows it if applicable).

We do **not** require a separate CLA. A one-line sign-off in the commit message is welcome but optional:

```text
Signed-off-by: Your Name <you@example.com>
```

## Norms

1. **Honesty first.** Do not reword README/PRIOR_ART to claim invention of experiment tracking or cheap metrics. Keep citations in `REFERENCES.md` current when you knowingly rely on a new upstream.
2. **Keep the skill small.** `SKILL.md` should stay concise; put detail in `schema.md` / `examples.md` / `safety.md`.
3. **Safety.** No scripts that upload run logs. **Never** put real API keys, tokens, `.env` contents, private URLs with credentials, raw PII, or undisclosed proprietary datasets into examples, issues, or PRs. Use synthetic crumbs only (see `examples/sample_runs.jsonl`).
4. **Compatibility.** Validator must remain Python stdlib-only unless there is a strong reason and docs are updated.
5. **No live `.runs/` in PRs.** Run logs belong on the contributor’s machine (and in `.gitignore`). CI rejects commits that add a `.runs/` directory.

## Privacy / compliance (short)

If your experiments may involve personal or regulated data, you—not this skill—are responsible for lawful basis, minimization, retention, and access control. Prefer hashes, counts, and paths over raw content. Do not publish `.runs/` that could re-identify people or leak restricted research data.

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
