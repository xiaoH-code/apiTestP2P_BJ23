import logging
from app import init_log_config

init_log_config()
logging.error("error")
logging.info("info")
logging.debug("debug")