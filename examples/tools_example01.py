import os

from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel
from strands_tools import calculator

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
model = LiteLLMModel(
    client_args={
        "api_key": OPENAI_API_KEY,
    },
    model_id="openai/gpt-4o",
    params={
        "max_tokens": 1000,
        "temperature": 0.7
    }
)


@tool
def add_ai_disclaimer(model_output: str) -> str:
    """Use this tool to add AI disclaimer.

    Args:
        model_output: The output generated by the model
    """
    output_message = "Result is generated by AI \n " + model_output
    return output_message


@tool
def answer_quiz(prompt: str) -> str:
    """Use this tool to answer quiz question.

    Args:
        prompt: The input question
    """
    output_message = "Photo synthesis is how plants eat food"
    return output_message


agent = Agent(tools=[calculator, answer_quiz], model=model, max_parallel_tools=1)


result = agent("Always use provided tools. Calculate 40 * 80 divided by 100 and then answer what is photosynthesis")


print(result.message)
print(result.metrics)
# # Direct tool call with recording (default behavior)
# agent.tool.calculator(expression="123 * 456")
#
# # Direct tool call without recording
# agent.tool.calculator(expression="765 / 987", record_direct_tool_call=False)
