.PHONY: help install install-dev test coverage lint format type-check clean build publish docs

# Default target
help:
	@echo "Multi-AI Refinement Framework - Development Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  install       - Install package in production mode"
	@echo "  install-dev   - Install package with development dependencies"
	@echo "  test          - Run tests"
	@echo "  coverage      - Run tests with coverage report"
	@echo "  lint          - Run linting checks"
	@echo "  format        - Format code with black and ruff"
	@echo "  type-check    - Run type checking with mypy"
	@echo "  clean         - Remove build artifacts and cache files"
	@echo "  build         - Build distribution packages"
	@echo "  publish       - Publish to PyPI (requires credentials)"
	@echo "  docs          - Generate documentation"
	@echo "  all           - Run format, lint, type-check, and test"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev,all]"
	pre-commit install

# Testing
test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=ai_refinement_framework --cov-report=html --cov-report=term-missing

# Code quality
lint:
	ruff check src/ tests/

format:
	black src/ tests/ examples/
	ruff check --fix src/ tests/

type-check:
	mypy src/

# Cleanup
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete

# Building
build: clean
	python -m build

# Publishing
publish: build
	python -m twine upload dist/*

publish-test: build
	python -m twine upload --repository testpypi dist/*

# Documentation
docs:
	@echo "Generating documentation..."
	@echo "TODO: Add documentation generation (e.g., sphinx, mkdocs)"

# Run all checks
all: format lint type-check test
	@echo "✅ All checks passed!"

# Quick check before commit
pre-commit: format lint type-check
	@echo "✅ Pre-commit checks complete!"

