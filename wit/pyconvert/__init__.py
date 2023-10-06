from .imports import RootImports, types
from .intrinsics import _clamp, _decode_utf8, _encode_utf8, _list_canon_lift, _list_canon_lower, _load, _store
from .types import Err, Ok, Result
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
            instance0["19"],
            instance0["20"],
            instance0["21"],
            instance0["22"],
            instance0["0"],
            instance0["23"],
            instance0["24"],
            instance0["25"],
            instance0["26"],
            instance0["27"],
            instance0["28"],
            instance0["29"],
            instance0["30"],
            instance0["31"],
            instance0["32"],
        ]).exports(store)
        def lowering0_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.monotonic_clock.now()
            return _clamp(ret, 0, 18446744073709551615)
        lowering0_ty = wasmtime.FuncType([], [wasmtime.ValType.i64(), ])
        trampoline0 = wasmtime.Func(store, lowering0_ty, lowering0_callee, access_caller = True)
        def lowering1_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.types.drop_directory_entry_stream(arg0 & 0xffffffff)
        lowering1_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline1 = wasmtime.Func(store, lowering1_ty, lowering1_callee, access_caller = True)
        def lowering2_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_input_stream(arg0 & 0xffffffff)
        lowering2_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline2 = wasmtime.Func(store, lowering2_ty, lowering2_callee, access_caller = True)
        def lowering3_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_output_stream(arg0 & 0xffffffff)
        lowering3_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline3 = wasmtime.Func(store, lowering3_ty, lowering3_callee, access_caller = True)
        def lowering4_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.types.drop_descriptor(arg0 & 0xffffffff)
        lowering4_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline4 = wasmtime.Func(store, lowering4_ty, lowering4_callee, access_caller = True)
        def lowering5_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdin.get_stdin()
            return _clamp(ret, 0, 4294967295)
        lowering5_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline5 = wasmtime.Func(store, lowering5_ty, lowering5_callee, access_caller = True)
        def lowering6_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_input.drop_terminal_input(arg0 & 0xffffffff)
        lowering6_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline6 = wasmtime.Func(store, lowering6_ty, lowering6_callee, access_caller = True)
        def lowering7_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdout.get_stdout()
            return _clamp(ret, 0, 4294967295)
        lowering7_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline7 = wasmtime.Func(store, lowering7_ty, lowering7_callee, access_caller = True)
        def lowering8_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_output.drop_terminal_output(arg0 & 0xffffffff)
        lowering8_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline8 = wasmtime.Func(store, lowering8_ty, lowering8_callee, access_caller = True)
        def lowering9_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stderr.get_stderr()
            return _clamp(ret, 0, 4294967295)
        lowering9_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline9 = wasmtime.Func(store, lowering9_ty, lowering9_callee, access_caller = True)
        def lowering10_callee(caller: wasmtime.Caller, arg0: int) -> None:
            expected: Result[None, None]
            if arg0 == 0:
                expected = Ok(None)
            elif arg0 == 1:
                expected = Err(None)
            else:
                raise TypeError("invalid variant discriminant for expected")
            import_object.exit.exit(expected)
        lowering10_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline10 = wasmtime.Func(store, lowering10_ty, lowering10_callee, access_caller = True)
        path = pathlib.Path(__file__).parent / ('root.core1.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance2 = wasmtime.Instance(store, module, [
            instance1["memory"],
            instance0["1"],
            trampoline0,
            instance0["2"],
            trampoline1,
            instance0["6"],
            instance0["12"],
            instance0["10"],
            instance0["11"],
            instance0["13"],
            instance0["8"],
            instance0["9"],
            instance1["cabi_realloc"],
            instance0["14"],
            instance0["15"],
            trampoline2,
            trampoline3,
            trampoline4,
            instance0["3"],
            instance0["4"],
            trampoline5,
            instance0["16"],
            trampoline6,
            trampoline7,
            instance0["17"],
            trampoline8,
            trampoline9,
            instance0["18"],
            trampoline10,
            instance0["5"],
            instance0["7"],
        ]).exports(store)
        def lowering11_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ptr = arg0
            len0 = arg1
            list = _decode_utf8(self._core_memory0, caller, ptr, len0)
            import_object.host.print(list)
        lowering11_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline11 = wasmtime.Func(store, lowering11_ty, lowering11_callee, access_caller = True)
        core_memory0 = instance1["memory"]
        assert(isinstance(core_memory0, wasmtime.Memory))
        self._core_memory0 = core_memory0
        def lowering12_callee(caller: wasmtime.Caller, arg0: int) -> None:
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
        lowering12_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline12 = wasmtime.Func(store, lowering12_ty, lowering12_callee, access_caller = True)
        realloc0 = instance2["cabi_import_realloc"]
        assert(isinstance(realloc0, wasmtime.Func))
        self._realloc0 = realloc0
        def lowering13_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.wall_clock.now()
            record = ret
            field = record.seconds
            field0 = record.nanoseconds
            _store(ctypes.c_uint64, self._core_memory0, caller, arg0, 0, _clamp(field, 0, 18446744073709551615))
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 8, _clamp(field0, 0, 4294967295))
        lowering13_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline13 = wasmtime.Func(store, lowering13_ty, lowering13_callee, access_caller = True)
        def lowering14_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int) -> None:
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
        lowering14_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i64(), wasmtime.ValType.i32(), ], [])
        trampoline14 = wasmtime.Func(store, lowering14_ty, lowering14_callee, access_caller = True)
        def lowering15_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
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
        lowering15_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline15 = wasmtime.Func(store, lowering15_ty, lowering15_callee, access_caller = True)
        def lowering16_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.types.get_flags(arg0 & 0xffffffff)
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
        lowering16_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline16 = wasmtime.Func(store, lowering16_ty, lowering16_callee, access_caller = True)
        def lowering17_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
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
        lowering17_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline17 = wasmtime.Func(store, lowering17_ty, lowering17_callee, access_caller = True)
        def lowering18_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None:
            ptr = arg2
            len0 = arg3
            list = _decode_utf8(self._core_memory0, caller, ptr, len0)
            ret = import_object.types.open_at(arg0 & 0xffffffff, types.PathFlags(arg1), list, types.OpenFlags(arg4), types.DescriptorFlags(arg5), types.Modes(arg6))
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg7, 0, 0)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg7, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(ret, Err):
                payload1 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg7, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg7, 4, (payload1).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering18_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline18 = wasmtime.Func(store, lowering18_ty, lowering18_callee, access_caller = True)
        def lowering19_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = _decode_utf8(self._core_memory0, caller, ptr, len0)
            ret = import_object.types.remove_directory_at(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
            elif isinstance(ret, Err):
                payload1 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 1, (payload1).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering19_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline19 = wasmtime.Func(store, lowering19_ty, lowering19_callee, access_caller = True)
        def lowering20_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = _decode_utf8(self._core_memory0, caller, ptr, len0)
            ret = import_object.types.unlink_file_at(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
            elif isinstance(ret, Err):
                payload1 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 1, (payload1).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering20_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline20 = wasmtime.Func(store, lowering20_ty, lowering20_callee, access_caller = True)
        def lowering21_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
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
        lowering21_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline21 = wasmtime.Func(store, lowering21_ty, lowering21_callee, access_caller = True)
        def lowering22_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
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
        lowering22_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline22 = wasmtime.Func(store, lowering22_ty, lowering22_callee, access_caller = True)
        def lowering23_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
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
        lowering23_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline23 = wasmtime.Func(store, lowering23_ty, lowering23_callee, access_caller = True)
        def lowering24_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
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
        lowering24_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline24 = wasmtime.Func(store, lowering24_ty, lowering24_callee, access_caller = True)
        def lowering25_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.environment.get_environment()
            vec = ret
            len5 = len(vec)
            result = self._realloc0(caller, 0, 0, 4, len5 * 16)
            assert(isinstance(result, int))
            for i6 in range(0, len5):
                e = vec[i6]
                base0 = result + i6 * 16
                (tuplei,tuplei1,) = e
                ptr, len2 = _encode_utf8(tuplei, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 4, len2)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 0, ptr)
                ptr3, len4 = _encode_utf8(tuplei1, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 12, len4)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 8, ptr3)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, len5)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 0, result)
        lowering25_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline25 = wasmtime.Func(store, lowering25_ty, lowering25_callee, access_caller = True)
        def lowering26_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.environment.get_arguments()
            vec = ret
            len2 = len(vec)
            result = self._realloc0(caller, 0, 0, 4, len2 * 8)
            assert(isinstance(result, int))
            for i3 in range(0, len2):
                e = vec[i3]
                base0 = result + i3 * 8
                ptr, len1 = _encode_utf8(e, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 4, len1)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 0, ptr)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, len2)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 0, result)
        lowering26_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline26 = wasmtime.Func(store, lowering26_ty, lowering26_callee, access_caller = True)
        def lowering27_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdin.get_terminal_stdin()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering27_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline27 = wasmtime.Func(store, lowering27_ty, lowering27_callee, access_caller = True)
        def lowering28_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdout.get_terminal_stdout()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering28_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline28 = wasmtime.Func(store, lowering28_ty, lowering28_callee, access_caller = True)
        def lowering29_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stderr.get_terminal_stderr()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering29_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline29 = wasmtime.Func(store, lowering29_ty, lowering29_callee, access_caller = True)
        path = pathlib.Path(__file__).parent / ('root.core3.wasm')
        module = wasmtime.Module.from_file(store.engine, path)
        instance3 = wasmtime.Instance(store, module, [
            trampoline11,
            trampoline12,
            trampoline13,
            trampoline14,
            trampoline15,
            trampoline16,
            trampoline17,
            trampoline18,
            trampoline19,
            trampoline20,
            trampoline21,
            trampoline22,
            trampoline23,
            trampoline24,
            trampoline25,
            trampoline26,
            trampoline27,
            trampoline28,
            trampoline29,
            instance2["fd_write"],
            instance2["clock_time_get"],
            instance2["args_sizes_get"],
            instance2["args_get"],
            instance2["environ_get"],
            instance2["environ_sizes_get"],
            instance2["fd_close"],
            instance2["fd_fdstat_get"],
            instance2["fd_prestat_get"],
            instance2["fd_prestat_dir_name"],
            instance2["path_open"],
            instance2["path_remove_directory"],
            instance2["path_unlink_file"],
            instance2["proc_exit"],
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
