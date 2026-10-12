# 28-Day Fitness Analytics

A small analytics report for a synthetic 28-day activity log. It uses pandas
and NumPy to summarize daily steps, sleep, weekly progress, protocol groups,
and the relationship between steps and bench-press measurements.

## What It Does

- Reads daily activity records from `fitness_log.csv`
- Calculates total and average steps and counts days at the 10,000-step target
- Summarizes average sleep and weekly step progress
- Compares average steps across the sample protocols
- Calculates a descriptive correlation between steps and bench press

## Setup

Requires Python 3.10 or newer.

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the report from the project directory:

```bash
python analyze_fitness.py
```

Run tests with `python -m unittest -v`.

## Sample Output

```text
28-DAY FITNESS LOG | SYNTHETIC SAMPLE
Days tracked: 28
Total steps: 268,700
Average steps/day: 9,596
Days with 10,000+ steps: 12
Average sleep: 7.6 hours
Step/bench correlation: 0.876
```

## Stack

Python, pandas, NumPy

The data is invented for practice. Group averages and correlations do not
show that one habit causes another and are not health advice.
