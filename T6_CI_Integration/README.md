# CLI To-Do Task Manager
## Overview
This project demonstrates security auditing and hardening of a Python CLI-based To-Do application. An existing implementation was reviewed to identify potential security weaknesses, followed by targeted fixes to improve robustness while preserving functionality and test coverage.

---

## Project Structure
```text
T5_Security/
├── todo/               # Application source code
├── security/           # Security utilities and hardening modules
├── tests/              # Unit and integration tests
├── reports/            # Security audit and validation reports
├── README.md
└── requirements.txt
```

---

## Security Review Approach
A structured security review was conducted focusing on:
- User input handling and sanitization
- Error reporting and information disclosure
- Persistent storage integrity
- Fault tolerance against malformed or tampered data

**Scope:** Local, non-networked Python CLI application.

---

## Identified Security Risks
- Unbounded user input leading to potential denial-of-service
- Control character injection in task titles
- Exposure of internal error details via CLI output
- Unsafe deserialization of corrupted storage files
- Partial storage corruption causing application failure
- Plaintext local data storage
- Lack of authorization controls in a shared environment

All risks are documented in detail in the security audit report.

---

## Security Enhancements Applied
- Centralized input validation and sanitization
- Secure error handling with internal logging
- Safe deserialization and schema validation for stored data
- Fault-tolerant handling of partially corrupted storage
- Improved storage integrity without altering business logic

Security-related logic is isolated from core application logic to improve maintainability and auditability.

---

## Security Testing and Validation
The following test scenarios were executed to validate the implemented security controls:

### 1. Run full automated test suite
```bash
pytest
```

### 2. Reject empty task titles
```bash
python todo/main.py add ""
```

### 3. Reject oversized input (denial-of-service prevention)
```bash
python todo/main.py add "$(python -c 'print("A"*1000)')"
```

### 4. Prevent invalid priority values
```bash
python todo/main.py add "Test task" --priority urgent
```

### 5. Handle corrupted storage safely
```bash
echo "{ invalid json }" > todo/tasks.json
python todo/main.py list
```

### 6. Prevent modification of completed tasks
```bash
python todo/main.py complete 1
python todo/main.py update 1 --title "New title"
```

### 7. Verify persistence integrity across reloads
```bash
python todo/main.py add "Persistent task"
python todo/main.py list
```

Detailed security testing results are documented in `reports/testing_and_validation.md`.
