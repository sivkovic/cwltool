# Stubs for galaxy.jobs.metrics.collectl.stats (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class StatisticsTracker:
    min = ...  # type: Any
    max = ...  # type: Any
    count = ...  # type: int
    sum = ...  # type: int
    def __init__(self) -> None: ...
    def track(self, value): ...
    @property
    def avg(self): ...
