package main

import (
	gen "github.com/shihanng/play-wasm/wit/gen"
)

func init() {
	a := HostImpl{}
	gen.SetConvert(a)
}

type HostImpl struct{}

func (e HostImpl) Exec(input []uint8) []uint8 {
	res := "Hellou, world!" + string([]byte(input))
	gen.ConvertPrint("Hellou, world!" + string([]byte(input)))
	return []byte(res)
}

//go:generate wit-bindgen tiny-go . --out-dir=gen
func main() {}

// tinygo build -target=wasi -o main.wasm main.go
// wasm-tools component embed --world convert . main.wasm -o main.embed.wasm
// wasm-tools component new main.embed.wasm --adapt wasi_snapshot_preview1.reactor.wasm -o main.component.wasm
