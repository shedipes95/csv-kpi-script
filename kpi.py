import argparse, json
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser(description="Compute basic KPIs from a transactions CSV.")
parser.add_argument("csv", help="Path to transactions.csv")
parser.add_argument("--month", help="YYYY-MM (optional filter)")
args = parser.parse_args()

csv_path = Path(args.csv)
df = pd.read_csv(csv_path)
df["date"] = pd.to_datetime(df["date"])  # expects ISO yyyy-mm-dd

if args.month:
    year, month = args.month.split("-")
    df = df[(df["date"].dt.year == int(year)) & (df["date"].dt.month == int(month))]

# Basic KPIs
inflow = float(df.loc[df["amount"] > 0, "amount"].sum())
outflow = float(df.loc[df["amount"] < 0, "amount"].sum())
net = float(df["amount"].sum())
count = int(df.shape[0])

by_category = (
    df.groupby("category")["amount"].sum().sort_values()
    if not df.empty else pd.Series(dtype="float64")
)

summary = {
    "tx_count": count,
    "inflow": round(inflow, 2),
    "outflow": round(outflow, 2),
    "net": round(net, 2),
    "top_spend_categories": by_category.nsmallest(3).round(2).to_dict(),
}

print("=== KPI SUMMARY ===")
print(json.dumps(summary, indent=2))

# Write outputs
out_json = csv_path.with_name("kpi_summary.json")
out_cat = csv_path.with_name("kpi_by_category.csv")
with open(out_json, "w") as f:
    json.dump(summary, f, indent=2)
if not by_category.empty:
    by_category.round(2).to_csv(out_cat, header=["amount"])
print(f"\nWrote: {out_json.name}" + (f", {out_cat.name}" if not by_category.empty else ""))