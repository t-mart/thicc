# thicc

Convert characters to their fullwidth representation

## Usage Examples

Pipe in text:
```bash
$ echo "foo" | thc
```
```
ｆｏｏ
```

Pass text in as an argument:
```bash
$ thc <(echo bar)
```
```
ｂａｒ
```

Reverse fullwidth text:
```bash
$ thc -r <(echo "ｂａｚ")
```
```
baz
```

## Installation
```bash
pip install --upgrade "git+https://github.com/t-mart/thicc"
```
