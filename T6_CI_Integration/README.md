# CLI To-Do Task Manager – CI Integration (Task 6)

![CI](https://github.com/dash29062005/yuva-intern/actions/workflows/ci.yml/badge.svg)

## Overview
This project demonstrates the integration of a Continuous Integration (CI) pipeline for a Python CLI-based To-Do application as part of **Task 6**. The objective is to automate code quality checks by running linting and tests on relevant code changes, simulating a professional development workflow.

---

## Project Structure
```text
T6_CI_Integration/
├── todo/               # Application source code
├── security/           # Security utilities (from previous tasks)
├── tests/              # Unit and integration tests
├── reports/
│   └── ci_report.md    # CI pipeline documentation
├── README.md
├── requirements.txt
└── .flake8
```

**Note:**  
The CI workflow configuration is located at the repository root under  
`.github/workflows/ci.yml`, as required by GitHub Actions.

---

## CI Tool Used
GitHub Actions was selected due to its seamless GitHub integration and widespread industry adoption for Python projects.

---

## CI Pipeline Overview
The CI pipeline is defined in `.github/workflows/ci.yml` and performs the following steps automatically:
- Checks out the repository source code
- Sets up Python 3.10
- Installs project dependencies
- Runs static code analysis using `flake8`
- Executes the full test suite using `pytest`

The pipeline is configured to fail immediately if linting or tests do not pass.

---

## Trigger Conditions
The CI workflow is scoped specifically to **Task 6** and runs automatically when:
- A push modifies files under `T6_CI_Integration/`
- A pull request modifies files under `T6_CI_Integration/`

This ensures CI validation applies only to Task 6 within a multi-task internship repository.

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
By integrating a scoped CI pipeline, the project enforces automated quality checks for Task 6 without affecting other internship tasks. This improves reliability, reduces manual testing effort, and demonstrates a professional approach to maintaining code quality through automation.
