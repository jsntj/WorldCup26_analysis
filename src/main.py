from pathlib import Path

import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    dataset_path = project_root / "input" / "international_results.csv"

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    df = pd.read_csv(dataset_path)

    print("Dataset loaded successfully")
    print(f"Path: {dataset_path}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print("Sample columns:", ", ".join(df.columns[:8]))


if __name__ == "__main__":
    main()
