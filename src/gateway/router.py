from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Deployment:
    name: str
    task: str


class ModelRouter:
    def __init__(self) -> None:
        self.deployments = {
            "chat": Deployment(os.getenv("AZURE_AI_CHAT_DEPLOYMENT", "gpt-4o-mini"), "chat"),
            "embed": Deployment(os.getenv("AZURE_AI_EMBED_DEPLOYMENT", "text-embedding-3-small"), "embed"),
        }

    def resolve(self, task: str) -> Deployment:
        if task not in self.deployments:
            raise KeyError(f"No deployment for task={task}")
        return self.deployments[task]
