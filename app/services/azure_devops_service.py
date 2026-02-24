
import requests
from app.settings import AZURE_ORG_URL, AZURE_PROJECT, AZURE_PAT

class AzureDevOpsService:

    def __init__(self):
        self.auth = ('', AZURE_PAT)

    def get_user_story(self, work_item_id):
        url = f"{AZURE_ORG_URL}/{AZURE_PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=6.0"
        response = requests.get(url, auth=self.auth, verify="cgi_root_ca.pem")
        response.raise_for_status()
        return response.json()

    def create_test_plan(self, name):
        url = f"{AZURE_ORG_URL}/{AZURE_PROJECT}/_apis/testplan/plans?api-version=6.0"
        payload = { "name": name }
        response = requests.post(url, json=payload, auth=self.auth)
        response.raise_for_status()
        return response.json()
