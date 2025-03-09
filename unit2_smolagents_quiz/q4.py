from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, HfApiModel

agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(),
    max_steps=10,
    name="ddgo",
    description="DuckDuckGoSearchTool",
)

agent.run(
    "Search for the best music recommendations for a party at the Wayne's mansion."
)