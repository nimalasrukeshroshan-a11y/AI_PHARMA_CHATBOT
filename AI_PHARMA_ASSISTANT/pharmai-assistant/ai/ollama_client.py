"""
Ollama client wrapper for local model inference.
This wrapper attempts common `ollama` call patterns and returns
the model text output as a string. It intentionally does NOT
require any external API keys and works with a locally-installed
Ollama/phi model.
"""

import ollama


def _extract_text_from_response(resp):
    """Try to extract text from various ollama response shapes."""
    try:
        # If dict-like
        if isinstance(resp, dict):
            # common shape used earlier: {"message": {"content": ...}}
            if "message" in resp and isinstance(resp["message"], dict):
                return resp["message"].get("content") or str(resp)
            # sometimes returned as {"choices": [{"text": ...}]}
            if "choices" in resp and isinstance(resp["choices"], list) and resp["choices"]:
                return resp["choices"][0].get("text", str(resp))
            return str(resp)

        # Fallback: try attribute access
        if hasattr(resp, "message"):
            m = getattr(resp, "message")
            if isinstance(m, dict):
                return m.get("content", str(resp))
            # object with content
            if hasattr(m, "get"):
                return m.get("content", str(resp))

        # final fallback
        return str(resp)
    except Exception:
        return str(resp)


def generate_response(prompt, user_profile=None, model_name="phi3"):
    """
    Generate a text response using the local Ollama model.

    Args:
        prompt: The prompt string to send to the model.
        user_profile: Optional user profile (not used by ollama client directly).
        model_name: Ollama model name to use (default: "phi3").

    Returns:
        String with the model response or an error message.
    """
    try:
        # First try the messages-style chat API if available
        try:
            resp = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
            return _extract_text_from_response(resp) or ""
        except TypeError:
            # If signature differs, try a simpler call
            pass

        try:
            # Some ollama versions accept (model, prompt)
            resp = ollama.chat(model_name, prompt)
            return _extract_text_from_response(resp) or ""
        except Exception:
            # Final attempt: direct call with named prompt
            resp = ollama.chat(model=model_name, prompt=prompt)
            return _extract_text_from_response(resp) or ""

    except Exception as e:
        return f"Error generating response via Ollama: {e}"
