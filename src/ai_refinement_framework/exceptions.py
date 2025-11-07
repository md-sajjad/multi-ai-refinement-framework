"""
Custom exceptions for the AI Refinement Framework.

This module defines all framework-specific exceptions to enable
precise error handling and meaningful error messages.
"""


class AIFrameworkError(Exception):
    """Base exception for all AI Refinement Framework errors."""
    pass


class ConfigurationError(AIFrameworkError):
    """Raised when there is an error in framework or agent configuration."""
    pass


class ProviderError(AIFrameworkError):
    """Raised when there is an error with an AI provider."""
    pass


class RoleNotConfiguredError(ConfigurationError):
    """Raised when attempting to use a role that hasn't been configured."""
    
    def __init__(self, role: str) -> None:
        super().__init__(f"No agent configured for role: {role}")
        self.role = role


class PromptNotFoundError(AIFrameworkError):
    """Raised when attempting to retrieve a prompt that doesn't exist."""
    
    def __init__(self, prompt_name: str) -> None:
        super().__init__(f"Prompt not found: {prompt_name}")
        self.prompt_name = prompt_name


class ModelNotFoundError(ProviderError):
    """Raised when a specified model is not available."""
    
    def __init__(self, model: str, provider: str) -> None:
        super().__init__(f"Model '{model}' not found for provider '{provider}'")
        self.model = model
        self.provider = provider

