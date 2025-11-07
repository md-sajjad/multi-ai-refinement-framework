# An Extensible, Multi-Provider AI Framework for Building Agentic Workflows"

This library provides the core architecture for building robust, production-ready AI applications that are decoupled from any single provider.

# Core Features:

- Multi-Provider Abstraction: Write your logic once and run it on Gemini, OpenAI, Anthropic, or local models using a single dispatch call.

- Role-Based Agentic Design: Define abstract roles for your AI agents (e.g., GENERATOR, REVIEWER, QA_ANALYST) and assign them to different models or providers.

- Configurable Model Tiers: Easily switch between high-performance (PRO) and low-cost (FLASH) models for different tasks to optimize cost and quality.

- Bring-Your-Own-Prompts (BYOP): This framework provides the engine. You provide your proprietary logic and "secret sauce" as simple text files.

- Proven Refinement Workflow: Includes a generic 6-phase iterative refinement process (CAIR) for taking a draft AI output to a production-quality final product.
