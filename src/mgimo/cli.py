"""MGIMO command line tools and datasets.

Usage:
  mgimo quiz [--capitals=n] [--countries=k]
  mgimo translate <text> [--from=source] [--to=target] [--roundtrip]
  mgimo translate <text> --chain=code1,code2,codeN
  mgimo translate <text> --detect
  mgimo translate --list [--search=str] [--json]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
"""

import json

from docopt import docopt

from mgimo.quiz.capitals import run
from mgimo.translate import (
    provided_languages,
    run_detect,
    random_language_code,
    run_translation,
)

__version__ = "0.6.0"

# todo: Добавить dataset


def filter_dict(mapping, term):
    term = term.lower()
    return {
        code: lang
        for code, lang in mapping.items()
        if term in lang.lower() or term in code.lower()
    }


def prints(code, text):
    lang = provided_languages[code]
    print(f"{code} ({lang}): {text}")


def dispatch_translate(args):
    if args["--detect"]:
        answer = run_detect(text=args["<text>"])
        print(answer)
    elif args["--list"]:
        lang_dict = provided_languages
        if args["--search"]:
            lang_dict = filter_dict(provided_languages, args["--search"])
        if args["--json"]:
            print(json.dumps(lang_dict, ensure_ascii=False, indent=2))
        else:
            for code, language in lang_dict.items():
                print(f"{code}: {language}")
    elif args["--chain"]:
            languages = args["--chain"].split(",")
            current_text = args["<text>"]
            current_source = languages[0]
            prints(current_source, current_text)
            for lang in languages[1:]:
                translated_text = run_translation(current_text, current_source, lang)
                prints(lang, translated_text)
                current_text = translated_text
                current_source = lang
    else:
        if args["--to"] == "random":
            args["--to"] = random_language_code()
        dst = args["--to"] or "ru"
        src = args["--from"] or "auto"
        text = args["<text>"]
        answer_1 = run_translation(text, source=src, target=dst)
        if args["--roundtrip"]:
            answer_2 = run_translation(text=answer_1, source=dst, target=src)
            print(f"{src}: {text}")
            prints(dst, answer_1)
            print(f"{src}: {answer_2}")
        else:
            prints(dst, answer_1)


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
