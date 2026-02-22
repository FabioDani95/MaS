"""Shared state between agents."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowState:
    """State container passed across workflow nodes."""

    source_pdf: str | None = None
    selected_pages: list[int] = field(default_factory=list)
    raw_extractions: list[dict[str, Any]] = field(default_factory=list)
    resolved_extractions: list[dict[str, Any]] = field(default_factory=list)
