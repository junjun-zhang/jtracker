
class JOB_STATE:  # enum
    BACKLOG = 'job_state.backlog'
    QUEUED = 'job_state.queued'
    COMPLETED = 'job_state.completed'
    FAILED = 'job_state.failed'
    RUNNING = 'job_state.running'


class TASK_STATE:  # enum
    QUEUED = 'task_state.queued'
    COMPLETED = 'task_state.completed'
    FAILED = 'task_state.failed'
    RUNNING = 'task_state.running'


def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None
