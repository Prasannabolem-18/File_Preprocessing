# Log Analyzer Project
## Overview
The **Log Analyzer** is a Python file-processing project that reads a log file, analyzes log entries, and generates a structured summary report.

The program counts different log levels and extracts error messages while implementing proper exception handling and logging mechanisms.

---

## Objectives

This project demonstrates:

* File Reading & Writing
* String Processing
* Log File Analysis
* Exception Handling
* Python Logging Module
* Structured Output Generation
* Git Version Control

---

##  Project Folder Structure

```
LogAnalyzer/
│
├── log_analyzer.py     # Main Python script
├── app.log             # Input log file
├── report.txt          # Generated summary report
├── analyzer.log        # Application log output
└── README.md           # Project documentation
```

---

## Features

✅ Reads log data from a file
✅ Counts log types (INFO, WARNING, ERROR)
✅ Extracts all ERROR messages
✅ Generates structured report
✅ Handles runtime exceptions
✅ Maintains execution logs

---

## Log File Format

Each log entry must follow:

```
YYYY-MM-DD HH:MM:SS LOG_TYPE MESSAGE
```

### Example

```
2026-04-07 10:03:00 ERROR Failed to connect to database
```

### Supported Log Types

* INFO
* WARNING
* ERROR

---

## Exception Handling

The program safely handles:

* **File Not Found** → when `app.log` is missing
* **Empty File** → when file has no valid content
* **Incorrect Log Format** → invalid entries are skipped and logged

Errors are recorded in `analyzer.log`.

---

##  Logging System

Python's built-in **logging module** is used.

Log file generated:

```
analyzer.log
```

Logging Levels:

* INFO → Successful operations
* ERROR → Processing errors & invalid log lines

---

##  How to Run

1. Install Python (3.x).
2. Place `app.log` inside the project folder.
3. Run the program:

```
python log_analyzer.py
```

---

##  Output Files

### 1️⃣ report.txt

Contains:

* Log summary counts
* Extracted ERROR messages

### 2️⃣ analyzer.log

Stores execution logs and error details.

---

##  Version Control

Git is used for version control.

Example commits:

* Added file reading functionality
* Implemented log processing
* Added exception handling
* Generated summary report

Project uploaded to GitHub repository.

---

