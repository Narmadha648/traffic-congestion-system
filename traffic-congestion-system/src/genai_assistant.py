import openai
import os

openai.api_key = "YOUR_OPENAI_KEY"

def generate_insight(level):
    prompt = f"""
    Congestion level is {level}.
    Provide traffic insight and rerouting suggestion.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )

    return response['choices'][0]['message']['content']