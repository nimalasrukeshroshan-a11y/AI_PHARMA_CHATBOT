"""
Compatibility wrapper for older `gorq_client.py` location.
This module delegates to the local `ai.ollama_client.generate_response` if
available. If Ollama or the local wrapper is not present, it returns a
helpful error message instructing how to install and run Ollama and a model.
"""

def generate_response(prompt, user_profile=None):
    """Generate text using local Ollama-based client or return an instructive error."""
    try:
        # Import lazily so missing `ollama` package doesn't fail module import
        from ai.ollama_client import generate_response as _gen
        return _gen(prompt, user_profile=user_profile)
    except ModuleNotFoundError:
        return (
            "Error: local Ollama runtime or Python package not found.\n"
            "Install Ollama per https://ollama.com/ and ensure the `ollama` Python package is available,\n"
            "then pull a model (e.g. `ollama pull phi3`) and run it (`ollama run phi3`) before retrying."
        )
    except Exception as e:
        return f"Error generating response (delegation failed): {e}"
