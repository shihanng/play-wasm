package main

import (
	"os"

	gen "github.com/shihanng/play-wasm/wit/gen"
)

func init() {
	a := HostImpl{}
	gen.SetConvert(a)
}

type HostImpl struct{}

func (e HostImpl) Exec(input []uint8) []uint8 {
	res := []byte(input)
	res = append(res, "hello from exec"...)

	gen.ConvertPrint(string(res))

	tmpFile, err := os.CreateTemp("", "test_")
	if err != nil {
		// Print for debug
		return []byte(err.Error() + ": create temp")
	}

	defer tmpFile.Close()
	defer os.Remove(tmpFile.Name())

	if _, err := tmpFile.Write(res); err != nil {
		// Print for debug
		return []byte(err.Error() + ": write")
	}

	return []byte(res)
}

//go:generate wit-bindgen tiny-go . --out-dir=gen
func main() {}

/*
tinygo build -target=wasi -o main.wasm main.go
wasm-tools component embed --world convert . main.wasm -o main.embed.wasm
wasm-tools component new main.embed.wasm --adapt wasi_snapshot_preview1.reactor.wasm -o main.component.wasm
python -m wasmtime.bindgen main.component.wasm --out-dir pyconvert
*/
