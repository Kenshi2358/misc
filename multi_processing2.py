import logging
import logging.handlers
import multiprocessing
import time


def worker_process(parent_queue, process_id):
    # This is an example of a function called that takes in the parent_queue and the process_id.
    child_logger = logging.getLogger(process_id)
    child_logger.setLevel(logging.INFO)

    if not child_logger.handlers:
        handler = logging.handlers.QueueHandler(parent_queue)
        child_logger.addHandler(handler)

    for i in range(5):
        child_logger.info(f"{process_id} - logging {i}")
        time.sleep(1)


def setup_logging(queue):
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(queue, handler)
    listener.start()

    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)


if __name__ == "__main__":
    parent_queue = multiprocessing.Queue()
    setup_logging(parent_queue)

    num_process = 3
    processes = [multiprocessing.Process(target=worker_process, args=(parent_queue, f"p{i}")) for i in range(1, num_process + 1)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    parent_queue.put(None)

    logging.info("Done running.")
