"""
AI provider implementations and abstractions.

This module contains the Provider protocol and concrete implementations
for various AI providers (OpenAI, Anthropic, Google, etc.).
"""

from abc import abstractmethod
from typing import Any, Optional, Protocol


class Provider(Protocol):
    """
    Protocol defining the interface that all AI providers must implement.
    
    This ensures consistent behavior across OpenAI, Anthropic, Google, 
    and custom providers.
    """
    
    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """
        Generate a response from the AI model.
        
        Args:
            prompt: The input prompt
            model: The specific model to use
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional provider-specific parameters
            
        Returns:
            The generated text response
        """
        ...
    
    def get_available_models(self) -> list[str]:
        """
        Get list of available models for this provider.
        
        Returns:
            List of model identifiers
        """
        ...


class MockProvider:
    """
    Mock provider for testing and development.
    
    Returns placeholder responses without calling any actual AI service.
    Useful for testing the framework structure without API keys.
    """
    
    def __init__(self) -> None:
        """Initialize the mock provider."""
        self.call_count = 0
    
    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """
        Generate a mock response.
        
        Args:
            prompt: The input prompt
            model: The model name (ignored in mock)
            temperature: Temperature parameter (ignored in mock)
            max_tokens: Max tokens (ignored in mock)
            **kwargs: Additional parameters (ignored in mock)
            
        Returns:
            A mock response string
        """
        self.call_count += 1
        return f"[Mock {model}] Response to: {prompt[:50]}..."
    
    def get_available_models(self) -> list[str]:
        """
        Get list of mock models.
        
        Returns:
            List of mock model identifiers
        """
        return ["mock-gpt-4", "mock-claude-3", "mock-gemini-pro"]


class OpenAIProvider:
    """
    OpenAI provider implementation.
    
    Requires the 'openai' package and OPENAI_API_KEY environment variable.
    """
    
    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize OpenAI provider.
        
        Args:
            api_key: Optional API key. If not provided, reads from environment.
        """
        try:
            import openai
            self.client = openai.OpenAI(api_key=api_key)
        except ImportError:
            raise ImportError(
                "OpenAI provider requires 'openai' package. "
                "Install with: pip install openai"
            )
    
    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """
        Generate a response using OpenAI's API.
        
        Args:
            prompt: The input prompt
            model: The OpenAI model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional OpenAI-specific parameters
            
        Returns:
            The generated text response
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return response.choices[0].message.content or ""
    
    def get_available_models(self) -> list[str]:
        """
        Get list of available OpenAI models.
        
        Returns:
            List of OpenAI model identifiers
        """
        return ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", "gpt-4o"]


class AnthropicProvider:
    """
    Anthropic (Claude) provider implementation.
    
    Requires the 'anthropic' package and ANTHROPIC_API_KEY environment variable.
    """
    
    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize Anthropic provider.
        
        Args:
            api_key: Optional API key. If not provided, reads from environment.
        """
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
        except ImportError:
            raise ImportError(
                "Anthropic provider requires 'anthropic' package. "
                "Install with: pip install anthropic"
            )
    
    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """
        Generate a response using Anthropic's API.
        
        Args:
            prompt: The input prompt
            model: The Anthropic model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional Anthropic-specific parameters
            
        Returns:
            The generated text response
        """
        message = self.client.messages.create(
            model=model,
            max_tokens=max_tokens or 1024,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return message.content[0].text
    
    def get_available_models(self) -> list[str]:
        """
        Get list of available Anthropic models.
        
        Returns:
            List of Anthropic model identifiers
        """
        return [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-3-5-sonnet-20240620",
        ]


class GeminiProvider:
    """
    Google Gemini provider implementation.
    
    Requires the 'google-generativeai' package and GOOGLE_API_KEY environment variable.
    """
    
    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize Gemini provider.
        
        Args:
            api_key: Optional API key. If not provided, reads from environment.
        """
        try:
            import google.generativeai as genai
            if api_key:
                genai.configure(api_key=api_key)
            self.genai = genai
        except ImportError:
            raise ImportError(
                "Gemini provider requires 'google-generativeai' package. "
                "Install with: pip install google-generativeai"
            )
    
    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> str:
        """
        Generate a response using Google's Gemini API.
        
        Args:
            prompt: The input prompt
            model: The Gemini model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional Gemini-specific parameters
            
        Returns:
            The generated text response
        """
        generation_config = {
            "temperature": temperature,
        }
        if max_tokens:
            generation_config["max_output_tokens"] = max_tokens
        
        model_instance = self.genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config
        )
        response = model_instance.generate_content(prompt)
        return response.text
    
    def get_available_models(self) -> list[str]:
        """
        Get list of available Gemini models.
        
        Returns:
            List of Gemini model identifiers
        """
        return ["gemini-pro", "gemini-pro-vision", "gemini-1.5-pro", "gemini-1.5-flash"]

