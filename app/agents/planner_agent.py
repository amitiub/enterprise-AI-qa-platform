
from openai import OpenAI
from app.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class PlannerAgent:
    @staticmethod
    def plan(user_story, model="gpt-4o-mini"):
        prompt = f"Break this user story into detailed test scenarios:\n{user_story}"
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
