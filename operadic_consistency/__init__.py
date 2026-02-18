"""
Operadic Consistency

A framework for evaluating reasoning consistency via Trees of Questions (ToQs)
and operadic partial collapses.
"""

__version__ = "0.1.0"

# Public API surface

from .core.toq_types import ToQ, ToQNode
from .core.transforms import OpenToQ
from .core.interfaces import (
    Answer,
    Answerer,
    Collapser,
    QuestionDecomposer,
    Normalizer,
)
from .core.consistency import (
    run_consistency_check,
    run_consistency_check_from_question,
)

__all__ = [
    "__version__",
    # Data structures
    "ToQ",
    "ToQNode",
    "OpenToQ",
    # Interfaces
    "Answer",
    "Answerer",
    "Collapser",
    "QuestionDecomposer",
    "Normalizer",
    # Entrypoints
    "run_consistency_check",
    "run_consistency_check_from_question",
]