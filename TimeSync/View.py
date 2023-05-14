import TimeSync.Controller as Controller


class View:

    def __init__(self, controller: Controller):
        self.controller = controller
        print("Welcome to TimeSync")

    def main_menu(self):
        while True:
            self._print_main_menu()
            selection = input("Select an option: ")
            match selection:
                case "1":
                    self.create_new_task()
                case "2":
                    # TODO: log time on task
                    print("not implemented")
                    self.log_time_on_task()
                case "3":
                    # TODO: view time logged on task
                    print("not implemented")
                    self.view_time_logged_on_task()
                case "4":
                    # TODO: view time logged on all tasks
                    print("not implemented")
                    self.view_time_logged_on_all_tasks()
                case "5":
                    # TODO: edit task
                    print("not implemented")
                    self.edit_task()
                case "6":
                    # TODO: delete task
                    print("not implemented")
                    self.delete_task()
                case "7":
                    # TODO: exit
                    print("not implemented")
                    self.exit()

    @staticmethod
    def _print_main_menu():
        print("Main Menu\n"
              "1. Create new task\n"
              "2. Log time on task\n"
              "3. View time logged on task\n"
              "4. View time logged on all tasks\n"
              "5. Edit task\n"
              "6. Delete task\n"
              "7. Exit\n")

    def create_new_task(self):
        print("Enter task details")
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        clickup_task = None

        selection = self.text_list_to_menu("ClickUp task", ["Create new task", "Select existing task"])
        match selection:
            case 0:
                print("not implemented")
                # clickup_task = self.controller.create_new_task(name, description)
            case 1:
                clickup_task = self.controller.get_clickup_task()
        # TODO: add jira task

        self.controller.create_new_task(name, description, clickup_task)

    @staticmethod
    def text_list_to_menu(name, selection_list):
        while True:
            print(f"Select {name}:")
            # print("0: Back")  # TODO: make this work add to end of list

            for index, item in enumerate(selection_list):
                print(f"{index}: {item}")

            selection = input("Enter selection: ")

            selection = int(selection)
            if selection < 0 or selection >= len(selection_list):
                print("Invalid selection")
                continue
            return selection

    def item_list_to_menu(self, name, selection_list):
        text_list = [item.name for item in selection_list]
        return selection_list[self.text_list_to_menu(name, text_list)]
