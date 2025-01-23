import logging
import logging.handlers
from multiprocessing import Queue

def setup_logging(queue):
    """This sets up all the logging, including listening to the queue."""
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(queue, handler)
    listener.start()

    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)

    return listener


parent_queue = Queue()
listener = setup_logging(parent_queue)

# Stop the Queue Listener.
listener.stop()