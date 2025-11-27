# ABC Bank - Savings Account Management System

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
