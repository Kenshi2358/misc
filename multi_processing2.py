import logging
import logging.handlers
import multiprocessing
import time

def worker_process(queue, process_name):
    logger = logging.getLogger(process_name)
    logger.setLevel(logging.INFO)
    handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(handler)
    
    for i in range(5):
        logger.info(f"{process_name} - logging {i}")
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
    log_queue = multiprocessing.Queue()
    setup_logging(log_queue)
    
    num_process = 3
    processes = [multiprocessing.Process(target=worker_process, args=(log_queue, f"p{i}")) for i in range(1, num_process + 1)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
    logging.info("Main process logging complete.")
