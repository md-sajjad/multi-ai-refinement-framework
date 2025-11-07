"""
Multi-AI Refinement Framework
==============================

An extensible, multi-provider AI framework for building agentic workflows.

This framework provides:
- Multi-provider abstraction (OpenAI, Anthropic, Google Gemini, etc.)
- Role-based agentic design
- Configurable model tiers (PRO/FLASH)
- BYOP (Bring Your Own Prompts) architecture
- Built-in CAIR (Continuous AI Refinement) workflow

Example:
    >>> from ai_refinement_framework import AIFramework, Role, ModelTier
    >>> framework = AIFramework()
    >>> framework.configure_agent(
    ...     role=Role.GENERATOR,
    ...     provider="openai",
    ...     model="gpt-4",
    ...     tier=ModelTier.PRO
    ... )
    >>> response = framework.dispatch(
    ...     role=Role.GENERATOR,
    ...     prompt="Write a hello world function"
    ... )

License:
    Apache License 2.0
"""

# Version and metadata
__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "Apache-2.0"

# Import public API from submodules
from .core import Role, ModelTier, RefinementResult
from .exceptions import (
    AIFrameworkError,
    ConfigurationError,
    ProviderError,
    RoleNotConfiguredError,
    PromptNotFoundError,
    ModelNotFoundError,
)
from .providers import (
    Provider,
    MockProvider,
    OpenAIProvider,
    AnthropicProvider,
    GeminiProvider,
)
from .framework import AIFramework
from .pipeline import CAIRPipeline
from .cost import CostTracker, MODEL_COSTS

# Define public API
__all__ = [
    # Core classes and enums
    "AIFramework",
    "Role",
    "ModelTier",
    "RefinementResult",
    
    # Pipeline
    "CAIRPipeline",
    
    # Providers
    "Provider",
    "MockProvider",
    "OpenAIProvider",
    "AnthropicProvider",
    "GeminiProvider",
    
    # Exceptions
    "AIFrameworkError",
    "ConfigurationError",
    "ProviderError",
    "RoleNotConfiguredError",
    "PromptNotFoundError",
    "ModelNotFoundError",
    
    # Cost tracking
    "CostTracker",
    "MODEL_COSTS",
]


def get_version() -> str:
    """Return the current version of the framework."""
    return __version__
