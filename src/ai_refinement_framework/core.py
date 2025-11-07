"""
Core data structures and enums for the AI Refinement Framework.

This module contains the fundamental building blocks used throughout the framework:
- Role definitions for agent specialization
- Model tier classifications
- Result objects for pipeline outputs
"""

from enum import Enum
from typing import Any, Dict, Optional


class Role(str, Enum):
    """
    Roles that AI agents can fulfill in the framework.
    
    Each role represents a specific function in the agentic workflow:
    - GENERATOR: Creates initial content or solutions
    - REVIEWER: Provides critical analysis and feedback
    - REFINER: Improves content based on feedback
    - QA_ANALYST: Validates quality and correctness
    - ORCHESTRATOR: Coordinates multi-agent workflows
    """
    GENERATOR = "generator"
    REVIEWER = "reviewer"
    REFINER = "refiner"
    QA_ANALYST = "qa_analyst"
    ORCHESTRATOR = "orchestrator"


class ModelTier(str, Enum):
    """
    Model performance tiers for cost/quality optimization.
    
    - PRO: High-capability models for complex, critical tasks
    - FLASH: Fast, cost-effective models for simpler tasks
    """
    PRO = "pro"
    FLASH = "flash"


class RefinementResult:
    """
    Result object from a CAIR refinement pipeline execution.
    
    Attributes:
        final_output: The final refined output
        quality_score: Quality assessment score (0.0 to 1.0)
        iterations: Number of refinement iterations performed
        history: List of intermediate outputs from each iteration
        metadata: Additional metadata about the refinement process
    """
    
    def __init__(
        self,
        final_output: str,
        quality_score: float,
        iterations: int,
        history: list[str],
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        self.final_output = final_output
        self.quality_score = quality_score
        self.iterations = iterations
        self.history = history
        self.metadata = metadata or {}
    
    def __repr__(self) -> str:
        return (
            f"RefinementResult(quality_score={self.quality_score:.2f}, "
            f"iterations={self.iterations})"
        )

