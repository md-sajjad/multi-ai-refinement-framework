# Multi-AI Refinement Framework

**An Extensible, Multi-Provider AI Framework for Building Agentic Workflows**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

This library provides the core architecture for building robust, production-ready AI applications that are decoupled from any single provider.

## 🚀 Core Features

- **Multi-Provider Abstraction**: Write your logic once and run it on Gemini, OpenAI, Anthropic, or local models using a single dispatch call.

- **Role-Based Agentic Design**: Define abstract roles for your AI agents (e.g., GENERATOR, REVIEWER, QA_ANALYST) and assign them to different models or providers.

- **Configurable Model Tiers**: Easily switch between high-performance (PRO) and low-cost (FLASH) models for different tasks to optimize cost and quality.

- **Bring-Your-Own-Prompts (BYOP)**: This framework provides the engine. You provide your proprietary logic and "secret sauce" as simple text files.

- **Proven Refinement Workflow**: Includes a generic 6-phase iterative refinement process (CAIR) for taking a draft AI output to a production-quality final product.

## 📦 Installation

### Basic Installation

```bash
pip install ai-refinement-framework
```

### Install with specific providers

```bash
# Install with OpenAI support
pip install ai-refinement-framework[openai]

# Install with Anthropic support
pip install ai-refinement-framework[anthropic]

# Install with Google Gemini support
pip install ai-refinement-framework[google]

# Install with all providers
pip install ai-refinement-framework[all]
```

### Development Installation

```bash
git clone https://github.com/yourusername/multi-ai-refinement-framework.git
cd multi-ai-refinement-framework
pip install -e ".[dev]"
```

## 🏃 Quick Start

```python
from ai_refinement_framework import AIFramework, Role, ModelTier

# Initialize the framework
framework = AIFramework()

# Define your agents with roles
framework.configure_agent(
    role=Role.GENERATOR,
    provider="openai",
    model="gpt-4",
    tier=ModelTier.PRO
)

framework.configure_agent(
    role=Role.REVIEWER,
    provider="anthropic",
    model="claude-3-sonnet",
    tier=ModelTier.PRO
)

# Use the framework
response = framework.dispatch(
    role=Role.GENERATOR,
    prompt="Write a Python function to calculate fibonacci numbers"
)

print(response)
```

## 🏗️ Architecture Overview

The framework is built around several key concepts:

### 1. **Provider Abstraction**
All AI providers implement a common interface, making it trivial to swap between OpenAI, Anthropic, Google, or custom providers.

### 2. **Role-Based Assignment**
Assign specific roles to different models based on their strengths:
- **GENERATOR**: Creates initial drafts
- **REVIEWER**: Provides critical feedback
- **REFINER**: Improves based on feedback
- **QA_ANALYST**: Validates outputs
- **ORCHESTRATOR**: Coordinates multi-agent workflows

### 3. **Model Tiers**
Optimize costs by using different model tiers:
- **PRO**: High-capability models for complex tasks
- **FLASH**: Fast, cost-effective models for simple tasks

### 4. **Refinement Pipeline**
The built-in CAIR (Continuous AI Refinement) workflow:
1. **Generate**: Create initial output
2. **Review**: Critical analysis
3. **Refine**: Improve based on feedback
4. **Validate**: Quality assurance
5. **Iterate**: Repeat until criteria met
6. **Finalize**: Produce final output

## 📚 Documentation

### Configuration

Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
```

### Advanced Usage

```python
from ai_refinement_framework import CAIRPipeline, Role

# Create a refinement pipeline
pipeline = CAIRPipeline(
    generator_role=Role.GENERATOR,
    reviewer_role=Role.REVIEWER,
    max_iterations=3,
    quality_threshold=0.9
)

# Run the pipeline
result = pipeline.execute(
    initial_prompt="Create a REST API for user management",
    context={"language": "Python", "framework": "FastAPI"}
)

print(result.final_output)
print(f"Quality Score: {result.quality_score}")
print(f"Iterations: {result.iterations}")
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by modern agentic AI architectures
- Built for production use cases
- Designed for extensibility and maintainability

## 📮 Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/multi-ai-refinement-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/multi-ai-refinement-framework/discussions)

## 🗺️ Roadmap

- [ ] Support for streaming responses
- [ ] Built-in token usage tracking and cost estimation
- [ ] More pre-built refinement workflows
- [ ] Integration with LangChain and LlamaIndex
- [ ] Support for local model inference (Ollama, etc.)
- [ ] Web UI for visual workflow design
- [ ] Performance benchmarking tools

---

**Built with ❤️ for the AI community**
