# CI Pipeline Report

## Overview
This report describes the Continuous Integration (CI) pipeline implemented for the Python CLI To-Do application as part of Week 6. The goal of the pipeline is to automatically validate code quality and correctness on every code change.

## CI Tool Selection
GitHub Actions was chosen due to its native GitHub integration, ease of configuration, and widespread industry adoption for Python-based projects.

## Pipeline Trigger Conditions
The CI workflow is automatically triggered on:
- Every push to the `main` branch
- Every pull request targeting the `main` branch

This ensures that all code changes are validated before and after integration.

## Pipeline Stages

1. **Source Code Checkout**  
   The repository is checked out using the official `actions/checkout` action.

2. **Python Environment Setup**  
   Python version 3.10 is provisioned using `actions/setup-python`, ensuring a consistent execution environment.

3. **Dependency Installation**  
   All required dependencies are installed from `requirements.txt` to replicate the local development environment.

4. **Static Code Analysis (Linting)**  
   `flake8` is executed to enforce coding standards and detect syntax or style-related issues early in the pipeline.

5. **Automated Testing**  
   The complete test suite is executed using `pytest`. Any test failure causes the pipeline to fail immediately.

## Failure Handling
The pipeline is configured to stop execution and report failure if either linting or testing fails, preventing faulty code from being merged.

## Verification
The CI configuration was verified by committing changes to the repository and observing successful and failed runs in the GitHub Actions interface. This confirmed correct trigger behavior and failure detection.

## Outcome
The implemented CI pipeline automates quality checks, reduces manual testing effort, and ensures that only validated code progresses through the development workflow, reflecting a professional CI/CD practice.
