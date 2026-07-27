# References & Related Work

This project **repackages well-known practices** into a small agent skill and JSON schema. It does not assert originality for the underlying ideas. Prefer citing the primary sources below when you write papers or docs that use this skill.

## Observability / cheap instrumentation

1. Prometheus Authors. *Instrumentation*. Prometheus Docs.  
   https://prometheus.io/docs/practices/instrumentation/  
   — “Instrument everything”; prefer cheap metrics; beware cardinality.

2. Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (Eds.). *Site Reliability Engineering* (Google). O’Reilly.  
   — Four golden signals: latency, traffic, errors, saturation.

## Experiment tracking / MLOps

3. MLflow Project. *MLflow Tracking*.  
   https://mlflow.org/docs/latest/tracking.html

4. Weights & Biases. *Experiment Tracking*.  
   https://docs.wandb.ai/

5. SwanLab / similar lightweight trackers (community tools for local/cloud metric logging).

## Agent skills with related logging

6. Dudek, K. et al. *ResearcherSkill* — autonomous experiment loop with `.lab/results.tsv` (`duration_s`, metrics, commit).  
   https://github.com/krzysztofdudek/researcherskill

7. kinhluan. *experiment-tracking* agent skill — YAML experiment logs, paper tables, cloud GPU notes.  
   https://github.com/kinhluan/skills/blob/main/.agent-skills/experiment-tracking/SKILL.md

8. Paul Berg / community *autoresearch*-style skills — metric-driven keep/discard loops with elapsed time.  
   e.g. https://github.com/paulrberg/agent-skills

## Reproducibility (math / ML)

9. Pineau, J. et al. *Improving Reproducibility in Machine Learning Research* (NeurIPS reproducibility program and related checklists).

10. Algorithm analysis texts on asymptotic time/space complexity (big-O) as *claimed* complexity distinct from *measured* wall-clock and RSS — treat both as useful, not interchangeable.

## How to cite this repository

If you use this skill in a paper or public artifact, a software citation is enough, for example:

```bibtex
@software{cheap_run_record,
  title        = {cheap-run-record: Opportunistic run metadata skill for math and AI},
  author       = {{cheap-run-record contributors}},
  year         = {2026},
  url          = {https://github.com/Bin-H-17/cheap-run-record},
  note         = {Convention pack synthesizing common experiment-logging practices; see REFERENCES.md}
}
```

Replace the URL after you publish the GitHub repository.
