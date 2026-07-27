#!/usr/bin/env python3
"""Validate cheap-run-record JSONL. Stdlib only. No network."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

STATUSES = {"ok", "fail", "timeout", "oom", "nan", "crash", "incomplete"}
STRONG = ("git", "seed", "n", "metrics")
RESOURCE = ("peak_rss_mb", "peak_gpu_mem_mb")


def has_timing(obj: dict[str, Any]) -> bool:
    if "duration_s" in obj and isinstance(obj["duration_s"], (int, float)):
        return True
    stages = obj.get("stages_s")
    return isinstance(stages, dict) and len(stages) > 0


def validate_obj(obj: Any, lineno: int, strict: bool) -> list[str]:
    errs: list[str] = []
    if not isinstance(obj, dict):
        return [f"L{lineno}: not a JSON object"]

    for key in ("ts", "name", "status"):
        if key not in obj:
            errs.append(f"L{lineno}: missing required field '{key}'")

    status = obj.get("status")
    if status is not None and status not in STATUSES:
        errs.append(f"L{lineno}: invalid status {status!r}")

    if not has_timing(obj):
        errs.append(f"L{lineno}: need stages_s or duration_s")

    if status == "incomplete":
        missing = obj.get("missing")
        if not isinstance(missing, list) or not missing:
            errs.append(f"L{lineno}: incomplete status requires non-empty 'missing'")

    if strict and status in {"ok", "fail"}:
        for key in STRONG:
            if key not in obj:
                errs.append(f"L{lineno}: strict: missing strongly recommended '{key}'")
        if not any(k in obj for k in RESOURCE):
            errs.append(
                f"L{lineno}: strict: need peak_rss_mb or peak_gpu_mem_mb"
            )

    # Soft size budget warning as error only in strict? Keep as warning via stderr in main.
    return errs


def line_bytes(raw: str) -> int:
    return len(raw.encode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="JSONL file to validate")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require strongly recommended fields for ok/fail",
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=4096,
        help="Warn if a line exceeds this many UTF-8 bytes (default 4096)",
    )
    args = parser.parse_args()

    if not args.path.is_file():
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    count = 0

    # utf-8-sig tolerates Windows BOM from editors / PowerShell Set-Content
    with args.path.open("r", encoding="utf-8-sig") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            count += 1
            if line_bytes(line) > args.max_bytes:
                warnings.append(
                    f"L{lineno}: line is {line_bytes(line)} bytes (budget {args.max_bytes})"
                )
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"L{lineno}: JSON decode error: {exc}")
                continue
            errors.extend(validate_obj(obj, lineno, args.strict))

    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors:
        print(f"FAIL: {len(errors)} error(s) in {count} record(s)", file=sys.stderr)
        return 1

    print(f"OK: {count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
