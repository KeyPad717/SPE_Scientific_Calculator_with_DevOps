# SPE_Scientific_Calculator_with_DevOps
# Scientific Calculator (CLI)

A command-line scientific calculator implemented in Python and prepared for a DevOps pipeline.
The project includes modular calculator operations and automated unit testing using **Pytest**.

---

## Features

The calculator supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division
* Factorial
* Natural logarithm (ln)
* Power function
* Square root

The application runs in a **menu-driven CLI interface**.

---

## Project Structure

```
scientific-calculator
│
├── calculator
│   ├── __init__.py
│   ├── main.py
│   └── operations.py
│
├── tests
│   └── test_calculator.py
│
├── README.md
└── .gitignore
```

* `calculator/` – contains the calculator application code
* `operations.py` – implementation of mathematical functions
* `main.py` – CLI interface for user interaction
* `tests/` – automated unit tests using Pytest

---

## Running the Calculator

From the project root directory:

```
python3 calculator/main.py
```

This launches the menu-driven scientific calculator.

---

## Running Unit Tests

The project includes automated tests for all calculator operations.

Run tests using:

```
python3 -m pytest tests/
```

Pytest automatically discovers and executes all test cases.

---

## Technologies Used

* **Python** – application implementation
* **Pytest** – unit testing framework
* **Git & GitHub** – source control

---

## Upcoming DevOps Pipeline

The project will be extended with the following DevOps tools:

* **Jenkins** – Continuous Integration
* **Docker** – Application containerization
* **Docker Hub** – Container image registry
* **Ansible** – Automated deployment

These steps will enable a full **CI/CD pipeline for the calculator application**.

