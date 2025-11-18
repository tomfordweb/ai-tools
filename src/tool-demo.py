#!/usr/bin/python

from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.messages import AIMessage
from typing import Literal

class WeatherInput(BaseModel):
    """Input for weather queries."""
    location: str = Field(description="City name or coordinates")
    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius",
        description="Temperature unit preference"
    )
    include_forecast: bool = Field(
        default=False,
        description="Include 5-day forecast"
    )

@tool(args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result

model = ChatOllama(
    model="gpt-oss:20b",
    validate_model_on_init=True,
    temperature=1,
    base_url="http://ollama:11434"
)

agent = create_agent(
    model,
    tools=[get_weather],
    system_prompt="You are a weatherman who returns details forecast information for the specified input"

)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "provide the forecast for kalamazoo, mi in farenheit"}]},
)

print(result)

