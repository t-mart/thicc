import argparse
import sys
import io

narrow = {
    " ": "　",
    "!": "！",
    "\"": "＂",
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

wide = {value: key for key, value in narrow.items()}


def get_or_passthru(key, map):
    try:
        return map[key]
    except KeyError:
        return key


parser = argparse.ArgumentParser(
    description="Convert characters to their fullwidth representation if one exists.",
)
parser.add_argument(
    '-r', '--reverse',
    action='store_true',
    help="Instead, convert characters to their regular representation",
)
parser.add_argument(
    '-t', '--text',
    help="The text to convert",
)

def main():
    args = parser.parse_args()
    conversion_map = wide if args.reverse else narrow
    file = io.StringIO(args.text) if args.text else sys.stdin
    for line in file:
        sys.stdout.write("".join(get_or_passthru(c, conversion_map) for c in line))
    if sys.stdout.isatty():
        sys.stdout.write("\n")


if __name__ == '__main__':
    main()


