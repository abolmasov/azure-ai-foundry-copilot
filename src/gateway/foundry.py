from __future__ import annotations

from typing import Any

from src.gateway.router import ModelRouter


class FoundryGateway:
    def __init__(self) -> None:
        self.router = ModelRouter()

    def chat(self, messages: list[dict[str, str]], task: str = "chat") -> dict[str, Any]:
        deployment = self.router.resolve(task)
        user = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
        # Local stub — replace with Azure AI / Foundry SDK calls in real environments.
        return {
            "deployment": deployment.name,
            "content": f"[stub:{deployment.name}] {user}",
            "grounding": [],
            "safety": {"blocked": False},
        }
