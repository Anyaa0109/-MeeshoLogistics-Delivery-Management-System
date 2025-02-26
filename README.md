Flask-Based SQL Query Executor

Overview

This project is a Flask-based SQL Query Executor designed for a logistics database. It allows users to execute SQL queries securely on an Oracle DB, handling over 50 queries per day. The system is optimized for managing orders, shipments, and returns, improving query efficiency by 30%.

Features

Flask-based Web Interface: Enables users to execute SQL queries easily.

Oracle DB Integration: Seamlessly connects with an Oracle database.

Secure Query Execution: Prevents SQL injection and unauthorized access.

Optimized Performance: Structured database design improves efficiency.

Logging and Monitoring: Keeps track of query executions for auditing.

Installation

Prerequisites

Python 3.x

Flask

cx_Oracle (for Oracle DB connection)

Oracle Database instance

Setup

Clone the repository:

git clone https://github.com/your-repo/flask-sql-executor.git
cd flask-sql-executor

Install dependencies:

pip install -r requirements.txt

Configure database settings in config.py:

DB_CONFIG = {
    'username': 'your_username',
    'password': 'your_password',
    'dsn': 'your_oracle_dsn'
}

Run the application:

python app.py

Access the web interface at http://127.0.0.1:5000

Usage

Enter a valid SQL query in the web interface.

Execute the query.

View and download the results.

Security Measures

Parameterized queries to prevent SQL injection.

Role-based access control (RBAC) for user authentication.

Query logging for audit trails.

Contributing

Fork the repository.

Create a feature branch.

Commit your changes.

Push to your branch and create a pull request.
