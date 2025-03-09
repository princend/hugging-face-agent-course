
from smolagents import CodeAgent,ToolCallingAgent,DuckDuckGoSearchTool, GoogleSearchTool, HfApiModel, VisitWebpageTool

model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", provider="together")
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool()],
    model=model,
    max_steps=10,
    name="search",
    description="Runs web searches for you."
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"]
)