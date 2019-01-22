"""
thicc - Convert characters to their fullwidth representation
"""
__version__ = "0.0.2"
__author__ = "Tim Martin"
__licence__ = "MIT"

import argparse
import sys

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


def get_args(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert characters to their fullwidth representation if one exists."
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Instead, convert characters to their regular representation.",
    )
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument(
        'file',
        nargs='?',
        type=argparse.FileType(mode='rb', encoding='utf8'),
        default=sys.stdin,
        metavar='filename',
        help="The file to convert. If omitted, standard input is read instead."
    )
    args = parser.parse_args(args)
    return args


def map_string(s, reverse=False):
    conversion_map = _narrow if reverse else _widen
    return "".join(conversion_map.get(c, c) for c in s)


def main():
    args = get_args()
    for line in args.file:
        sys.stdout.write(map_string(line, reverse=args.reverse))
    if sys.stdout.isatty():
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
