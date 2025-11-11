# Python Automation Tools

Small Python utilities that automate everyday workflows: file organization, scheduled backups, quick reporting and other productivity tasks.

## Overview
This repository demonstrates practical problem-solving with Python — short, useful scripts that improve efficiency and daily work routines.

## Features
- Organize files by extension or date
- Create timestamped directory backups
- Generate simple CSV summary reports
- Cross-platform (tested on Windows & Linux)

## Installation
git clone https://github.com/Eminss1/python-automation-tools.git
cd python-automation-tools
python -m venv .venv
.venv\Scripts\activate   # on Windows
pip install -r requirements.txt

## Usage
### Organize files inside a folder
python src/file_organizer.py --target ./Downloads

### Backup a directory into ./backups/
python src/auto_backup.py --source ./project --dest ./backups

### Generate a summary of a CSV file
python src/report_csv_summary.py --input data.csv --out reports/summary.csv

## Project Structure
python-automation-tools/
├─ src/
│  ├─ file_organizer.py
│  ├─ auto_backup.py
│  └─ report_csv_summary.py
├─ examples/
├─ requirements.txt
└─ README.md

## Future Improvements

- Add CLI menu and logging
- Add scheduled (cron) tasks
- Add GUI wrapper (Tkinter)

## License
MIT
