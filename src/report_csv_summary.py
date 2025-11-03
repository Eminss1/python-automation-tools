#!/usr/bin/env python3
import argparse, pandas as pd
from pathlib import Path

def summarize(input_csv: Path, out_csv: Path):
    df = pd.read_csv(input_csv)
    desc = df.describe(include="all").transpose()
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    desc.to_csv(out_csv)
    print(f"Summary saved to: {out_csv}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Summarize a CSV file.")
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=Path("./reports/summary.csv"))
    args = ap.parse_args()
    summarize(args.input, args.out)
