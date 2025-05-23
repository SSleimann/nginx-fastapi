from typing import Any

from prometheus_client import multiprocess


def child_exit(_: Any, worker: Any) -> None:
    multiprocess.mark_process_dead(worker.pid)
