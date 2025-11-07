"""
Main AI Framework implementation.

This module contains the core AIFramework class that manages agents,
providers, and dispatching of requests to configured AI models.
"""

from typing import Any, Dict, Optional

from .core import Role, ModelTier
from .exceptions import RoleNotConfiguredError, PromptNotFoundError
from .providers import (
    Provider,
    MockProvider,
    OpenAIProvider,
    AnthropicProvider,
    GeminiProvider,
)


class AIFramework:
    """
    Main framework class for managing multi-provider AI interactions.
    
    This class provides:
    - Agent configuration and management
    - Provider abstraction
    - Role-based dispatching
    - Prompt management
    
    Example:
        >>> framework = AIFramework()
        >>> framework.configure_agent(
        ...     role=Role.GENERATOR,
        ...     provider="openai",
        ...     model="gpt-4"
        ... )
        >>> response = framework.dispatch(
        ...     role=Role.GENERATOR,
        ...     prompt="Generate code"
        ... )
    """
    
    def __init__(self) -> None:
        """Initialize the AI Framework."""
        self._agents: Dict[Role, Dict[str, Any]] = {}
        self._providers: Dict[str, Provider] = {}
        self._prompts: Dict[str, str] = {}
    
    def configure_agent(
        self,
        role: Role,
        provider: str,
        model: str,
        tier: ModelTier = ModelTier.PRO,
        temperature: float = 0.7,
        **kwargs: Any
    ) -> None:
        """
        Configure an AI agent for a specific role.
        
        Args:
            role: The role this agent will fulfill
            provider: Provider name (e.g., "openai", "anthropic", "google")
            model: Specific model identifier
            tier: Performance tier (PRO or FLASH)
            temperature: Sampling temperature
            **kwargs: Additional configuration parameters
        """
        self._agents[role] = {
            "provider": provider,
            "model": model,
            "tier": tier,
            "temperature": temperature,
            **kwargs
        }
        
        # Initialize provider if not already done
        if provider not in self._providers:
            self._providers[provider] = self._get_provider(provider)
    
    def dispatch(
        self,
        role: Role,
        prompt: str,
        context: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> str:
        """
        Dispatch a request to the agent configured for the given role.
        
        Args:
            role: The role to dispatch to
            prompt: The prompt to send
            context: Optional context dictionary
            **kwargs: Additional parameters
            
        Returns:
            The agent's response
            
        Raises:
            RoleNotConfiguredError: If no agent is configured for the role
        """
        if role not in self._agents:
            raise RoleNotConfiguredError(role.value)
        
        agent_config = self._agents[role]
        provider_name = agent_config["provider"]
        
        # Get the provider
        provider = self._providers[provider_name]
        
        # For mock provider, use its simple implementation
        if isinstance(provider, MockProvider):
            return provider.generate(
                prompt=prompt,
                model=agent_config["model"],
                temperature=agent_config.get("temperature", 0.7),
                **kwargs
            )
        
        # For real providers, you would call their generate method
        # This is a placeholder for now
        return f"[{role.value}] Response to: {prompt[:50]}..."
    
    def load_prompt(self, name: str, filepath: str) -> None:
        """
        Load a prompt template from a file.
        
        Args:
            name: Name to reference this prompt
            filepath: Path to the prompt file
        """
        with open(filepath, 'r') as f:
            self._prompts[name] = f.read()
    
    def get_prompt(self, name: str) -> str:
        """
        Retrieve a loaded prompt template.
        
        Args:
            name: The prompt name
            
        Returns:
            The prompt template
            
        Raises:
            PromptNotFoundError: If prompt name not found
        """
        if name not in self._prompts:
            raise PromptNotFoundError(name)
        return self._prompts[name]
    
    def _get_provider(self, provider_name: str) -> Provider:
        """
        Get or create a provider instance.
        
        Args:
            provider_name: Name of the provider
            
        Returns:
            Provider instance
        """
        # For now, return mock provider for all
        # In production, this would instantiate the appropriate provider
        if provider_name == "openai":
            try:
                return OpenAIProvider()
            except ImportError:
                return MockProvider()
        elif provider_name == "anthropic":
            try:
                return AnthropicProvider()
            except ImportError:
                return MockProvider()
        elif provider_name == "google" or provider_name == "gemini":
            try:
                return GeminiProvider()
            except ImportError:
                return MockProvider()
        else:
            return MockProvider()

