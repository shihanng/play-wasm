from wasmtime import Engine, Linker, Module, Store, WasiConfig

engine = Engine()
store = Store(engine)
wasi = WasiConfig()
wasi.inherit_argv()
wasi.inherit_env()
wasi.inherit_stdout()
wasi.inherit_stderr()
wasi.inherit_stdin()
store.set_wasi(wasi)
linker = Linker(engine)
linker.define_wasi()
module = Module.from_file(store.engine, "main.wasm")
linking1 = linker.instantiate(store, module)
start = linking1.exports(store).get("") or linking1.exports(store)["_start"]
start(store)
