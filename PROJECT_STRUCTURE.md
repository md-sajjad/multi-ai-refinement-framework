# Project Structure

This document provides an overview of the complete directory structure and file organization for the Multi-AI Refinement Framework.

## 📂 Directory Tree

```
multi-ai-refinement-framework/
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI/CD pipeline
│
├── src/
│   └── ai_refinement_framework/
│       ├── __init__.py               # Main package module with core classes
│       └── py.typed                  # PEP 561 type checking marker
│
├── tests/
│   ├── __init__.py                   # Test package initialization
│   └── test_framework.py             # Comprehensive test suite
│
├── examples/
│   └── basic_usage.py                # Basic usage examples and patterns
│
├── .gitattributes                    # Git line ending and file handling rules
├── .gitignore                        # Git ignore patterns for Python projects
├── .pre-commit-config.yaml           # Pre-commit hooks configuration
├── CHANGELOG.md                      # Version history and release notes
├── CONTRIBUTING.md                   # Contribution guidelines
├── env.example                       # Example environment variables file
├── LICENSE                           # Apache 2.0 License
├── Makefile                          # Common development tasks
├── PROJECT_STRUCTURE.md              # This file
├── pyproject.toml                    # Modern Python package configuration
├── pytest.ini                        # Pytest configuration
├── QUICKSTART.md                     # Quick start guide for new users
└── README.md                         # Main project documentation
```

## 📄 File Descriptions

### Configuration Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Modern Python packaging configuration with dependencies, metadata, and tool settings |
| `pytest.ini` | Pytest test runner configuration |
| `.pre-commit-config.yaml` | Pre-commit hooks for code quality (Black, Ruff, MyPy, etc.) |
| `.gitignore` | Files and directories to ignore in version control |
| `.gitattributes` | Git attributes for consistent line endings and export rules |
| `env.example` | Example environment variables (copy to `.env`) |
| `Makefile` | Shortcuts for common development tasks |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation and feature overview |
| `QUICKSTART.md` | 5-minute quick start guide with examples |
| `CONTRIBUTING.md` | Guidelines for contributing to the project |
| `CHANGELOG.md` | Version history and release notes |
| `PROJECT_STRUCTURE.md` | This file - project organization reference |
| `LICENSE` | Apache 2.0 open source license |

### Source Code

| File | Purpose |
|------|---------|
| `src/ai_refinement_framework/__init__.py` | Main package module with all core classes and APIs |
| `src/ai_refinement_framework/py.typed` | Marker file for type checking support (PEP 561) |

### Tests

| File | Purpose |
|------|---------|
| `tests/__init__.py` | Test package initialization |
| `tests/test_framework.py` | Comprehensive unit tests for all framework components |

### Examples

| File | Purpose |
|------|---------|
| `examples/basic_usage.py` | Runnable examples demonstrating framework features |

### CI/CD

| File | Purpose |
|------|---------|
| `.github/workflows/ci.yml` | GitHub Actions workflow for automated testing, linting, and building |

## 🎯 Key Components

### Core Classes (in `src/ai_refinement_framework/__init__.py`)

1. **AIFramework**
   - Main framework class
   - Manages agents and providers
   - Handles dispatching and prompt management

2. **Role** (Enum)
   - GENERATOR: Creates initial content
   - REVIEWER: Provides critical feedback
   - REFINER: Improves based on feedback
   - QA_ANALYST: Validates quality
   - ORCHESTRATOR: Coordinates workflows

3. **ModelTier** (Enum)
   - PRO: High-capability models
   - FLASH: Fast, cost-effective models

4. **Provider** (Protocol)
   - Interface for AI provider implementations
   - Ensures consistent behavior across providers

5. **CAIRPipeline**
   - Continuous AI Refinement workflow
   - Iterative improvement process
   - Quality threshold management

6. **RefinementResult**
   - Contains final output and metadata
   - Quality scores and iteration history
   - Context preservation

## 🔧 Development Workflow

### Essential Commands

```bash
# Install development dependencies
make install-dev

# Run tests
make test

# Run tests with coverage
make coverage

# Format code
make format

# Lint code
make lint

# Type check
make type-check

# Run all checks
make all

# Clean build artifacts
make clean

# Build distribution
make build
```

### Pre-commit Hooks

Automatically run on each commit:
- Trailing whitespace removal
- File ending fixes
- YAML/TOML/JSON validation
- Black formatting
- Ruff linting
- MyPy type checking
- Bandit security checks

## 📦 Package Distribution

### Build Process

1. **Source Distribution**: Contains all source files
2. **Wheel Distribution**: Pre-built binary package
3. **Location**: `dist/` directory after building

### Installation Modes

```bash
# Install from PyPI (when published)
pip install ai-refinement-framework

# Install with specific providers
pip install ai-refinement-framework[openai]
pip install ai-refinement-framework[anthropic]
pip install ai-refinement-framework[google]
pip install ai-refinement-framework[all]

# Install for development
pip install -e ".[dev,all]"
```

## 🧪 Testing

### Test Organization

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions (marked with `@pytest.mark.integration`)
- **Coverage Target**: >90% code coverage

### Test Files

- `tests/test_framework.py`: Comprehensive tests for all core functionality

## 📊 Code Quality Tools

| Tool | Purpose | Configuration |
|------|---------|---------------|
| Black | Code formatting | `pyproject.toml` |
| Ruff | Fast linting | `pyproject.toml` |
| MyPy | Type checking | `pyproject.toml` |
| Pytest | Testing | `pytest.ini`, `pyproject.toml` |
| Coverage | Code coverage | `pyproject.toml` |
| Bandit | Security checking | `pyproject.toml` |
| Pre-commit | Git hooks | `.pre-commit-config.yaml` |

## 🚀 CI/CD Pipeline

### GitHub Actions Workflows

**ci.yml**: Runs on push and pull requests
- **Test Job**: Tests on Python 3.9-3.12, Linux/Mac/Windows
- **Lint Job**: Black, Ruff, MyPy checks
- **Security Job**: Bandit security scanning
- **Build Job**: Package building and validation
- **Coverage**: Uploads to Codecov

## 📝 Version Management

Version is defined in:
1. `src/ai_refinement_framework/__init__.py` (`__version__`)
2. `pyproject.toml` (`version`)

Both should be kept in sync.

## 🔐 Security

- API keys stored in `.env` (never committed)
- `env.example` provides template
- Bandit security scanning in CI/CD
- No secrets in code or tests

## 🌟 Best Practices

1. **Type Hints**: All functions have type annotations
2. **Docstrings**: Google-style docstrings throughout
3. **Testing**: High test coverage with meaningful tests
4. **Code Style**: Black formatting, Ruff linting
5. **Git**: Conventional commit messages
6. **Documentation**: Comprehensive docs and examples

## 📈 Extending the Framework

### Adding New Components

1. **New Provider**: Implement the `Provider` protocol
2. **New Role**: Add to the `Role` enum
3. **New Workflow**: Subclass or compose with `AIFramework`
4. **New Tests**: Add corresponding test cases

### File Locations

- **Core Code**: `src/ai_refinement_framework/`
- **Tests**: `tests/`
- **Examples**: `examples/`
- **Documentation**: Root directory (`.md` files)

## 🎓 Learning Path

1. **Start**: Read `README.md` for overview
2. **Quick Start**: Follow `QUICKSTART.md` for hands-on
3. **Examples**: Run `examples/basic_usage.py`
4. **Source**: Study `src/ai_refinement_framework/__init__.py`
5. **Tests**: Review `tests/test_framework.py` for usage patterns
6. **Contribute**: Read `CONTRIBUTING.md` to contribute back

---

**Last Updated**: 2024-11-07
**Framework Version**: 0.1.0

