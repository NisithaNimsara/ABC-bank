# ABC Bank — Savings Account Management System

## Overview

This repository contains a simple Python-based system for ABC Bank (Sri Lanka) to register and manage savings account customer details. It supports opening new accounts, viewing individual or all customer details (account number, name, balance), updating customer information (except account number and balance), and processing deposits and withdrawals with balance validation.

## Features

- Create/open new savings accounts
- View a single customer's details by account number
- List all customers and balances
- Update customer information (name, contact, address) — account number and balance are immutable via update
- Deposit funds and withdraw funds with validation (no overdrafts)
- Simple file-based persistent storage (see repository for exact implementation)

## Requirements

- Python 3.8+
- (Optional) Dependencies listed in requirements.txt, if present

## Installation

1. Clone the repository:
   git clone https://github.com/NisithaNimsara/ABC-bank.git
   cd ABC-bank

2. (Optional) Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows

3. Install dependencies (if any):
   pip install -r requirements.txt

## Usage

Replace `main.py` below with the actual entrypoint in this repository if different.

Run the app (example):

    python main.py

Common example actions (adjust to actual CLI in repo):

- Create a new account:
    python main.py create --name "Jane Doe" --initial-deposit 5000 --contact "077xxxxxxx"

- View a customer:
    python main.py view --account 1001

- List all customers:
    python main.py list

- Update customer info:
    python main.py update --account 1001 --name "Jane A. Doe" --contact "077yyyyyyy"

- Deposit:
    python main.py deposit --account 1001 --amount 2000

- Withdraw:
    python main.py withdraw --account 1001 --amount 1500

If the repository uses a different entrypoint or a GUI/Flask app, refer to the project files for exact commands.

## Data storage

The app uses a simple persistent storage mechanism (JSON/CSV/file-based). Check the repository files to find where account data is stored (commonly a `data/` folder or a JSON file).

## Project structure (example)

- README.md                     — Project documentation
- main.py / app.py               — Application entrypoint (adjust to repo)
- bank/ or src/                  — Core modules with account logic
- data/                          — Persistent storage files
- tests/                         — Unit tests (if any)
- requirements.txt               — Python dependencies (if any)

## Testing

If tests exist, run them with:

    pytest

Consider adding unit tests for core behaviors: account creation, deposit/withdraw, and updates.

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repo
2. Create a feature branch: git checkout -b feature/your-feature
3. Make changes and add tests
4. Commit: git commit -m "Add feature"
5. Push and open a pull request against the `main` branch

## License

If a LICENSE file is not yet present, add one (e.g., MIT) or confirm the desired license.

## Contact

Maintainer: NisithaNimsara (https://github.com/NisithaNimsara)

## Acknowledgements

Built for ABC Bank (Sri Lanka). Thank you to contributors and testers.
