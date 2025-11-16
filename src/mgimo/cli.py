"""MGIMO command line tools and datasets.

Usage:
  mgimo quiz [--capitals=n] [--countries=k]
  mgimo translate <text> [--from=source] [--to=target] [--roundtrip]
  mgimo translate <text> --chain=code1,code2,codeN
  mgimo translate <text> --detect
  mgimo translate --list [--contains=str] [--json]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
"""

import json

from docopt import docopt

from mgimo.quiz.capitals import run
from mgimo.translate import Text, supported_languages

__version__ = "0.6.0"

# todo: Добавить dataset


def dispatch_translate(args):
    def get_text(args) -> Text:
        if not args["<text>"]:
            content = input("Enter text: ")
            return Text(content)
        else:
            return Text(args["<text>"])

    if args["--detect"]:
        t = get_text(args)
        answer = t.detect_language()
        print(answer)
    elif args["--list"]:
        lang_dict = supported_languages
        if substring := args["--contains"]:
            lang_dict = supported_languages.filter(substring)
        if args["--json"]:
            print(json.dumps(lang_dict, ensure_ascii=False, indent=2))
        else:
            for code, language in lang_dict.items():
                print(f"{code}: {language}")
    elif args["--chain"]:
        languages = args["--chain"].split(",")
        t = Text(args["<text>"], languages[0])
        print(t)
        text_items = t.translate_chain(languages)
        for ti in text_items:
            print(ti)
    else:
        t = get_text(args)
        source_language = args["--from"] or "auto"
        t = Text(args["<text>"], source_language)
        if args["--to"] == "random":
            dst = supported_languages.random()
        elif args["--to"]:
            dst = args["--to"]
        else:
            dst = "ru"
        answer_1 = t.translate(dst)
        if args["--roundtrip"]:
            answer_2 = answer_1.translate(source_language)
            print(t)
            print(answer_1)
            print(answer_2)
        else:
            print(answer_1)


def main():
    args = docopt(__doc__, version=__version__)
    if args["quiz"]:
        k = args["--countries"]
        n = args["--capitals"]
        if n is None and k is None:
            n = 2
            k = 2
        n = int(n) if n else 0
        k = int(k) if k else 0
        run(n_capitals=n, n_countries=k)
    if args["translate"]:
        dispatch_translate(args)


if __name__ == "__main__":
    main()
