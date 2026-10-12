import unittest

import pandas as pd

from analyze_fitness import analyze


class FitnessAnalysisTests(unittest.TestCase):
    def test_computes_totals_and_goal_days(self):
        data = pd.DataFrame({
            "day": [1, 2],
            "steps": [9_000, 11_000],
            "sleep_hours": [7.0, 8.0],
            "water_glasses": [7, 8],
            "protocol": ["A", "B"],
            "bench_kg": [80, 82],
        })
        result = analyze(data)
        self.assertEqual(result["total_steps"], 20_000)
        self.assertEqual(result["goal_days"], 1)
        self.assertEqual(len(result["weekly"]), 1)

    def test_empty_data_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze(pd.DataFrame(columns=[
                "day", "steps", "sleep_hours", "water_glasses", "protocol", "bench_kg"
            ]))


if __name__ == "__main__":
    unittest.main()
