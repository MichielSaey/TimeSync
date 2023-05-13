import logging
import os


def initialize_logging():  # pragma: no cover
    """
    Initialize logging configuration.
    """
    logging.basicConfig(
        level="INFO",
        format=os.getenv(
            "LOGGING_FORMAT",
            "%(asctime)s %(name)-12s:" " %(levelname)-" "8s -  " "%(message)s",
        ),
    )
    logging.getLogger(__name__).setLevel(os.getenv("LOGGING_LEVEL", "INFO"))
    logging.getLogger("clickup_to_jira").setLevel(
        os.getenv("LOGGING_LEVEL", "INFO")
    )
    logging.getLogger(__name__).propagate = True