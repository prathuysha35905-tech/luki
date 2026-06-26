import requests

LM_URL = "http://127.0.0.1:1234/v1/chat/completions"

def explain_movie(movie, recommendations):

    prompt = f"""
A user likes {movie}.

Recommended movies:

{recommendations}

Explain in simple English why these movies are similar.
Keep it under 100 words.
"""

    payload = {
        "model": "qwen/qwen3-8b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(LM_URL, json=payload)

    return response.json()["choices"][0]["message"]["content"]