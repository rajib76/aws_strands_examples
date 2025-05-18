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
boto_session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                     region_name="us-east-1")

model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    temperature=0.3,
    boto_session=boto_session
)


# model = LiteLLMModel(
#     client_args={
#         "api_key": OPENAI_API_KEY,
#     },
#     # **model_config
#     model_id="openai/gpt-4o",
#     params={
#         "max_tokens": 1000,
#         "temperature": 0.7,
#     }
# )

agent = Agent(model=model)

# Ask the agent a question
agent("Tell me about agentic AI")
