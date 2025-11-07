# Contributing to Multi-AI Refinement Framework

Thank you for your interest in contributing to the Multi-AI Refinement Framework! This document provides guidelines and instructions for contributing.

## 🎯 Ways to Contribute

- **Bug Reports**: Submit detailed bug reports with reproduction steps
- **Feature Requests**: Propose new features or enhancements
- **Documentation**: Improve docs, add examples, fix typos
- **Code**: Fix bugs, implement features, optimize performance
- **Tests**: Add or improve test coverage
- **Provider Integrations**: Add support for new AI providers

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/multi-ai-refinement-framework.git
cd multi-ai-refinement-framework
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev,all]"

# Install pre-commit hooks
pre-commit install
```

### 3. Create a Branch

```bash
# Create a branch for your changes
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📝 Development Guidelines

### Code Style

We use automated tools to maintain code quality:

- **Black**: Code formatting
- **Ruff**: Linting and import sorting
- **MyPy**: Type checking

```bash
# Format code
black src/ tests/

# Check linting
ruff check src/ tests/

# Type checking
mypy src/
```

### Code Standards

1. **Type Hints**: Use type hints for all function signatures
   ```python
   def process_data(input: str, config: Dict[str, Any]) -> Result:
       ...
   ```

2. **Docstrings**: Use Google-style docstrings
   ```python
   def example_function(param1: str, param2: int) -> bool:
       """
       Brief description of the function.
       
       Args:
           param1: Description of param1
           param2: Description of param2
           
       Returns:
           Description of return value
           
       Raises:
           ValueError: When param2 is negative
       """
       ...
   ```

3. **Error Handling**: Use appropriate exceptions with clear messages
   ```python
   if not config:
       raise ValueError("Configuration cannot be empty")
   ```

4. **Naming Conventions**:
   - Classes: `PascalCase`
   - Functions/Methods: `snake_case`
   - Constants: `UPPER_CASE`
   - Private members: `_leading_underscore`

### Testing

All code changes should include tests:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_refinement_framework --cov-report=html

# Run specific test file
pytest tests/test_framework.py

# Run specific test
pytest tests/test_framework.py::TestAIFramework::test_dispatch
```

**Testing Guidelines:**
- Aim for >90% code coverage
- Test edge cases and error conditions
- Use meaningful test names: `test_<what>_<condition>_<expected>`
- Use fixtures for common setup
- Mock external API calls

### Documentation

- Update README.md for user-facing changes
- Add/update docstrings for new/modified code
- Add examples to the `examples/` directory for major features
- Update CHANGELOG.md (if present) with your changes

## 🔄 Pull Request Process

### 1. Before Submitting

- [ ] All tests pass (`pytest`)
- [ ] Code is formatted (`black`)
- [ ] Linting passes (`ruff check`)
- [ ] Type checking passes (`mypy`)
- [ ] Documentation is updated
- [ ] Changes are covered by tests
- [ ] Commit messages are clear and descriptive

### 2. Commit Messages

Follow conventional commits format:

```
type(scope): brief description

Longer description if needed

Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(providers): add support for Anthropic Claude 3.5

docs: update README with new examples

fix(pipeline): handle empty responses in CAIR workflow
```

### 3. Submit Pull Request

1. Push your branch to your fork
2. Open a pull request against the `main` branch
3. Fill out the PR template completely
4. Link any related issues
5. Wait for review and address feedback

### 4. PR Review Process

- Maintainers will review your PR
- Address any requested changes
- Once approved, a maintainer will merge your PR
- Your contribution will be included in the next release!

## 🏗️ Architecture Overview

### Project Structure

```
multi-ai-refinement-framework/
├── src/
│   └── ai_refinement_framework/
│       ├── __init__.py          # Main API exports
│       ├── core/                # Core abstractions
│       ├── providers/           # Provider implementations
│       ├── workflows/           # Workflow implementations
│       └── utils/               # Utility functions
├── tests/                       # Test suite
├── examples/                    # Usage examples
└── docs/                        # Documentation
```

### Key Concepts

1. **Provider Abstraction**: All providers implement the `Provider` protocol
2. **Role-Based Design**: Agents are assigned roles (Generator, Reviewer, etc.)
3. **Framework Core**: `AIFramework` manages agents and dispatch
4. **CAIR Pipeline**: Implements iterative refinement workflow

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the issue
2. **Reproduction Steps**: Minimal code to reproduce
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Python version, OS, package version
6. **Logs/Errors**: Full error messages and stack traces

## 💡 Feature Requests

For feature requests, please include:

1. **Use Case**: Why this feature is needed
2. **Proposed Solution**: How you envision it working
3. **Alternatives**: Other solutions you've considered
4. **Examples**: Code examples of how it would be used

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or insulting/derogatory comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## ❓ Questions?

- **General Questions**: Open a [Discussion](https://github.com/yourusername/multi-ai-refinement-framework/discussions)
- **Bug Reports**: Open an [Issue](https://github.com/yourusername/multi-ai-refinement-framework/issues)
- **Feature Requests**: Open an [Issue](https://github.com/yourusername/multi-ai-refinement-framework/issues) with the `enhancement` label

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

---

**Happy Contributing! 🎉**

