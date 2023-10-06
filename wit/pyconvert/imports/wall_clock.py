from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

@dataclass
class Datetime:
    seconds: int
    nanoseconds: int

class HostWallClock(Protocol):
    @abstractmethod
    def now(self) -> Datetime:
        raise NotImplementedError

