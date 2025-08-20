# CSV → KPI (tiny Python CLI)

A minimal **Python + pandas** CLI that ingests a simple `transactions.csv` and outputs basic KPIs:
- **inflow**, **outflow**, **net**
- per-category totals (CSV)
- a JSON summary file
- optional month filter: `--month YYYY-MM`

> **Why Herbst:** pragmatic, back-office style summary for statement/CSV data. Clean, explainable outputs suitable for ERP/reporting use cases.

---

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python kpi.py transactions.csv --month 2025-07
