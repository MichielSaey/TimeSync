import os
import logging

import pyclickup.models
from pyclickup import ClickUp

import TimeSync.Controller as Controller
logger = logging.getLogger(__name__)


class ClickUpService(ClickUp):
    def __init__(self, controller: Controller):
        super().__init__(os.environ["CLICKUP_API_KEY"])
        self.controller = controller

    def get_task_by_selection(self):
        """
        Get ClickUp task based on the selected project and task.

        :return:
        """
        logger.info("get clickup task")
        selected_team = pyclickup.models.Team = self.teams[0]
        selected_space: pyclickup.models.Space = self.controller.item_selection('Role', selected_team.spaces)
        selected_list: pyclickup.models.List = self.controller.clickup_list_selection('Project', selected_space.projects)
        selected_task: pyclickup.models.Task = self.controller.item_selection('Task', selected_list.get_all_tasks())

        # TODO: add clickup task to TimeSync task
        return selected_task





