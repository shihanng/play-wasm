import json

import wasmtime.bindgen
from pyconvert import Root, RootImports, imports
from wasmtime import Store


class Host(imports.Host):
    def print(self, s: str):
        print(s + "test")


class HostEnvironment:
    def get_environment(self):
        return [("TMPDIR", "/tmp2/")]


class HostPreopens:
    def get_directories(self):
        return []


def main():
    store = Store()
    demo = Root(
        store,
        RootImports(
            Host(),
            None,
            None,
            None,
            None,
            HostPreopens(),
            HostEnvironment(),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ),
    )
    data = {"key": "value"}
    json_str = json.dumps(data)
    json_bytes = json_str.encode("utf-8")
    res = demo.exec(store, json_bytes)
    print(res.decode("utf-8"))


if __name__ == "__main__":
    main()
