from .imports import RootImports
from .intrinsics import _clamp, _decode_utf8, _encode_utf8, _list_canon_lift, _list_canon_lower, _load, _store
from .types import Err, Ok
import ctypes
import pathlib
from typing import cast
import wasmtime

class Root:
    
    def __init__(self, store: wasmtime.Store, import_object: RootImports) -> None:
        path = pathlib.Path(__file__).parent / ('root.core2.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance0 = wasmtime.Instance(store, module, []).exports(store)
        path = pathlib.Path(__file__).parent / ('root.core0.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance1 = wasmtime.Instance(store, module, [
            instance0["12"],
            instance0["0"],
        ]).exports(store)
        def lowering0_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_input_stream(arg0 & 0xffffffff)
        lowering0_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline0 = wasmtime.Func(store, lowering0_ty, lowering0_callee, access_caller = True)
        def lowering1_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_output_stream(arg0 & 0xffffffff)
        lowering1_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline1 = wasmtime.Func(store, lowering1_ty, lowering1_callee, access_caller = True)
        def lowering2_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.types.drop_descriptor(arg0 & 0xffffffff)
        lowering2_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline2 = wasmtime.Func(store, lowering2_ty, lowering2_callee, access_caller = True)
        def lowering3_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdin.get_stdin()
            return _clamp(ret, 0, 4294967295)
        lowering3_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline3 = wasmtime.Func(store, lowering3_ty, lowering3_callee, access_caller = True)
        def lowering4_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_input.drop_terminal_input(arg0 & 0xffffffff)
        lowering4_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline4 = wasmtime.Func(store, lowering4_ty, lowering4_callee, access_caller = True)
        def lowering5_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdout.get_stdout()
            return _clamp(ret, 0, 4294967295)
        lowering5_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline5 = wasmtime.Func(store, lowering5_ty, lowering5_callee, access_caller = True)
        def lowering6_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_output.drop_terminal_output(arg0 & 0xffffffff)
        lowering6_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline6 = wasmtime.Func(store, lowering6_ty, lowering6_callee, access_caller = True)
        def lowering7_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stderr.get_stderr()
            return _clamp(ret, 0, 4294967295)
        lowering7_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline7 = wasmtime.Func(store, lowering7_ty, lowering7_callee, access_caller = True)
        path = pathlib.Path(__file__).parent / ('root.core1.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance2 = wasmtime.Instance(store, module, [
            instance1["memory"],
            instance0["1"],
            instance0["4"],
            instance0["7"],
            instance0["5"],
            instance0["6"],
            instance0["8"],
            instance1["cabi_realloc"],
            trampoline0,
            trampoline1,
            trampoline2,
            instance0["2"],
            instance0["3"],
            trampoline3,
            instance0["9"],
            trampoline4,
            trampoline5,
            instance0["10"],
            trampoline6,
            trampoline7,
            instance0["11"],
        ]).exports(store)
        def lowering8_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ptr = arg0
            len0 = arg1
            list = _decode_utf8(self._core_memory0, caller, ptr, len0)
            import_object.host.print(list)
        lowering8_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline8 = wasmtime.Func(store, lowering8_ty, lowering8_callee, access_caller = True)
        core_memory0 = instance1["memory"]
        assert(isinstance(core_memory0, wasmtime.Memory))
        self._core_memory0 = core_memory0
        def lowering9_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.preopens.get_directories()
            vec = ret
            len3 = len(vec)
            result = self._realloc0(caller, 0, 0, 4, len3 * 12)
            assert(isinstance(result, int))
            for i4 in range(0, len3):
                e = vec[i4]
                base0 = result + i4 * 12
                (tuplei,tuplei1,) = e
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 0, _clamp(tuplei, 0, 4294967295))
                ptr, len2 = _encode_utf8(tuplei1, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 8, len2)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 4, ptr)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, len3)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 0, result)
        lowering9_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline9 = wasmtime.Func(store, lowering9_ty, lowering9_callee, access_caller = True)
        realloc0 = instance2["cabi_import_realloc"]
        assert(isinstance(realloc0, wasmtime.Func))
        self._realloc0 = realloc0
        def lowering10_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int) -> None:
            ret = import_object.types.write_via_stream(arg0 & 0xffffffff, arg1 & 0xffffffffffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 0, 0)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg2, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 4, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering10_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i64(), wasmtime.ValType.i32(), ], [])
        trampoline10 = wasmtime.Func(store, lowering10_ty, lowering10_callee, access_caller = True)
        def lowering11_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.types.append_via_stream(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg1, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 4, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering11_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline11 = wasmtime.Func(store, lowering11_ty, lowering11_callee, access_caller = True)
        def lowering12_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.types.get_type(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 1, (payload).value)
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 1, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering12_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline12 = wasmtime.Func(store, lowering12_ty, lowering12_callee, access_caller = True)
        def lowering13_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.streams.check_write(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
                _store(ctypes.c_uint64, self._core_memory0, caller, arg1, 8, _clamp(payload, 0, 18446744073709551615))
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 8, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering13_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline13 = wasmtime.Func(store, lowering13_ty, lowering13_callee, access_caller = True)
        def lowering14_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = cast(bytes, _list_canon_lift(ptr, len0, 1, ctypes.c_uint8, self._core_memory0, caller))
            ret = import_object.streams.write(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
            elif isinstance(ret, Err):
                payload1 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 1, (payload1).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering14_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline14 = wasmtime.Func(store, lowering14_ty, lowering14_callee, access_caller = True)
        def lowering15_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = cast(bytes, _list_canon_lift(ptr, len0, 1, ctypes.c_uint8, self._core_memory0, caller))
            ret = import_object.streams.blocking_write_and_flush(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
            elif isinstance(ret, Err):
                payload1 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 1, (payload1).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering15_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline15 = wasmtime.Func(store, lowering15_ty, lowering15_callee, access_caller = True)
        def lowering16_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.streams.blocking_flush(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 1, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering16_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline16 = wasmtime.Func(store, lowering16_ty, lowering16_callee, access_caller = True)
        def lowering17_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdin.get_terminal_stdin()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering17_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline17 = wasmtime.Func(store, lowering17_ty, lowering17_callee, access_caller = True)
        def lowering18_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdout.get_terminal_stdout()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering18_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline18 = wasmtime.Func(store, lowering18_ty, lowering18_callee, access_caller = True)
        def lowering19_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stderr.get_terminal_stderr()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering19_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline19 = wasmtime.Func(store, lowering19_ty, lowering19_callee, access_caller = True)
        path = pathlib.Path(__file__).parent / ('root.core3.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance3 = wasmtime.Instance(store, module, [
            trampoline8,
            trampoline9,
            trampoline10,
            trampoline11,
            trampoline12,
            trampoline13,
            trampoline14,
            trampoline15,
            trampoline16,
            trampoline17,
            trampoline18,
            trampoline19,
            instance2["fd_write"],
            instance0["$imports"],
        ]).exports(store)
        realloc1 = instance1["cabi_realloc"]
        assert(isinstance(realloc1, wasmtime.Func))
        self._realloc1 = realloc1
        post_return0 = instance1["cabi_post_exec"]
        assert(isinstance(post_return0, wasmtime.Func))
        self._post_return0 = post_return0
        lift_callee0 = instance1["exec"]
        assert(isinstance(lift_callee0, wasmtime.Func))
        self.lift_callee0 = lift_callee0
    def exec(self, caller: wasmtime.Store, input: bytes) -> bytes:
        ptr, len0 = _list_canon_lower(input, ctypes.c_uint8, 1, 1, self._realloc1, self._core_memory0, caller)
        ret = self.lift_callee0(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_int32, self._core_memory0, caller, ret, 0)
        load1 = _load(ctypes.c_int32, self._core_memory0, caller, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(bytes, _list_canon_lift(ptr2, len3, 1, ctypes.c_uint8, self._core_memory0, caller))
        self._post_return0(caller, ret)
        return list
