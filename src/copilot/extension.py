from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any


class CopilotInvokeRequest(BaseModel):
    conversation_id: str
    message: str
    context: dict[str, Any] = Field(default_factory=dict)


class CopilotInvokeResponse(BaseModel):
    conversation_id: str
    reply: str
    citations: list[str] = Field(default_factory=list)


def handle_copilot_invoke(req: CopilotInvokeRequest) -> CopilotInvokeResponse:
    return CopilotInvokeResponse(
        conversation_id=req.conversation_id,
        reply=f"Copilot extension stub received: {req.message}",
        citations=[],
    )
