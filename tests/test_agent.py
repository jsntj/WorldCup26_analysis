import unittest
from io import StringIO
from unittest.mock import patch

from worldcup26_analysis.agent import WorldCupPredictionAgent, get_default_2026_candidates, main


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

    def test_train_fits_model(self):
        agent = WorldCupPredictionAgent()
        agent.train()
        self.assertTrue(hasattr(agent.model, "n_features_in_"))
        self.assertEqual(agent.model.n_features_in_, 3)

    def test_main_runs_end_to_end(self):
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
        self.assertIn("World Cup 2026 prediction ranking:", output)
        self.assertIn("Predicted winner:", output)


if __name__ == "__main__":
    unittest.main()
