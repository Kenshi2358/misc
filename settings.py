"""
This script contains the custom logger configuration.
"""
import os
import logging

def addLoggingLevel(levelName, levelNum, methodName=None):
    """
    Adds a new logging level to the `logging` module and the
    currently configured logging class.
    """

    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError(f'{levelName} already defined in logging module')
    if hasattr(logging, methodName):
        raise AttributeError(f'{methodName} already defined in logging module')
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError(f'{methodName} already defined in logger class')

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)
    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)

# Need to add this before class: CustomFormatter.
addLoggingLevel('MAIN', 25)
addLoggingLevel('TCLS', 26)

class CustomFormatter(logging.Formatter):
    """
    Custom formatting class for logging module, to help with Jenkins output.
    \033 is the ascii escape character.
    """

    blue = "\033[0;34m"

    #green = "\033[38;5;82m" # old green
    green = "\033[38;5;40m" 

    yellow = "\033[1;33m"

    #red = "\033[38;5;196m" # old red
    red = "\033[0;31m"

    # ---------------
    # Un-used colors.
    black = '\033[0;30m'
    brown = '\033[0;33m'
    purple = '\033[0;35m'
    cyan = '\033[0;36m'

    grey = '\033[0;37m'
    dark_grey = '\033[1;30m'
    light_red = '\033[1;31m'
    light_green = '\033[1;32m'

    light_blue = '\033[1;34m'
    light_purple = '\033[1;35m'
    light_cyan = '\033[1;36m'
    white = '\033[1;37m'
    # ---------------

    bold = "\033[1m"
    reset = "\033[0m"

    format = '%(asctime)s %(levelname)-8s %(message)s'

    FORMATS = {
        logging.DEBUG: blue + bold + format + reset,

        logging.INFO: format + reset,
        logging.MAIN: green + bold + format + reset,
        logging.TCLS: blue + bold + format + reset,

        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + bold + format + reset,
        logging.CRITICAL: red + bold + format + reset
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        date_format = '%Y-%m-%d %H:%M:%S'

        formatter = logging.Formatter(log_format, date_format)
        return formatter.format(record)

# Instantiate a logger object to the logger class.
logger = logging.getLogger("main_logger_settings")
# Set the log level.
logger.setLevel(logging.INFO)

# Create console handler.
# Handlers specify where the logging should go - either the console or to a file.
# Streamhandler tells the logger to print messages to the console.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# The Formatter tells the logger how to customize the log messages.
console_handler.setFormatter(CustomFormatter())

# Add the handler object to the logger object using the addHandler() method.
logger.addHandler(console_handler)

logger.debug(f'OS environ variables: {os.environ}')
