#!/usr/bin/env python3
import argparse, zipfile, time
from pathlib import Path

def backup(source: Path, dest: Path):
    source = source.resolve()
    dest.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    zip_path = dest / f"{source.name}-{ts}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in source.rglob("*"):
            if p.is_file():
                zf.write(p, p.relative_to(source))
    print(f"Created: {zip_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="ZIP backup of a directory.")
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--dest", type=Path, default=Path("./backups"))
    args = ap.parse_args()
    backup(args.source, args.dest)
