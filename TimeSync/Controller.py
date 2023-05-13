import os
import logging

from TimeSync.Services.ClickUp import ClickUpService

logger = logging.getLogger(__name__)

class Controller:
    def __init__(self):
        self.click_up_service = ClickUpService()

    def start(self):
        logger.info("Controller start")
        self.click_up_service.get_all_tasks()
