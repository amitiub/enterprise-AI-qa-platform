
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ORG_URL = os.getenv("AZURE_ORG_URL")
AZURE_PROJECT = os.getenv("AZURE_PROJECT")
AZURE_PAT = os.getenv("AZURE_PAT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

AVAILABLE_MODELS = [
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-4.1-mini",
    "gpt-4.1",
    "o3-mini"
]

"""
| Model        | Best For                       |
| ------------ | ------------------------------ |
| gpt-4o-mini  | Fast bulk test case generation |
| gpt-4o       | Balanced quality + speed       |
| gpt-4.1      | Complex business rules         |
| o3-mini      | Deep logic validation          |
| gpt-4.1-mini | Cost-optimized reasoning       |
"""