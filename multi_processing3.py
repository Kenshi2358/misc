import logging
import logging.handlers
import multiprocessing

from time import sleep, time

from process_monitor import MPMonitor, MPProcessFailure
from functools import wraps
import argparse
import math


def worker_process(parent_queue, process_id):
    
    # Setup a child logger.
    child_logger = logging.getLogger(process_id)
    child_logger.setLevel(logging.INFO)

    # handler = logging.handlers.QueueHandler(parent_queue)
    # child_logger.addHandler(handler)
    # child_logger.propagate = False

    if not child_logger.handlers:
        handler = logging.handlers.QueueHandler(parent_queue)
        child_logger.addHandler(handler)

    for i in range(5):
        child_logger.info(f"{process_id} - logging {i}")
        sleep(1)


def convert_time(total_seconds: float) -> str:

    output_str = ''
    minutes = 0

    if total_seconds >= 60:
        minutes = math.floor(total_seconds / 60)
        num_seconds = total_seconds % 60
    else:
        num_seconds = total_seconds

    if minutes == 0:
        output_str += f"{num_seconds:2.0f} sec"
    else:
        output_str += f"{minutes:2} min {num_seconds:2.0f} sec"

    return output_str


def timing(f):
    """
    Timing decorator for functions.
    """

    @wraps(f)
    def wrap(*args, **kw):
        time_start = time()
        result = f(*args, **kw)
        time_end = time()

        net_time = convert_time(time_end - time_start)
        logging.info(f"func:{f.__name__!r} args:[{args!r}, {kw!r}] took: {net_time}")
        return result

    return wrap


@timing
def main(args):

    # Create a custom parent queue to listen to child processes.
    parent_queue = multiprocessing.Queue()

    # Create a custom logger, including listening to the queue.
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(parent_queue, handler)
    listener.start()

    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)

    monitor = MPMonitor()

    num_process = 3
    for i in range(1, num_process + 1):
        process_id = f"p{i}"
        monitor.add_proc(
            target=worker_process,
            args=(parent_queue, process_id),
        )

    logging.info("Parent logger - Starting monitor")
    # start monitored jobs
    monitor.start()

    # while processes are alive, monitor jobs
    while any(proc.is_alive() for proc in monitor.procs):
        monitor.monitor_processes()
        sleep(2)

    # check for failures
    failure = any(proc.failed for proc in monitor.procs)
    if failure:
        output = "\n"
        for proc in monitor.procs:
            if proc.failed:
                output += f"{proc.name} failed: {proc.exception}\n"

        logging.error(output)
        raise MPProcessFailure("Failure during load process.")

    # end monitored jobs
    monitor.terminate_all()
    del monitor

    logging.info("Parent logger - ending monitor")

    # Stop the Queue Listener.
    listener.stop()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)
