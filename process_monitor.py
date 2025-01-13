import multiprocessing as mp
from time import sleep
from typing import Callable

from psutil import NoSuchProcess, Process
from terminaltables3 import AsciiTable

__all__ = ["MPMonitor", "MPProcessFailure"]


class MPProcessFailure(Exception):
    """Custom exception for access denied"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MPProcess(mp.Process):
    def __init__(self, target=None, name=None, args=(), kwargs={}) -> None:
        super().__init__(target=target, name=name, args=args, kwargs=kwargs)
        self._pconn, self._cconn = mp.Pipe()
        self._err = False
        self._exception = None

    def run(self):
        try:
            super().run()
            self._cconn.send(None)
        except Exception as e:
            self._cconn.send((e,))

    @property
    def exception(self):
        """ Returns (exception, traceback) if run raises one."""
        if self._pconn.poll():
            exception = self._pconn.recv()
            if exception:
                self._exception = exception
                self._err = True

        return self._exception

    @property
    def failed(self):
        return self._err


class MPMonitor:
    def __init__(self) -> None:
        self.procs = []

    @property
    def number_of_procs(self) -> int:
        return len(self.procs)

    def add_proc(self, target: Callable, args: tuple = ()) -> None:
        proc_name = f"{self.number_of_procs+1}".rjust(2, "0")
        proc = MPProcess(name=proc_name, target=target, args=args)
        self.procs.append(proc)

    def start(self) -> None:
        for proc in self.procs:
            proc.start()

    def get_proc_info(self, process) -> dict:
        if not process.is_alive():
            return {"pid": process.pid, "status": "stopped"}

        try:
            p = Process(process.pid)
            cpu_percent = p.cpu_percent(interval=0.1)
            memory_percent = p.memory_percent()
            status = p.status()
        except NoSuchProcess:
            return {"pid": process.pid, "status": "terminated"}
        except Exception as e:
            return {"pid": process.pid, "status": f"error: {e}"}

        return {
            "pid": process.pid, "cpu_percent": cpu_percent,
            "memory_percent": memory_percent, "status": status
        }

    def monitor_processes(self, silent: bool = True) -> None:
        output = [["Process", "PID", "Status"]]
        for proc in self.procs:
            info = self.get_proc_info(proc)
            status = proc.exception if proc.exception else info["status"]
            output.append([proc.name, info['pid'], status])
        output_table = AsciiTable(output, "Process Monitor")

        if not silent:
            print(output_table.table)

    def terminate_all(self) -> None:
        for proc in self.procs:
            if proc.is_alive():
                proc.terminate()
                proc.join()

    def __del__(self):
        self.terminate_all()


def worker_function(i) -> None:
    import random

    print(f"Worker {i} started")
    sleep(random.randint(1, 10))
    print(f"Worker {i} finished")


if __name__ == "__main__":
    # example of implementation

    print("Parent Log - start")

    monitor = MPMonitor()
    for i in range(1, 11):
        monitor.add_proc(target=worker_function, args=(i, ))
    monitor.start()

    while any(proc.is_alive() for proc in monitor.procs):
        monitor.monitor_processes(silent=False)
        sleep(2)

    failure = any(proc.failed for proc in monitor.procs)
    del monitor

    print("Parent Log - end")

    if failure:
        raise MPProcessFailure("A monitored process failed!")
