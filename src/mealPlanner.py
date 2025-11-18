#!/usr/bin/python

import sys
from langchain_ollama import ChatOllama
from langchain.messages import AIMessage

llm = ChatOllama(
    model="gemma3:270m",
    temperature=0,
    base_url="http://ollama:11434"
)

result = llm.invoke([
    (
        "system",
        "Your are a helpful assistant that creates affordable meal plans made of whole foods for 2 adults and 1 teenager."
        "One of the adults is a vegetarian. Provide a weekly meal plan that is based off the ingredients the user provides."
    ),
    (
        "human",
        "pinto beans, rice, chicken, tofu, canned tomatoes, sweet potatoes, potatoes"
    )
]
)

print(result.content)


