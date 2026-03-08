# E-Submission Automation Test

Automation testing project for the **E-Submission module** using **Python, Playwright, and Behave (BDD)** with **Page Object Model (POM)** structure.

## Tech Stack

* Python
* Playwright
* Behave (BDD)

## Project Structure

```
project
├── features        # BDD feature files
├── steps           # Step definitions
├── pages           # Page Object Model
├── locators        # UI locators
├── files           # Test files for upload
├── environment.py  # Test setup
└── requirements.txt
```

## Installation

```
pip install -r requirements.txt
playwright install
```

## Run Tests

```
behave
```

## Test Scope

* Login
* Create submission
* Upload files
* Submit submission
* Terminate submission
