import os
from unittest.mock import DEFAULT

from openai import OpenAI

client = OpenAI()

DEFAULT_LLM = os.getenv("LLM_NAME")

def chat(message: str, model: str):
    model_name = DEFAULT_LLM
    match model:
        case "llama3":
            model_name = "llama3.1:8b"
        case "gemma2":
            model_name = "gemma2:latest"
        case "mistral":
            model_name = "mistral:latest"
        case "qwen2.5":
            model_name = "qwen2.5:14b"
    return query_llm(model_name, message)


def query_llm(model: str, question: str):
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": question
            },
        ],
        stream=False,
    )
    return response.choices[0].message.content
