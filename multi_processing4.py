# Example of logging from multiple processes in a process-safe manner.

import random
from multiprocessing import current_process
from multiprocessing import Process
from multiprocessing import Queue

import logging
from logging.handlers import QueueHandler, QueueListener

from process_monitor import MPMonitor, MPProcessFailure
from functools import wraps
from time import sleep, time
import math
import argparse


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


handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)

# task to be executed in child processes
@timing
def task():
    # create a logger
    logger = logging.getLogger('app500')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False

    # get the current process
    process = current_process()
    logger.info(f'Child {process.name} - started')

    # simulate doing work
    for i in range(5):
        logger.info(f'Child {process.name} step {i}')
        sleep(random.randint(1, 3))

    logger.info(f'Child {process.name} - finished')


@timing
def main(args):

    logging.info('Main process - started')

    monitor = MPMonitor()

    num_process = 3
    for i in range(1, num_process + 1):
        process_id = f"p{i}"
        monitor.add_proc(
            target=task,
            args=(),
        )

    monitor.start()

    while any(proc.is_alive() for proc in monitor.procs):
        monitor.monitor_processes()
        sleep(2)

    failure = any(proc.failed for proc in monitor.procs)
    if failure:
        output = "\n"
        for proc in monitor.procs:
            if proc.failed:
                output += f"{proc.name} failed: {proc.exception}\n"

        logging.error(output)
        raise MPProcessFailure("Failure during load process.")

    for proc in monitor.procs:
        proc.join()

    logging.info('Main process - finished')
    monitor.monitor_processes(silent=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)
