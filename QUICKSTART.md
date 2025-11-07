# Quick Start Guide

Get up and running with the Multi-AI Refinement Framework in 5 minutes!

## ⚡ Installation

### Option 1: Install from PyPI (when published)

```bash
pip install ai-refinement-framework[all]
```

### Option 2: Install from Source (Development)

```bash
git clone https://github.com/yourusername/multi-ai-refinement-framework.git
cd multi-ai-refinement-framework
pip install -e ".[dev,all]"
```

## 🔑 Configuration

### 1. Set Up API Keys

Copy the example environment file and add your API keys:

```bash
cp env.example .env
```

Edit `.env` and add your keys:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
```

### 2. Load Environment Variables

The framework automatically loads from `.env` using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()  # Optional - automatically done by most providers
```

## 🚀 Your First AI Agent

### Example 1: Simple Generation

```python
from ai_refinement_framework import AIFramework, Role, ModelTier

# Initialize
framework = AIFramework()

# Configure an agent
framework.configure_agent(
    role=Role.GENERATOR,
    provider="openai",
    model="gpt-4",
    tier=ModelTier.PRO
)

# Generate
response = framework.dispatch(
    role=Role.GENERATOR,
    prompt="Write a Python function to reverse a string"
)

print(response)
```

### Example 2: Multi-Agent Review System

```python
from ai_refinement_framework import AIFramework, Role, ModelTier

framework = AIFramework()

# Configure generator (OpenAI)
framework.configure_agent(
    role=Role.GENERATOR,
    provider="openai",
    model="gpt-4",
    tier=ModelTier.PRO
)

# Configure reviewer (Anthropic)
framework.configure_agent(
    role=Role.REVIEWER,
    provider="anthropic",
    model="claude-3-sonnet",
    tier=ModelTier.PRO
)

# Generate code
code = framework.dispatch(
    role=Role.GENERATOR,
    prompt="Create a FastAPI endpoint for user registration"
)

# Review the code
review = framework.dispatch(
    role=Role.REVIEWER,
    prompt=f"Review this code for security and best practices:\n\n{code}"
)

print("Generated Code:", code)
print("Review:", review)
```

### Example 3: CAIR Refinement Pipeline

```python
from ai_refinement_framework import CAIRPipeline, Role

# Create pipeline
pipeline = CAIRPipeline(
    max_iterations=3,
    quality_threshold=0.9
)

# Configure all roles
for role in [Role.GENERATOR, Role.REVIEWER, Role.REFINER, Role.QA_ANALYST]:
    pipeline.framework.configure_agent(
        role=role,
        provider="openai",
        model="gpt-4"
    )

# Execute refinement
result = pipeline.execute(
    initial_prompt="Create a secure password hashing function",
    context={
        "language": "Python",
        "requirements": ["bcrypt", "salt", "error handling"]
    }
)

print(f"Final Output:\n{result.final_output}")
print(f"\nQuality Score: {result.quality_score:.2%}")
print(f"Iterations: {result.iterations}")
```

## 💡 Common Patterns

### Pattern 1: Cost Optimization with Model Tiers

```python
# Use PRO for complex tasks
framework.configure_agent(
    role=Role.GENERATOR,
    provider="openai",
    model="gpt-4",
    tier=ModelTier.PRO
)

# Use FLASH for simple validations
framework.configure_agent(
    role=Role.QA_ANALYST,
    provider="openai",
    model="gpt-3.5-turbo",
    tier=ModelTier.FLASH
)
```

### Pattern 2: Provider Mixing

```python
# Best for generation
framework.configure_agent(
    role=Role.GENERATOR,
    provider="openai",
    model="gpt-4"
)

# Best for analysis
framework.configure_agent(
    role=Role.REVIEWER,
    provider="anthropic",
    model="claude-3-opus"
)

# Fast for QA
framework.configure_agent(
    role=Role.QA_ANALYST,
    provider="google",
    model="gemini-pro"
)
```

### Pattern 3: Custom Prompts from Files

```python
framework = AIFramework()

# Load prompts
framework.load_prompt("code_review", "prompts/code_review.txt")
framework.load_prompt("optimization", "prompts/optimize.txt")

# Use loaded prompts
review_prompt = framework.get_prompt("code_review")
response = framework.dispatch(
    role=Role.REVIEWER,
    prompt=review_prompt.format(code=user_code)
)
```

## 📁 Project Structure

```
your-project/
├── .env                    # Your API keys (not in git)
├── prompts/               # Your custom prompts
│   ├── generate.txt
│   ├── review.txt
│   └── refine.txt
└── main.py               # Your application code
```

## 🔍 Testing Your Setup

Run the example script to verify everything works:

```bash
cd examples
python basic_usage.py
```

## 🎯 Next Steps

1. **Read the Full Documentation**: Check [README.md](README.md) for detailed information
2. **Explore Examples**: Look in the `examples/` directory for more patterns
3. **Customize**: Create your own prompts and workflows
4. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute back

## ⚠️ Troubleshooting

### Issue: Module Not Found

```bash
# Make sure you're in the right environment
pip list | grep ai-refinement-framework

# Reinstall if needed
pip install -e ".[all]"
```

### Issue: API Key Errors

```python
import os
print(os.getenv("OPENAI_API_KEY"))  # Should not be None

# Make sure .env is in the right location
# Or set manually:
os.environ["OPENAI_API_KEY"] = "your-key"
```

### Issue: Import Errors

```python
# Check Python version (requires 3.9+)
import sys
print(sys.version)

# Update pip and reinstall
pip install --upgrade pip
pip install -e ".[all]"
```

## 📚 Additional Resources

- **Full Documentation**: [README.md](README.md)
- **API Reference**: Coming soon
- **Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **Examples**: [examples/](examples/)

## 💬 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/multi-ai-refinement-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/multi-ai-refinement-framework/discussions)

---

**Happy Building! 🚀**

