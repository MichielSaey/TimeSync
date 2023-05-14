import TimeSync.Controller as Controller
class Model:

    def __init__(self, controller: Controller):
        self.controller = controller
        self.all_tasks = []

    def add_task(self, task):
        self.all_tasks.append(task)

    def get_all_tasks(self):
        return self.all_tasks
