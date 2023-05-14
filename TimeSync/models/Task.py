import pyclickup


class Task:
    def __init__(self,
                 name: str,
                 description: str = None,
                 clickup_task: pyclickup.models.Task = None,
                 # jira_task: jira.resources.Issue = None
                 ):
        self.name = name
        self.description = description
        self.clickup_task = clickup_task
        # self.jira_task = jira_task

    def __str__(self):
        return f"Task: {self.name}\n" \
               f"ClickUp Task: {self.clickup_task}\n" \
               # f"Jira Task: {self.jira_task}\n"

    def __repr__(self):
        return f"Task: {self.name}\n" \
               f"ClickUp Task: {self.clickup_task}\n" \
               # f"Jira Task: {self.jira_task}\n"

    #TODO: Log time on task