# WorldCup26_analysis

Small Python project to start analysis from previous FIFA World Cup data and generate an initial 2026 winner prediction with a simple agent.

## Setup (venv)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run prediction agent

```bash
python -m worldcup26_analysis.agent
```

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
