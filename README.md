```go
GOOS=wasip1 GOARCH=wasm go build -o main.wasm main.go
tinygo build -o main.wasm -target=wasi main.go
```
