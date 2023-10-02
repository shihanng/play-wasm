from abc import abstractmethod
from typing import Protocol

Instant = int
class HostMonotonicClock(Protocol):
    @abstractmethod
    def now(self) -> Instant:
        raise NotImplementedError

