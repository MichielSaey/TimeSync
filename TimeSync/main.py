from TimeSync.Controller import Controller
from TimeSync.utils import initialize_logging

if __name__ == '__main__':
    initialize_logging()
    controller = Controller()
    controller.start()

