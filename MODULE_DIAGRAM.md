# Module Architecture Diagram

## Package Structure Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                    ai_refinement_framework                         │
│                         (Package Root)                             │
└────────────────────────────────────────────────────────────────────┘
                                 │
                                 │ imports
                                 ▼
┌────────────────────────────────────────────────────────────────────┐
│                        __init__.py                                 │
│                  (Public API Exports - 89 lines)                   │
│                                                                    │
│  • Version metadata (__version__, __author__, __license__)         │
│  • Public API exports (__all__)                                    │
│  • Import statements from submodules                               │
│  • get_version() helper function                                   │
└────────────────────────────────────────────────────────────────────┘
                                 │
                                 │ imports from
                                 ▼
        ┌────────────────────────┴────────────────────────┐
        │                                                  │
        ▼                                                  ▼
┌──────────────────┐                              ┌──────────────────┐
│    core.py       │◄─────────────┐               │  exceptions.py   │
│   (76 lines)     │              │               │   (43 lines)     │
│                  │              │               │                  │
│ • Role enum      │              │               │ • AIFrameworkError│
│ • ModelTier enum │              │               │ • ConfigurationError│
│ • RefinementResult│             │               │ • ProviderError   │
└──────────────────┘              │               │ • RoleNotConfiguredError│
        ▲                         │               │ • PromptNotFoundError│
        │                         │               │ • ModelNotFoundError│
        │                         │               └──────────────────┘
        │                         │                        ▲
        │                         │                        │
        │                         │                        │
┌──────────────────┐              │               ┌──────────────────┐
│  providers.py    │              │               │  framework.py    │
│  (289 lines)     │              │               │  (164 lines)     │
│                  │              │               │                  │
│ • Provider protocol│            │               │ • AIFramework    │
│ • MockProvider    │             └───────────────┤   - configure_agent()│
│ • OpenAIProvider  │                             │   - dispatch()   │
│ • AnthropicProvider│                            │   - load_prompt()│
│ • GeminiProvider  │                             │   - get_prompt() │
└──────────────────┘                              │   - _get_provider()│
        ▲                                         └──────────────────┘
        │                                                  ▲
        │                                                  │
        │                                                  │
        │                                         ┌──────────────────┐
        │                                         │   pipeline.py    │
        │                                         │   (116 lines)    │
        │                                         │                  │
        └─────────────────────────────────────────┤ • CAIRPipeline   │
                                                  │   - execute()    │
                                                  │   - Uses AIFramework│
                                                  └──────────────────┘
                                                          ▲
                                                          │
                                                          │
                                                  ┌──────────────────┐
                                                  │     cost.py      │
                                                  │   (143 lines)    │
                                                  │                  │
                                                  │ • MODEL_COSTS dict│
                                                  │ • CostTracker    │
                                                  │   - add_call()   │
                                                  │   - estimate_cost()│
                                                  │   - get_summary()│
                                                  │   - reset()      │
                                                  └──────────────────┘
```

## Module Dependency Graph

```
         core.py (no dependencies)
            ↓
    ┌───────┴───────┬───────────────┐
    ↓               ↓               ↓
exceptions.py   providers.py    framework.py
    ↓               ↓               ↓
    └───────────────┴───────────────┴─→ pipeline.py
                                        
                                        cost.py (independent)
```

## Import Relationships

### Internal Package Imports (Relative)

```python
# providers.py
from abc import abstractmethod
from typing import Any, Optional, Protocol

# framework.py
from .core import Role, ModelTier
from .exceptions import RoleNotConfiguredError, PromptNotFoundError
from .providers import Provider, MockProvider, OpenAIProvider, ...

# pipeline.py
from .core import Role, RefinementResult
from .framework import AIFramework

# cost.py
from typing import Dict, Optional
# (independent module)
```

### User-Facing Imports (Absolute)

```python
# Users import from the package root
from ai_refinement_framework import (
    AIFramework,        # from framework.py
    Role,               # from core.py
    ModelTier,          # from core.py
    CAIRPipeline,       # from pipeline.py
    CostTracker,        # from cost.py
    RoleNotConfiguredError,  # from exceptions.py
)
```

## Data Flow Example

### Configuration Flow
```
User Code
    │
    ▼
AIFramework.configure_agent()
    │
    ├─→ Validates Role (from core.py)
    ├─→ Validates ModelTier (from core.py)
    └─→ Creates Provider (from providers.py)
```

### Dispatch Flow
```
User Code
    │
    ▼
AIFramework.dispatch()
    │
    ├─→ Check if Role configured
    │   └─→ Raise RoleNotConfiguredError (from exceptions.py)
    │
    ├─→ Get Provider (from providers.py)
    │   └─→ MockProvider / OpenAIProvider / etc.
    │
    └─→ Call Provider.generate()
        └─→ Return response
```

### Pipeline Flow
```
User Code
    │
    ▼
CAIRPipeline.execute()
    │
    ├─→ Uses AIFramework (from framework.py)
    │   └─→ Dispatch to Role.GENERATOR
    │
    ├─→ Iterative refinement loop
    │   ├─→ Dispatch to Role.REVIEWER
    │   └─→ Dispatch to Role.REFINER
    │
    └─→ Return RefinementResult (from core.py)
```

### Cost Tracking Flow
```
User Code
    │
    ▼
CostTracker.add_call()
    │
    ├─→ Lookup MODEL_COSTS (from cost.py)
    ├─→ Calculate costs
    └─→ Update totals and history
```

## Module Responsibilities

| Module | Responsibility | Dependencies | Exported Items |
|--------|---------------|--------------|----------------|
| `core.py` | Fundamental types | None | Role, ModelTier, RefinementResult |
| `exceptions.py` | Error types | None | 6 exception classes |
| `providers.py` | AI provider implementations | None | Provider protocol + 4 implementations |
| `framework.py` | Main orchestration | core, exceptions, providers | AIFramework |
| `pipeline.py` | Refinement workflow | core, framework | CAIRPipeline |
| `cost.py` | Cost tracking | typing only | CostTracker, MODEL_COSTS |

## Module Sizes

```
┌────────────────┬───────┬────────────────────────────┐
│ Module         │ Lines │ Visual                     │
├────────────────┼───────┼────────────────────────────┤
│ providers.py   │  289  │ ████████████████████████   │
│ framework.py   │  164  │ █████████████              │
│ cost.py        │  143  │ ███████████                │
│ pipeline.py    │  116  │ █████████                  │
│ __init__.py    │   89  │ ███████                    │
│ core.py        │   76  │ ██████                     │
│ exceptions.py  │   43  │ ███                        │
├────────────────┼───────┼────────────────────────────┤
│ TOTAL          │  920  │                            │
└────────────────┴───────┴────────────────────────────┘
```

## Key Design Principles

### 1. Separation of Concerns
Each module has a single, clear responsibility:
- **core**: Data structures
- **exceptions**: Error handling
- **providers**: External integrations
- **framework**: Business logic
- **pipeline**: Workflows
- **cost**: Tracking/analytics

### 2. Minimal Dependencies
Modules depend only on what they need:
- `core.py` has zero dependencies
- `exceptions.py` has zero dependencies
- `providers.py` has zero internal dependencies
- Only `framework.py` and `pipeline.py` have multiple internal deps

### 3. Clear API Surface
Users only need to know the top-level package:
```python
from ai_refinement_framework import *  # Everything they need
```

### 4. Extensibility
Easy to add new features:
- New provider? Add to `providers.py`
- New pipeline? Add new file `pipeline_advanced.py`
- New exception? Add to `exceptions.py`
- New cost model? Update `cost.py`

### 5. Testability
Each module can be tested independently:
```python
# Test core types
from ai_refinement_framework.core import Role

# Test exceptions
from ai_refinement_framework.exceptions import RoleNotConfiguredError

# Test providers in isolation
from ai_refinement_framework.providers import MockProvider
```

## Physical File Structure

```
src/ai_refinement_framework/
│
├── __init__.py          ← Public API (users start here)
│   └── Imports from all modules below
│
├── core.py              ← Foundation (no dependencies)
│   └── Role, ModelTier, RefinementResult
│
├── exceptions.py        ← Errors (no dependencies)
│   └── Custom exception hierarchy
│
├── providers.py         ← External integrations (no internal deps)
│   └── Provider implementations
│
├── framework.py         ← Main logic (uses core, exceptions, providers)
│   └── AIFramework class
│
├── pipeline.py          ← Workflows (uses core, framework)
│   └── CAIRPipeline class
│
├── cost.py              ← Analytics (independent)
│   └── CostTracker, MODEL_COSTS
│
└── py.typed             ← Type hints marker
```

## Summary

The refactored architecture provides:

✅ **Clear separation** - Each module has one job  
✅ **Minimal coupling** - Modules depend only on what they need  
✅ **Maximum cohesion** - Related code stays together  
✅ **Easy navigation** - Intuitive file names and structure  
✅ **Simple testing** - Test each module independently  
✅ **Flexible extension** - Add features without breaking existing code  

This is a **professional, maintainable, and scalable** package structure that follows Python best practices and industry standards.

