"""
Basic usage example for the AI Refinement Framework.

This example demonstrates:
1. Initializing the framework
2. Configuring agents with different roles
3. Dispatching requests to agents
4. Using the CAIR refinement pipeline
"""

from ai_refinement_framework import (
    AIFramework,
    Role,
    ModelTier,
    CAIRPipeline,
)


def basic_framework_example() -> None:
    """Demonstrate basic framework usage."""
    print("=" * 60)
    print("Basic Framework Example")
    print("=" * 60)
    
    # Initialize the framework
    framework = AIFramework()
    
    # Configure a generator agent using OpenAI
    framework.configure_agent(
        role=Role.GENERATOR,
        provider="openai",
        model="gpt-4",
        tier=ModelTier.PRO,
        temperature=0.7
    )
    
    # Configure a reviewer agent using Anthropic
    framework.configure_agent(
        role=Role.REVIEWER,
        provider="anthropic",
        model="claude-3-sonnet",
        tier=ModelTier.PRO,
        temperature=0.5
    )
    
    # Configure a QA analyst using a flash model for cost efficiency
    framework.configure_agent(
        role=Role.QA_ANALYST,
        provider="openai",
        model="gpt-3.5-turbo",
        tier=ModelTier.FLASH,
        temperature=0.3
    )
    
    # Dispatch a request to the generator
    print("\n1. Generating initial code...")
    response = framework.dispatch(
        role=Role.GENERATOR,
        prompt="Write a Python function to calculate the nth Fibonacci number",
        context={"language": "Python", "style": "functional"}
    )
    print(f"Response: {response}")
    
    # Get review from the reviewer
    print("\n2. Getting code review...")
    review = framework.dispatch(
        role=Role.REVIEWER,
        prompt=f"Review this code: {response}",
        context={"focus": ["performance", "readability"]}
    )
    print(f"Review: {review}")
    
    print("\n" + "=" * 60)


def cair_pipeline_example() -> None:
    """Demonstrate CAIR refinement pipeline."""
    print("=" * 60)
    print("CAIR Pipeline Example")
    print("=" * 60)
    
    # Create a refinement pipeline
    pipeline = CAIRPipeline(
        generator_role=Role.GENERATOR,
        reviewer_role=Role.REVIEWER,
        refiner_role=Role.REFINER,
        qa_role=Role.QA_ANALYST,
        max_iterations=3,
        quality_threshold=0.9
    )
    
    # Configure the agents
    for role in [Role.GENERATOR, Role.REVIEWER, Role.REFINER, Role.QA_ANALYST]:
        pipeline.framework.configure_agent(
            role=role,
            provider="openai",
            model="gpt-4",
            tier=ModelTier.PRO
        )
    
    # Execute the pipeline
    print("\nExecuting refinement pipeline...")
    result = pipeline.execute(
        initial_prompt="Create a RESTful API endpoint for user registration",
        context={
            "language": "Python",
            "framework": "FastAPI",
            "requirements": [
                "Email validation",
                "Password hashing",
                "Error handling",
                "Input validation"
            ]
        }
    )
    
    # Display results
    print(f"\nFinal Output:\n{result.final_output}")
    print(f"\nQuality Score: {result.quality_score:.2f}")
    print(f"Iterations: {result.iterations}")
    print(f"Number of drafts: {len(result.history)}")
    
    print("\n" + "=" * 60)


def multi_tier_example() -> None:
    """Demonstrate using different model tiers for cost optimization."""
    print("=" * 60)
    print("Multi-Tier Model Example")
    print("=" * 60)
    
    framework = AIFramework()
    
    # Use PRO tier for complex generation
    framework.configure_agent(
        role=Role.GENERATOR,
        provider="openai",
        model="gpt-4",
        tier=ModelTier.PRO,
        temperature=0.8
    )
    
    # Use FLASH tier for simple QA tasks
    framework.configure_agent(
        role=Role.QA_ANALYST,
        provider="openai",
        model="gpt-3.5-turbo",
        tier=ModelTier.FLASH,
        temperature=0.2
    )
    
    print("\nGenerating complex code (PRO tier - GPT-4)...")
    code = framework.dispatch(
        role=Role.GENERATOR,
        prompt="Design a thread-safe caching system with LRU eviction"
    )
    print(f"Generated: {code}")
    
    print("\nValidating output (FLASH tier - GPT-3.5-turbo)...")
    validation = framework.dispatch(
        role=Role.QA_ANALYST,
        prompt=f"Does this code have any syntax errors? {code}"
    )
    print(f"Validation: {validation}")
    
    print("\n" + "=" * 60)


def main() -> None:
    """Run all examples."""
    print("\n🚀 AI Refinement Framework Examples\n")
    
    # Run examples
    basic_framework_example()
    print("\n")
    
    cair_pipeline_example()
    print("\n")
    
    multi_tier_example()
    
    print("\n✅ All examples completed!\n")
    print("Note: These are mock responses. To use with real AI providers,")
    print("you'll need to implement provider integrations and set API keys.\n")


if __name__ == "__main__":
    main()

