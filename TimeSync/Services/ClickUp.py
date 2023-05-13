import os
import logging

from pyclickup import ClickUp

logger = logging.getLogger(__name__)


class ClickUpService(ClickUp):
    def __init__(self):
        super().__init__()

    def get_all_tasks(self):
        """
        Get ClickUp tasks.

        :return:
        """
        logger.info("get clickup all tasks")
        print(self.teams)
