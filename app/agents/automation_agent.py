
from openai import OpenAI
from app.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class AutomationAgent:
    @staticmethod
    def generate(user_story, model="gpt-4o-mini"):
        prompt = f"""
You are an expert Java automation architect.
Generate Selenium Web automation framework in Java using:
- Maven project structure
- TestNG
- Page Object Model
- WebDriverManager
- Proper package structure
- BaseTest class
- One sample Page class
- One sample Test class
- Use good naming conventions
- Include comments

User Story:
{user_story}
"""
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
