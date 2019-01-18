# fullwidth

## Usage Examples

Pipe in text:
```bash
$ echo "foo" | fw
```
```
ｆｏｏ
```

Pass text in as an argument:
```bash
$ fw --text "bar multiple words"
```
```
ｂａｒ
```

Reverse fullwidth text:
```bash
$ fw -r -t "ｂａｚ"
```
```
baz
```

## Installation
```bash
pip install --upgrade "git+https://github.com/t-mart/fw"
```
