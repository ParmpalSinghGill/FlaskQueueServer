"""Define functions to use in redis queue."""

import time

from rq import get_current_job


def some_long_function(some_input):
    """An example function for redis queue."""
    print("get_result started")
    job = get_current_job()
    time.sleep(5)
    print("get_result Ended")

    return {
        "job_id": job.id,
        "job_enqueued_at": job.enqueued_at.isoformat(),
        "job_started_at": job.started_at.isoformat(),
        "input": some_input,
        "result": some_input,
    }
