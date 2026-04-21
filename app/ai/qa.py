import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/chat"

# Model you installed (change if needed)
MODEL = "llama3.2:1b"


def ask_question(summary, question):
    """
    Calls your local Ollama AI safely.
    Returns a clean answer string.
    """

    try:
        prompt = f"""
You are a business data analyst AI.

Dataset summary:
{summary}

User question:
{question}

Provide a clear and practical answer
based ONLY on the dataset information.
"""

        res = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "You are a business data analyst AI."},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=400
        )

        res.raise_for_status()

        data = res.json()

        # New Ollama API returns nested message object
        answer = (
            data.get("message", {})
                .get("content", "")
                .strip()
        )

        if not answer:
            return "AI returned an empty response."

        return answer

    except Exception as e:
        return f"AI service error:\n{str(e)}"
