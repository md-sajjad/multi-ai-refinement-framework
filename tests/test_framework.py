"""
Unit tests for the AI Refinement Framework core functionality.
"""

import pytest
from ai_refinement_framework import (
    AIFramework,
    Role,
    ModelTier,
    CAIRPipeline,
    RefinementResult,
    RoleNotConfiguredError,
    PromptNotFoundError,
)


class TestRole:
    """Tests for the Role enum."""
    
    def test_role_values(self) -> None:
        """Test that all expected roles are defined."""
        assert Role.GENERATOR.value == "generator"
        assert Role.REVIEWER.value == "reviewer"
        assert Role.REFINER.value == "refiner"
        assert Role.QA_ANALYST.value == "qa_analyst"
        assert Role.ORCHESTRATOR.value == "orchestrator"


class TestModelTier:
    """Tests for the ModelTier enum."""
    
    def test_tier_values(self) -> None:
        """Test that model tiers are correctly defined."""
        assert ModelTier.PRO.value == "pro"
        assert ModelTier.FLASH.value == "flash"


class TestAIFramework:
    """Tests for the AIFramework class."""
    
    def test_framework_initialization(self) -> None:
        """Test that framework initializes correctly."""
        framework = AIFramework()
        assert framework is not None
        assert isinstance(framework._agents, dict)
        assert isinstance(framework._providers, dict)
        assert isinstance(framework._prompts, dict)
    
    def test_configure_agent(self) -> None:
        """Test agent configuration."""
        framework = AIFramework()
        framework.configure_agent(
            role=Role.GENERATOR,
            provider="openai",
            model="gpt-4",
            tier=ModelTier.PRO,
            temperature=0.8
        )
        
        assert Role.GENERATOR in framework._agents
        agent_config = framework._agents[Role.GENERATOR]
        assert agent_config["provider"] == "openai"
        assert agent_config["model"] == "gpt-4"
        assert agent_config["tier"] == ModelTier.PRO
        assert agent_config["temperature"] == 0.8
    
    def test_dispatch_without_agent_raises_error(self) -> None:
        """Test that dispatching to unconfigured role raises RoleNotConfiguredError."""
        framework = AIFramework()
        
        with pytest.raises(RoleNotConfiguredError, match="No agent configured for role"):
            framework.dispatch(
                role=Role.GENERATOR,
                prompt="Test prompt"
            )
    
    def test_dispatch_with_configured_agent(self) -> None:
        """Test dispatching to a configured agent."""
        framework = AIFramework()
        framework.configure_agent(
            role=Role.GENERATOR,
            provider="openai",
            model="gpt-4"
        )
        
        response = framework.dispatch(
            role=Role.GENERATOR,
            prompt="Test prompt"
        )
        
        assert isinstance(response, str)
        assert "generator" in response.lower()
    
    def test_prompt_management(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        """Test loading and retrieving prompts."""
        framework = AIFramework()
        
        # Create a temporary prompt file
        prompt_file = tmp_path / "test_prompt.txt"
        prompt_content = "This is a test prompt with {placeholder}"
        prompt_file.write_text(prompt_content)
        
        # Load the prompt
        framework.load_prompt("test", str(prompt_file))
        
        # Retrieve the prompt
        loaded_prompt = framework.get_prompt("test")
        assert loaded_prompt == prompt_content
    
    def test_get_nonexistent_prompt_raises_error(self) -> None:
        """Test that getting a nonexistent prompt raises PromptNotFoundError."""
        framework = AIFramework()
        
        with pytest.raises(PromptNotFoundError):
            framework.get_prompt("nonexistent")


class TestRefinementResult:
    """Tests for the RefinementResult class."""
    
    def test_result_initialization(self) -> None:
        """Test RefinementResult initialization."""
        result = RefinementResult(
            final_output="Final output",
            quality_score=0.95,
            iterations=3,
            history=["Draft 1", "Draft 2", "Final output"],
            metadata={"test": "value"}
        )
        
        assert result.final_output == "Final output"
        assert result.quality_score == 0.95
        assert result.iterations == 3
        assert len(result.history) == 3
        assert result.metadata["test"] == "value"
    
    def test_result_repr(self) -> None:
        """Test RefinementResult string representation."""
        result = RefinementResult(
            final_output="Test",
            quality_score=0.88,
            iterations=2,
            history=["Draft 1", "Test"]
        )
        
        repr_str = repr(result)
        assert "0.88" in repr_str
        assert "iterations=2" in repr_str


class TestCAIRPipeline:
    """Tests for the CAIR Pipeline."""
    
    def test_pipeline_initialization(self) -> None:
        """Test pipeline initialization with default values."""
        pipeline = CAIRPipeline()
        
        assert pipeline.generator_role == Role.GENERATOR
        assert pipeline.reviewer_role == Role.REVIEWER
        assert pipeline.refiner_role == Role.REFINER
        assert pipeline.qa_role == Role.QA_ANALYST
        assert pipeline.max_iterations == 3
        assert pipeline.quality_threshold == 0.85
    
    def test_pipeline_custom_configuration(self) -> None:
        """Test pipeline with custom configuration."""
        pipeline = CAIRPipeline(
            generator_role=Role.ORCHESTRATOR,
            reviewer_role=Role.QA_ANALYST,
            max_iterations=5,
            quality_threshold=0.95
        )
        
        assert pipeline.generator_role == Role.ORCHESTRATOR
        assert pipeline.reviewer_role == Role.QA_ANALYST
        assert pipeline.max_iterations == 5
        assert pipeline.quality_threshold == 0.95
    
    def test_pipeline_execution(self) -> None:
        """Test executing the refinement pipeline."""
        pipeline = CAIRPipeline(max_iterations=2)
        
        # Configure the framework agents
        pipeline.framework.configure_agent(
            role=Role.GENERATOR,
            provider="test",
            model="test-model"
        )
        pipeline.framework.configure_agent(
            role=Role.REVIEWER,
            provider="test",
            model="test-model"
        )
        pipeline.framework.configure_agent(
            role=Role.REFINER,
            provider="test",
            model="test-model"
        )
        
        result = pipeline.execute(
            initial_prompt="Test prompt",
            context={"key": "value"}
        )
        
        assert isinstance(result, RefinementResult)
        assert result.final_output is not None
        assert result.quality_score >= 0.0
        assert result.iterations > 0
        assert len(result.history) > 0
        assert result.metadata["initial_prompt"] == "Test prompt"
        assert result.metadata["context"]["key"] == "value"


class TestVersioning:
    """Tests for version information."""
    
    def test_version_import(self) -> None:
        """Test that version can be imported."""
        from ai_refinement_framework import __version__, get_version
        
        assert isinstance(__version__, str)
        assert get_version() == __version__

