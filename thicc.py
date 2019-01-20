"""
thicc - Convert characters to their fullwidth representation
"""
__version__ = "0.0.1"
__author__ = "Tim Martin"
__licence__ = "MIT"

import argparse
import sys
import io

_widen = {
    " ": "　",
    "!": "！",
    '"': "＂",
    "#": "＃",
    "$": "＄",
    "%": "％",
    "&": "＆",
    "'": "＇",
    "(": "（",
    ")": "）",
    "*": "＊",
    "+": "＋",
    ",": "，",
    "-": "－",
    ".": "．",
    "/": "／",
    "0": "０",
    "1": "１",
    "2": "２",
    "3": "３",
    "4": "４",
    "5": "５",
    "6": "６",
    "7": "７",
    "8": "８",
    "9": "９",
    ":": "：",
    ";": "；",
    "<": "＜",
    "=": "＝",
    ">": "＞",
    "?": "？",
    "@": "＠",
    "A": "Ａ",
    "B": "Ｂ",
    "C": "Ｃ",
    "D": "Ｄ",
    "E": "Ｅ",
    "F": "Ｆ",
    "G": "Ｇ",
    "H": "Ｈ",
    "I": "Ｉ",
    "J": "Ｊ",
    "K": "Ｋ",
    "L": "Ｌ",
    "M": "Ｍ",
    "N": "Ｎ",
    "O": "Ｏ",
    "P": "Ｐ",
    "Q": "Ｑ",
    "R": "Ｒ",
    "S": "Ｓ",
    "T": "Ｔ",
    "U": "Ｕ",
    "V": "Ｖ",
    "W": "Ｗ",
    "X": "Ｘ",
    "Y": "Ｙ",
    "Z": "Ｚ",
    "[": "［",
    "\\": "＼",
    "]": "］",
    "^": "＾",
    "_": "＿",
    "`": "｀",
    "a": "ａ",
    "b": "ｂ",
    "c": "ｃ",
    "d": "ｄ",
    "e": "ｅ",
    "f": "ｆ",
    "g": "ｇ",
    "h": "ｈ",
    "i": "ｉ",
    "j": "ｊ",
    "k": "ｋ",
    "l": "ｌ",
    "m": "ｍ",
    "n": "ｎ",
    "o": "ｏ",
    "p": "ｐ",
    "q": "ｑ",
    "r": "ｒ",
    "s": "ｓ",
    "t": "ｔ",
    "u": "ｕ",
    "v": "ｖ",
    "w": "ｗ",
    "x": "ｘ",
    "y": "ｙ",
    "z": "ｚ",
    "{": "｛",
    "|": "｜",
    "}": "｝",
    "~": "～",
    "⦅": "｟",
    "⦆": "｠",
    "¢": "￠",
    "£": "￡",
    "¬": "￢",
    "¯": "￣",
    "¦": "￤",
    "¥": "￥",
    "₩": "￦",
}

_narrow = {value: key for key, value in _widen.items()}


class TextToFile(argparse.Action):
    def __call__(self, parser, namespace: argparse.Namespace, values, option_string=None):
        setattr(namespace, self.dest, io.StringIO(values))


def get_args(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert characters to their fullwidth representation if one exists."
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Instead, convert characters to their regular representation",
    )
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    if sys.stdin.isatty():
        # if its an interactive session, e.g. no piped in stuff
        parser.add_argument("text", action=TextToFile, help="The text to convert")
    args = parser.parse_args(args)
    if not sys.stdin.isatty():
        args.text = sys.stdin
    return args


def map_string(s, reverse=False):
    conversion_map = _narrow if reverse else _widen
    return "".join(conversion_map.get(c, c) for c in s)


def main():
    args = get_args()
    file = args.text if args.text else sys.stdin
    for line in file:
        sys.stdout.write(map_string(line, reverse=args.reverse))
    if sys.stdout.isatty():
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
