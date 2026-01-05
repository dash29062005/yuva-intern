# Security Module

This directory contains security-focused components introduced during Week 5 to harden the Python CLI To-Do application.

## Purpose
The security module isolates defensive logic from core business logic to ensure consistent enforcement of security controls and simplify auditing and maintenance.

## Components

- `validators.py`  
  Centralized input validation and sanitization logic used to prevent malformed, oversized, or unsafe user input.

- `logger.py`  
  Secure internal error logging utility that records diagnostic information without exposing sensitive details to end users.

- `safe_io.py`  
  Safe deserialization and schema validation layer for persistent storage, designed to tolerate partial corruption and prevent crashes from tampered data.

## Security Principles Applied
- Input validation and sanitization  
- Information disclosure prevention  
- Secure logging  
- Safe deserialization  
- Fault tolerance

## Scope
Local, non-networked Python CLI application operating within a local trust boundary.
