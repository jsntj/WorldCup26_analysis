import unittest

from worldcup26_analysis.agent import WorldCupPredictionAgent, get_default_2026_candidates


class TestWorldCupPredictionAgent(unittest.TestCase):
    def test_load_historical_data_has_expected_columns(self):
        agent = WorldCupPredictionAgent()
        historical = agent.load_historical_data()
        self.assertFalse(historical.empty)
        self.assertTrue(
            {"team", "fifa_rank", "recent_win_rate", "avg_goals", "won_world_cup"}.issubset(
                historical.columns
            )
        )

    def test_predict_2026_returns_probabilities_sorted_desc(self):
        agent = WorldCupPredictionAgent()
        agent.train()
        candidates = get_default_2026_candidates()
        result = agent.predict_2026(candidates)
        self.assertEqual(len(result), len(candidates))
        self.assertIn("win_probability", result.columns)
        self.assertGreaterEqual(result["win_probability"].iloc[0], result["win_probability"].iloc[-1])
        self.assertTrue(((result["win_probability"] >= 0) & (result["win_probability"] <= 1)).all())


if __name__ == "__main__":
    unittest.main()
