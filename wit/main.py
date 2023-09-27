from pyconvert import Root, RootImports, imports
from wasmtime import Store


class Host(imports.Host):
    def print(self, s: str):
        print(s + "test")


def main():
    store = Store()
    demo = Root(
        store,
        RootImports(
            Host(), None, None, None, None, None, None, None, None, None, None, None
        ),
    )
    demo.exec(store)


if __name__ == "__main__":
    main()
