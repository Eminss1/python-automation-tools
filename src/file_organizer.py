#!/usr/bin/env python3
import argparse, shutil
from pathlib import Path

def organize(target: Path):
    target = target.expanduser().resolve()
    if not target.is_dir():
        raise SystemExit(f"Not a directory: {target}")

    for p in target.iterdir():
        if p.is_file():
            ext = p.suffix.lower().lstrip(".") or "no_extension"
            dest = target / ext
            dest.mkdir(exist_ok=True)
            shutil.move(str(p), str(dest / p.name))
    print(f"Organized files in: {target}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Organize files by extension.")
    ap.add_argument("--target", type=Path, required=True, help="Folder to organize")
    args = ap.parse_args()
    organize(args.target)
