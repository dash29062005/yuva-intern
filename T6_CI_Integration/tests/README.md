# Automated Test Suite – CLI To-Do Application

## Purpose
This folder contains the **automated test suite** for the CLI To-Do Task Manager.  
The tests were designed to validate the correctness, reliability, and integration of the application’s core components without relying on manual verification.

The test suite follows a clear separation between **unit tests** and **integration tests**, ensuring that individual components work correctly both in isolation and when combined.

---

## Test Structure
```text
tests/
├── test_task.py
├── test_task_manager.py
├── test_storage.py
└── test_integration_flow.py
```
Each test file focuses on a specific layer of the application.

---

## Test File Descriptions

### 1. `test_task.py` – Task Domain Model Tests
**Type:** Unit Tests  

Covered scenarios:
- Successful creation of a task with valid input
- Rejection of invalid task data (empty title, invalid priority)
- Status transition when a task is marked as completed
- Enforcement of immutability for completed tasks

**Goal:**  
Ensure that all business rules related to a single task are enforced at the model level.

---

### 2. `test_task_manager.py` – Business Logic Tests
**Type:** Unit Tests  

Covered scenarios:
- Automatic task ID generation
- Correct handling of add, update, delete, and complete operations
- Protection against invalid task IDs
- Prevention of unintended data modification during updates

**Goal:**  
Confirm that task-related logic works correctly independent of the CLI and storage layers.

---

### 3. `test_storage.py` – Persistence Layer Tests
**Type:** Unit Tests (I/O isolated using temporary paths)

Covered scenarios:
- Automatic creation of the storage file when missing
- Correct save-and-load behavior
- Proper error handling when the JSON file is corrupted

**Goal:**  
Ensure data persistence is reliable and failure scenarios are handled explicitly.

---

### 4. `test_integration_flow.py` – System Integration Test
**Type:** Integration Test  

Covered scenario:
- Add task → save to storage → reload → verify task data

**Goal:**  
Confirm that the application behaves correctly as a complete system.

---

## How to Run Tests
From the project root directory:

```bash
pytest
```

All tests are fully automated and require no manual setup.

---

## Testing Strategy Summary
- Business logic is tested independently of the CLI.
- File system interactions are isolated using temporary paths.
- Tests are deterministic, fast, and repeatable.
