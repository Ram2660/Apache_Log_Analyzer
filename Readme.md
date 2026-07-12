# Log Analyzer

A Python-based log analyzer that reads Apache-style access logs and generates useful statistics about server activity. This project was built as part of my Python and DevOps learning journey, progressing from a basic parser to a more robust log analysis tool.

---

## Features

### Current Features (Version 1)

* Read Apache-style access logs.
* Count total requests.
* Count HTTP status codes.
* Count HTTP request methods.
* Count client IP addresses.
* Count requested URLs.
* Find the busiest IP address.
* Find the most requested URL.
* Generate a clean summary report.
* Validate file paths before processing.

### Planned Improvements (Version 2)

* Parse logs using Regular Expressions (`re`).
* Command-line arguments using `argparse`.
* Better exception handling.
* Logging using Python's `logging` module.
* Export reports to CSV and JSON.
* Object-Oriented implementation.
* Unit tests.
* Support for multiple log files.
* Better formatted reports and statistics.

---

## Technologies Used

* Python 3
* pathlib
* Built-in Python libraries

---

## Sample Output

```
==========================
      LOG ANALYZER
==========================

Total Requests : 500

Status Codes
------------
200 : 241
404 : 37
500 : 12

HTTP Methods
------------
GET : 315
POST : 110
PUT : 40
DELETE : 35

Top IP
------
192.168.1.10 (48 Requests)

Top URL
-------
/index.html (76 Requests)
```

---

## Project Structure

```
log-analyzer/
│
├── log_analyzer.py
├── access.log
├── README.md
└── .gitignore
```

---

## How to Run

Clone the repository:

```bash
git clone <repository-url>
cd log-analyzer
```

Run the program:

```bash
python log_analyzer.py
```

Enter the path to your log file when prompted.

---

## Learning Objectives

This project helped me practice:

* File handling
* String manipulation
* Dictionaries
* Functions
* Code refactoring
* Modular programming
* Log parsing
* Basic data analysis

---

## Future Roadmap

* Smarter log parsing using Regular Expressions.
* Export reports to CSV and JSON.
* Detect suspicious IP addresses.
* Support multiple log formats.
* Add automated tests.
* Package as a command-line utility.

---
