from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "historical_world_cup_performance.csv"


class WorldCupPredictionAgent:
    def __init__(self, data_path: Path = DATA_PATH):
        self.data_path = data_path
        self.model = RandomForestClassifier(n_estimators=200, random_state=42)

    def load_historical_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)

    def train(self) -> None:
        historical = self.load_historical_data()
        X = historical[["fifa_rank", "recent_win_rate", "avg_goals"]]
        y = historical["won_world_cup"]
        self.model.fit(X, y)

    def predict_2026(self, teams_2026: pd.DataFrame) -> pd.DataFrame:
        probabilities = self.model.predict_proba(
            teams_2026[["fifa_rank", "recent_win_rate", "avg_goals"]]
        )[:, 1]
        result = teams_2026.copy()
        result["win_probability"] = probabilities
        return result.sort_values("win_probability", ascending=False).reset_index(drop=True)


def get_default_2026_candidates() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"team": "Argentina", "fifa_rank": 1, "recent_win_rate": 0.81, "avg_goals": 1.9},
            {"team": "France", "fifa_rank": 2, "recent_win_rate": 0.79, "avg_goals": 2.0},
            {"team": "Brazil", "fifa_rank": 5, "recent_win_rate": 0.75, "avg_goals": 1.8},
            {"team": "England", "fifa_rank": 4, "recent_win_rate": 0.74, "avg_goals": 1.7},
            {"team": "Spain", "fifa_rank": 3, "recent_win_rate": 0.76, "avg_goals": 1.8},
        ]
    )


def main() -> None:
    agent = WorldCupPredictionAgent()
    agent.train()
    predictions = agent.predict_2026(get_default_2026_candidates())
    top_team = predictions.iloc[0]
    print("World Cup 2026 prediction ranking:")
    print(predictions[["team", "win_probability"]].to_string(index=False))
    print(f"\nPredicted winner: {top_team['team']}")


if __name__ == "__main__":
    main()
