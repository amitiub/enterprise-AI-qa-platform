🧠 Enterprise AI QA Platform

An enterprise-grade AI-powered QA automation platform that integrates with Azure DevOps to:

Generate structured test cases

Generate Selenium Java automation framework code

Use multi-agent AI architecture

Optionally create Azure Test Plans

Deploy to Azure App Service

🚀 Overview

This platform uses a multi-agent AI pipeline to transform Azure DevOps User Stories into:

Structured Gherkin-style test cases

Selenium Web (Java + TestNG + POM) automation code

It supports model selection, structured generation, logging, and enterprise deployment readiness.

🏗 Architecture
Azure DevOps → Planner Agent → Test Case Agent → Automation Agent
                                      ↓
                               Validation & Logging
AI Agents
Agent	Responsibility
PlannerAgent	Breaks user story into test scenarios
TestCaseAgent	Generates structured JSON test cases
AutomationAgent	Generates Selenium Java framework code
🛠 Tech Stack

FastAPI

OpenAI (latest SDK)

Azure DevOps REST API

Bootstrap 5 (UI)

Gunicorn (Azure deployment)

Python 3.11+

📂 Project Structure
AI_QA_PLATFORM/
│
├── app/
│   ├── main.py
│   ├── settings.py
│   ├── core/
│   ├── agents/
│   ├── services/
│   ├── templates/
│   └── static/
│
├── requirements.txt
├── startup.txt
└── README.md
⚙️ Setup Instructions (Local Development)
1️⃣ Clone or Extract Project

Navigate to project folder:

cd AI_QA_PLATFORM
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create .env File

Create a file in project root:

.env

Add:

AZURE_ORG_URL=https://your-azure-url
AZURE_PROJECT=YourProject
AZURE_PAT=YourPersonalAccessToken
OPENAI_API_KEY=your_openai_key
5️⃣ Run Application
uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000
☁ Deployment to Azure App Service

Startup command already configured in:

startup.txt

Startup command:

gunicorn -k uvicorn.workers.UvicornWorker app.main:app

Deploy using Azure CLI:

az webapp up --runtime "PYTHON:3.11"
🎯 Features

✔ Multi-agent AI architecture
✔ Model selection (gpt-4o, gpt-4o-mini, etc.)
✔ Structured Gherkin test case generation
✔ Selenium Java automation (POM + TestNG)
✔ Azure DevOps integration
✔ Loading spinner + UI enhancements
✔ Download generated outputs
✔ Basic enterprise logging
✔ Azure App Service ready

🧠 AI Model Configuration

Models can be selected dynamically from UI.

Recommended usage:

Agent	Recommended Model
Planner	o3-mini
Test Case	gpt-4o-mini
Automation	gpt-4o
🔐 Security Notes

Do not commit .env file

Use Azure Key Vault in production

Use corporate SSL certificate if required

Do not disable SSL verification in production

📈 Performance Considerations

For optimal performance:

Use lighter models for simple stories

Clean HTML from Azure description before sending to AI

Use parallel agent execution (future enhancement)

🚀 Future Enhancements

Full Azure Test Case upload

Agentic AI loop (self-validation + retry)

JSON schema validation

Streaming AI response

Cost tracking

Execution metrics dashboard

CI/CD integration

👨‍💻 Author

Enterprise AI QA Platform
Designed for scalable AI-powered test automation workflows.
