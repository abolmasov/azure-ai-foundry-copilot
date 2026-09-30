from fastapi import FastAPI
from pydantic import BaseModel

from src.copilot.extension import CopilotInvokeRequest, CopilotInvokeResponse, handle_copilot_invoke
from src.gateway.foundry import FoundryGateway

app = FastAPI(title="Azure AI Foundry Copilot Architecture", version="0.1.0")
gw = FoundryGateway()


class ChatRequest(BaseModel):
    message: str
    task: str = "chat"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    return gw.chat(messages=[{"role": "user", "content": req.message}], task=req.task)


@app.post("/copilot/invoke", response_model=CopilotInvokeResponse)
def copilot(req: CopilotInvokeRequest) -> CopilotInvokeResponse:
    return handle_copilot_invoke(req)
