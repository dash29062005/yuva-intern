# CLI To-Do Task Manager – CI Integration 

![CI](https://github.com/dash29062005/yuva-intern/actions/workflows/ci.yml/badge.svg)

## Overview
This project demonstrates the integration of a Continuous Integration (CI) pipeline for a Python CLI-based To-Do application as part of **Task 6**. The objective is to automate code quality checks by running linting and tests on relevant code changes, simulating a professional development workflow used in real-world software projects.

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
The CI workflow configuration file (`ci.yml`) is located at the repository root under  
`.github/workflows/ci.yml`, as required by GitHub Actions.

---

## CI Tool Used
GitHub Actions was selected due to its seamless integration with GitHub and its widespread adoption in professional Python development workflows.

---

## CI Pipeline Overview
The CI pipeline is defined in `.github/workflows/ci.yml` and performs the following steps automatically:
- Checks out the repository source code
- Sets up Python 3.10
- Installs project dependencies
- Runs static code analysis using `flake8`
- Executes the complete test suite using `pytest`

The pipeline is configured to fail immediately if linting or tests do not pass, ensuring strict quality enforcement.

---

## CI Workflow Configuration (Summary)
```yaml
name: Python CI (Task 6)

on:
  push:
    paths:
      - "T6_CI_Integration/**"
  pull_request:
    paths:
      - "T6_CI_Integration/**"
```

This configuration ensures that CI runs only when Task 6 files are modified, which is appropriate for a multi-task internship repository.

---

## Trigger Conditions
The CI workflow runs automatically when:
- A push modifies files under `T6_CI_Integration/`
- A pull request modifies files under `T6_CI_Integration/`

This scoped triggering prevents unnecessary CI runs for unrelated internship tasks.

---

## CI Execution Commands
The following commands are executed automatically by the CI pipeline and can also be run locally to reproduce the same checks:

```bash
cd T6_CI_Integration
pip install -r requirements.txt
flake8 .
pytest
```

---

## Documentation
Detailed information about the CI setup, configuration decisions, and validation process is available in:
```
reports/ci_report.md
```

---

## Conclusion
By integrating a scoped Continuous Integration pipeline, this project enforces automated linting and testing for Task 6 without affecting other internship tasks. The CI setup improves code reliability, reduces manual verification effort, and demonstrates a professional approach to maintaining code quality through automation.
