import os

import boto3
from dotenv import load_dotenv
from strands import Agent
from strands.models import BedrockModel
from strands.models.litellm import LiteLLMModel

load_dotenv()
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Create a BedrockModel
# model = BedrockModel(
#     model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
#     temperature=0.3
# )


model = LiteLLMModel(
    client_args={
        "api_key": OPENAI_API_KEY,
    },
    # **model_config
    model_id="openai/gpt-4o",
    params={
        "max_tokens": 1000,
        "temperature": 0.7,
    }
)

agent = Agent(model=model)

# Ask the agent a question
agent("Tell me about agentic AI")
