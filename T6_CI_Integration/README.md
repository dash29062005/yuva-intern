# CLI To-Do Task Manager

![CI](https://github.com/dash29062005/yuva-intern/actions/workflows/ci.yml/badge.svg)


## Overview
This project demonstrates the integration of a Continuous Integration (CI) pipeline for a Python CLI-based To-Do application. The objective is to automate code quality checks by running linting and tests on every code change, simulating a professional development workflow.

---

## Project Structure
```text
Week6_CI_Integration/
├── todo/               # Application source code
├── security/           # Security utilities (from previous tasks)
├── tests/              # Unit and integration tests
├── reports/
│   └── ci_report.md    # CI pipeline documentation
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI configuration
├── README.md
├── requirements.txt
└── .flake8
```

---

## CI Tool Used
GitHub Actions was selected due to its seamless GitHub integration and widespread industry use for Python projects.

---

## CI Pipeline Overview
The CI pipeline is defined in `.github/workflows/ci.yml` and performs the following steps automatically:
- Checks out the repository code
- Sets up Python 3.10
- Installs project dependencies
- Runs static code analysis using `flake8`
- Executes the full test suite using `pytest`

The pipeline is configured to fail immediately if linting or tests do not pass.

---

## Trigger Conditions
The CI workflow runs automatically on:
- Every push to the `main` branch
- Every pull request targeting the `main` branch

This ensures continuous validation of all code changes.

---

## Running CI Checks Locally
To replicate the CI steps on a local machine:

```bash
pip install -r requirements.txt
flake8 .
pytest
```

---

## Documentation
Detailed information about the CI setup, configuration, and verification process is available in:
```
reports/ci_report.md
```

---

## Conclusion
By integrating a CI pipeline, the project now enforces automated quality checks for every code change. This improves reliability, reduces manual testing effort, and demonstrates a professional approach to maintaining code quality through automation.

CI trigger

