from ..types import Result
from abc import abstractmethod
from enum import Enum
from typing import Protocol

InputStream = int
OutputStream = int
class WriteError(Enum):
    LAST_OPERATION_FAILED = 0
    CLOSED = 1

class HostStreams(Protocol):
    @abstractmethod
    def drop_input_stream(self, this: InputStream) -> None:
        raise NotImplementedError
    @abstractmethod
    def check_write(self, this: OutputStream) -> Result[int, WriteError]:
        raise NotImplementedError
    @abstractmethod
    def write(self, this: OutputStream, contents: bytes) -> Result[None, WriteError]:
        raise NotImplementedError
    @abstractmethod
    def blocking_write_and_flush(self, this: OutputStream, contents: bytes) -> Result[None, WriteError]:
        raise NotImplementedError
    @abstractmethod
    def blocking_flush(self, this: OutputStream) -> Result[None, WriteError]:
        raise NotImplementedError
    @abstractmethod
    def drop_output_stream(self, this: OutputStream) -> None:
        raise NotImplementedError

