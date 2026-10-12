"""Analyze a synthetic 28-day fitness log using pandas and NumPy."""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).with_name("fitness_log.csv")


def analyze(data: pd.DataFrame) -> dict[str, object]:
    required = {"day", "steps", "sleep_hours", "water_glasses", "protocol", "bench_kg"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if data.empty:
        raise ValueError("Fitness log must contain at least one day.")

    steps = data["steps"].to_numpy(dtype=float)
    bench = data["bench_kg"].to_numpy(dtype=float)
    correlation = float(np.corrcoef(steps, bench)[0, 1]) if len(data) > 1 else float("nan")
    weekly = (
        data.assign(week=((data["day"] - 1) // 7) + 1)
        .groupby("week", as_index=False)
        .agg(avg_steps=("steps", "mean"), goal_days=("steps", lambda values: int((values >= 10_000).sum())))
    )
    return {
        "days_tracked": len(data),
        "total_steps": int(steps.sum()),
        "average_steps": round(float(steps.mean())),
        "goal_days": int(np.sum(steps >= 10_000)),
        "average_sleep": round(float(data["sleep_hours"].mean()), 1),
        "protocol_average_steps": data.groupby("protocol")["steps"].mean().round().astype(int).to_dict(),
        "steps_bench_correlation": round(correlation, 3) if np.isfinite(correlation) else None,
        "weekly": weekly,
    }


def main() -> None:
    data = pd.read_csv(DATA_FILE)
    report = analyze(data)
    print("28-DAY FITNESS LOG | SYNTHETIC SAMPLE")
    print(f"Days tracked: {report['days_tracked']}")
    print(f"Total steps: {report['total_steps']:,}")
    print(f"Average steps/day: {report['average_steps']:,}")
    print(f"Days with 10,000+ steps: {report['goal_days']}")
    print(f"Average sleep: {report['average_sleep']} hours")
    print(f"Step/bench correlation: {report['steps_bench_correlation']}")
    print("\nWeekly summary:")
    print(report["weekly"].to_string(index=False))
    print("\nAverage steps by protocol (descriptive only):")
    for protocol, average in report["protocol_average_steps"].items():
        print(f"  {protocol}: {average:,}")


if __name__ == "__main__":
    main()
