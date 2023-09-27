from ..types import Err, Ok, Result
import wasmtime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .. import Root

class Run:
    component: 'Root'
    
    def __init__(self, component: 'Root') -> None:
        self.component = component
    def run(self, caller: wasmtime.Store) -> Result[None, None]:
        ret = self.component.lift_callee1(caller)
        assert(isinstance(ret, int))
        expected: Result[None, None]
        if ret == 0:
            expected = Ok(None)
        elif ret == 1:
            expected = Err(None)
        else:
            raise TypeError("invalid variant discriminant for expected")
        return expected
