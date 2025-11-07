"""
Cost tracking and estimation for AI model usage.

This module provides utilities for tracking token usage and estimating
costs across different AI providers and models.
"""

from typing import Dict, Optional


# Model costs in USD per 1K tokens (input, output)
MODEL_COSTS: Dict[str, Dict[str, float]] = {
    # OpenAI Models
    "gpt-4": {
        "input": 0.03,
        "output": 0.06,
    },
    "gpt-4-turbo": {
        "input": 0.01,
        "output": 0.03,
    },
    "gpt-4o": {
        "input": 0.005,
        "output": 0.015,
    },
    "gpt-3.5-turbo": {
        "input": 0.0005,
        "output": 0.0015,
    },
    
    # Anthropic Models
    "claude-3-opus-20240229": {
        "input": 0.015,
        "output": 0.075,
    },
    "claude-3-sonnet-20240229": {
        "input": 0.003,
        "output": 0.015,
    },
    "claude-3-5-sonnet-20240620": {
        "input": 0.003,
        "output": 0.015,
    },
    "claude-3-haiku-20240307": {
        "input": 0.00025,
        "output": 0.00125,
    },
    
    # Google Gemini Models
    "gemini-pro": {
        "input": 0.00025,
        "output": 0.0005,
    },
    "gemini-1.5-pro": {
        "input": 0.0035,
        "output": 0.0105,
    },
    "gemini-1.5-flash": {
        "input": 0.00035,
        "output": 0.00105,
    },
}


class CostTracker:
    """
    Track costs across multiple AI model invocations.
    
    This class helps monitor spending by tracking token usage
    and calculating costs based on model pricing.
    """
    
    def __init__(self) -> None:
        """Initialize the cost tracker."""
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0
        self.call_history: list[Dict[str, any]] = []
    
    def add_call(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cost: Optional[float] = None
    ) -> None:
        """
        Record a model API call.
        
        Args:
            model: The model identifier
            input_tokens: Number of input tokens used
            output_tokens: Number of output tokens generated
            cost: Optionally provide the exact cost, otherwise it's calculated
        """
        if cost is None:
            cost = self.estimate_cost(model, input_tokens, output_tokens)
        
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += cost
        
        self.call_history.append({
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost,
        })
    
    def estimate_cost(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:
        """
        Estimate the cost of a model call.
        
        Args:
            model: The model identifier
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            
        Returns:
            Estimated cost in USD
        """
        if model not in MODEL_COSTS:
            return 0.0
        
        pricing = MODEL_COSTS[model]
        input_cost = (input_tokens / 1000) * pricing["input"]
        output_cost = (output_tokens / 1000) * pricing["output"]
        
        return input_cost + output_cost
    
    def get_summary(self) -> Dict[str, any]:
        """
        Get a summary of all tracked costs.
        
        Returns:
            Dictionary with cost summary information
        """
        return {
            "total_calls": len(self.call_history),
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "total_cost_usd": self.total_cost,
        }
    
    def reset(self) -> None:
        """Reset all tracked costs and history."""
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0
        self.call_history = []

