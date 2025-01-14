# Example of logging from multiple processes in a process-safe manner.

from random import random
from multiprocessing import current_process
from multiprocessing import Process
from multiprocessing import Queue

import logging
from logging.handlers import QueueHandler

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


def logger_process(queue):

    logger = logging.getLogger('app')

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    while True:
        ## Consume a log message. If none arrive, end loop. Otherwise, log the message.
        message = queue.get()
        if message is None:
            break
        logger.handle(message)


# task to be executed in child processes
@timing
def task(queue):
    # create a logger
    logger = logging.getLogger('app500')
    logger.setLevel(logging.INFO)

    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))

    # get the current process
    process = current_process()
    logger.info(f'Child {process.name} - started')

    # simulate doing work
    for i in range(5):
        logger.info(f'Child {process.name} step {i}')
        sleep(random())

    logger.info(f'Child {process.name} - finished')


@timing
def main(args):

    # create the shared queue
    queue = Queue()
    # create a logger
    logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))
    # set logger level.
    logger.setLevel(logging.INFO)

    # start the logger process
    logger_p = Process(target=logger_process, args=(queue,))
    logger_p.start()

    logger.info('Main process - started')

    monitor = MPMonitor()

    num_process = 3
    for i in range(1, num_process + 1):
        process_id = f"p{i}"
        monitor.add_proc(
            target=task,
            args=(queue,),
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

        logger.error(output)
        raise MPProcessFailure("Failure during load process.")

    del monitor

    # # configure child processes
    # processes = [Process(target=task, args=(queue,)) for i in range(5)]
    # # start child processes
    # for process in processes:
    #     process.start()
    # # wait for child processes to finish
    # for process in processes:
    #     process.join()

    logger.info('Main process - finished')
    # shutdown the queue correctly
    queue.put(None)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)
