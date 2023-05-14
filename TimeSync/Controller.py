import os
import logging

import pyclickup.models

from TimeSync.Services.ClickUp import ClickUpService
from TimeSync.View import View
from TimeSync.models.Task import Task
from TimeSync.models.Model import Model

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self):
        self.click_up_service = ClickUpService(self)
        self.view = View(self)
        self.model = Model(self)

    def start(self):
        logger.info("Controller start")
        # TODO: add main menu
        self.view.main_menu()

    def stop(self):
        logger.info("Controller stop")

    # View methods
    def item_selection(self, name, selection_list):
        return self.view.item_list_to_menu(name, selection_list)

    def clickup_list_selection(self, name, selection_list: [pyclickup.models.Project]):
        project_list: list = []
        for project in selection_list:
            if project.lists:
                for i in project.lists:
                    project_list.append(i)
        return self.view.item_list_to_menu(name, project_list)

    def get_clickup_task(self):
        return self.click_up_service.get_task_by_selection()

    # Task methods
    # TODO: if ClickUp task is not found, create new ClickUp task
    # TODO: Add Jira task to TimeSync task
    # TODO: if Jira task is not found, create new Jira task
    def create_new_task(self, name, description, clickup_task=None, jira_task=None):
        task = Task(name, description, clickup_task)
        self.model.add_task(task)

    # TODO: Log time on TimeSync task

    # TODO: View time logged on TimeSync task

    # TODO: View time logged on all TimeSync tasks <- pandas?

    # TODO: Delete TimeSync task
