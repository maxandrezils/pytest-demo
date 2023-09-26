# pytest-demo

Practice and Demo using pytest to test an API

## Installation Guide

This guide assumes you have Poetry installed to manage Python Virtual Environments.
To install the project's dependencies, run:
`poetry install`

## Running the Tests

To run the tests, run the following command

```bash
poetry run pytest
```

To run the tests with an HTML report

```bash
poetry run pytest -v -s --html=report.html --self-contained-html
```
