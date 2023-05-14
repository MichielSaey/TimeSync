import os
import logging

import pyclickup.models
from jira import JIRA

import TimeSync.Controller as Controller
logger = logging.getLogger(__name__)

class JiraService(JIRA):
    def __init__(self, controller: Controller):
        super().__init__(
            os.getenv("JIRA_URL"),
            basic_auth=(os.getenv("JIRA_USER"), os.getenv("JIRA_API_KEY"))
        )
        self.controller = controller

    def get_task(self):
        pass