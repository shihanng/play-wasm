from .environment import HostEnvironment
from .exit import HostExit
from .monotonic_clock import HostMonotonicClock
from .preopens import HostPreopens
from .stderr import HostStderr
from .stdin import HostStdin
from .stdout import HostStdout
from .streams import HostStreams
from .terminal_input import HostTerminalInput
from .terminal_output import HostTerminalOutput
from .terminal_stderr import HostTerminalStderr
from .terminal_stdin import HostTerminalStdin
from .terminal_stdout import HostTerminalStdout
from .types import HostTypes
from .wall_clock import HostWallClock
from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

class Host(Protocol):
    @abstractmethod
    def print(self, msg: str) -> None:
        raise NotImplementedError

@dataclass
class RootImports:
    host: Host
    wall_clock: HostWallClock
    monotonic_clock: HostMonotonicClock
    streams: HostStreams
    types: HostTypes
    preopens: HostPreopens
    environment: HostEnvironment
    exit: HostExit
    stdin: HostStdin
    stdout: HostStdout
    stderr: HostStderr
    terminal_input: HostTerminalInput
    terminal_output: HostTerminalOutput
    terminal_stdin: HostTerminalStdin
    terminal_stdout: HostTerminalStdout
    terminal_stderr: HostTerminalStderr
