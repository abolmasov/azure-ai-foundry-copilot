from src.copilot.extension import CopilotInvokeRequest, handle_copilot_invoke
from src.gateway.foundry import FoundryGateway


def test_chat_stub_uses_router():
    out = FoundryGateway().chat([{"role": "user", "content": "hello"}])
    assert "hello" in out["content"]
    assert out["deployment"]


def test_copilot_contract():
    resp = handle_copilot_invoke(CopilotInvokeRequest(conversation_id="c1", message="hi"))
    assert resp.conversation_id == "c1"
