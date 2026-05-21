# WorldCup26_analysis

Python workspace for World Cup 2026 analysis.

## Structure

```
.
├── .venv/                       # Local virtual environment
├── input/                       # Dataset storage
│   └── international_results.csv
├── src/
│   └── main.py                  # Starter analysis script
├── requirements.txt
└── README.md
```

## Quick Start

1. Activate the virtual environment:

	```bash
	source .venv/bin/activate
	```

2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Run the starter script:

	```bash
	python src/main.py
	```

## Dataset

Dataset downloaded into `input/international_results.csv` from:

- https://raw.githubusercontent.com/martj42/international_results/master/results.csv