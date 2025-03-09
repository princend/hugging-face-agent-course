from smolagents import CodeAgent, HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

agent = CodeAgent(
    tools=[],
    executor_type="e2b",
    model=model,
    additional_authorized_imports=["numpy"],  # Authorize numpy import
)


### 官方solution 
"""
### 但是執行會錯誤
### ImportError: cannot import name 'E2BSandbox' from 'smolagents'
"""

# from smolagents import CodeAgent, E2BSandbox
# model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
# agent = CodeAgent(
#     tools=[],
#     model=model,
#     sandbox=E2BSandbox(),
#     additional_authorized_imports=["numpy"]
# )
