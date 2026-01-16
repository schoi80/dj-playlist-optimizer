.PHONY: help install test lint format pre-commit clean run-example check

# Default target
.DEFAULT_GOAL := help

help:
	@echo "🎧 DJ Playlist Optimizer - Development Makefile"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Available targets:"
	@echo "  install      Install dependencies and pre-commit hooks"
	@echo "  test         Run tests with pytest"
	@echo "  lint         Run ruff check and auto-fix"
	@echo "  format       Run ruff formatter"
	@echo "  check        Run lint and test"
	@echo "  pre-commit   Run all pre-commit hooks"
	@echo "  clean        Remove temporary files and virtual environment"
	@echo "  run-example  Run the SDK usage example"

install:
	uv sync --dev
	uv run pre-commit install
	uv run pre-commit install --hook-type commit-msg

test:
	uv run python -m pytest

lint:
	uv run ruff check --fix

format:
	uv run ruff format

check: lint test

pre-commit:
	uv run pre-commit run --all-files

clean:
	rm -rf .venv .pytest_cache .ruff_cache build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

run-example:
	uv run python examples/sdk_usage.py
