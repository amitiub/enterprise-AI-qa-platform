
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.logger import get_logger
from app.agents.planner_agent import PlannerAgent
from app.agents.testcase_agent import TestCaseAgent
from app.agents.automation_agent import AutomationAgent
from app.services.azure_devops_service import AzureDevOpsService
from app.settings import AVAILABLE_MODELS

app = FastAPI(title="Enterprise AI QA Platform")
templates = Jinja2Templates(directory="app/templates")
logger = get_logger()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "models": AVAILABLE_MODELS})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, work_item_id: str = Form(...), model: str = Form(...)):
    try:
        azure = AzureDevOpsService()
        work_item = azure.get_user_story(work_item_id)
        user_story = work_item['fields'].get('System.Description', '')

        logger.info("Planning scenarios")
        scenarios = PlannerAgent.plan(user_story, model)

        logger.info("Generating test cases")
        test_cases = TestCaseAgent.generate(scenarios, model)

        logger.info("Generating automation script")
        automation = AutomationAgent.generate(user_story, model)

        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "test_cases": test_cases,
            "automation": automation
        })

    except Exception as e:
        logger.error(str(e))
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": str(e)
        })
