#!/usr/bin/env python3
"""Calculate deterministic before/after impact metrics."""

from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate reduction percentage, saved amount, and speed multiplier."
    )
    parser.add_argument("before", type=float, help="Value before the change; must be positive")
    parser.add_argument("after", type=float, help="Value after the change; must be non-negative")
    parser.add_argument("--unit", default="minutes", help="Unit label included in JSON output")
    args = parser.parse_args()

    if args.before <= 0:
        parser.error("before must be greater than zero")
    if args.after < 0:
        parser.error("after must be non-negative")
    if args.after > args.before:
        parser.error("after must not exceed before for a reduction calculation")

    saved = args.before - args.after
    reduction = saved / args.before * 100
    speed = None if args.after == 0 else args.before / args.after

    result = {
        "before": args.before,
        "after": args.after,
        "saved": saved,
        "reduction_percent": round(reduction, 1),
        "speed_multiplier": None if speed is None else round(speed, 2),
        "unit": args.unit,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
