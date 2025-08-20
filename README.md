# CSV → KPI (tiny CLI)
Reads a simple transactions CSV and prints basic KPIs (inflow/outflow/net) and per-category totals. Optional `--month YYYY-MM` filter.

## Run
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python kpi.py transactions.csv --month 2025-07