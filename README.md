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
$ thc --text "bar multiple words"
```
```
ｂａｒ
```

Reverse fullwidth text:
```bash
$ thc -r -t "ｂａｚ"
```
```
baz
```

## Installation
```bash
pip install --upgrade "git+https://github.com/t-mart/thicc"
```
