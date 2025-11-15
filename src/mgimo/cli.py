"""MGIMO command line tools and datasets.

Usage:
  mgimo quiz [--capitals=n] [--countries=k]
  mgimo translate <text> [--from=src] [--to=dst | --to-random] [--roundtrip]
  mgimo translate <text> --detect
  mgimo translate --list [--search=str] [--json]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
"""

from docopt import docopt

from mgimo.quiz.capitals import run
from mgimo.translate.engine import provided_languages

__version__ = "0.6.0"

# todo: Добавить dataset


def dispatch_translate(args):
    if args["--detect"]:
        from mgimo.translate import run_detect

        answer = run_detect(text=args["<text>"])
        print(answer)
    elif args["--list"]:
        lang_dict = provided_languages
        if args["--search"]:
            search_str = args["--search"].lower()
            lang_dict = {
                code: lang
                for code, lang in provided_languages.items()
                if search_str in lang.lower() or search_str in code.lower()
            }

        if args["--json"]:
            import json

            print(json.dumps(lang_dict, ensure_ascii=False, indent=2))
        else:
            for code, language in lang_dict.items():
                print(f"{code}: {language}")
    else:
        from mgimo.translate import run_translation

        if args["--to-random"]:
            from mgimo.translate.engine import random_language_code

            dst = random_language_code()
        else:
            dst = args["--to"] or "ru"
        src = args["--from"] or "auto"
        text = args["<text>"]
        answer_1 = run_translation(text, source=src, target=dst)
        if args["--roundtrip"]:
            answer_2 = run_translation(text=answer_1, source=dst, target=src)
            print(f"{src}: {text}")
            print(f"{dst} ({provided_languages[dst]}): {answer_1}")
            print(f"{src}: {answer_2}")
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
