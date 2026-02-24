
from openai import OpenAI
from app.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class TestCaseAgent:
    @staticmethod
    def generate(scenarios, model="gpt-4o-mini"):
        prompt = f"""
Convert these scenarios into structured JSON test cases.

Format:
[
    {{
        "id": "",
        "title": "",
        "preconditions": "",
        "steps": [],
        "expected_result": ""
    }}
]

Scenarios:
{scenarios}
"""
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
