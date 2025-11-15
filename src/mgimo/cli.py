"""MGIMO command line tools and datasets.

Usage:
  mgimo quiz [--capitals=n] [--countries=k]
  mgimo translate <text> [--from=src] [--to=dst]
  mgimo translate <text> --detect
  mgimo translate --list [--json]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
"""
import sys

from docopt import docopt

from mgimo.quiz.capitals import run

__version__ = "0.5.0"

# todo: Добавить dataset


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
        if args["--detect"]:
            # from mgimo.translate import run_detect
            # _ = run_detect(text=args["<text>"])
            sys.exit("Language detection is not supported.")
        elif args["--list"]:
            from mgimo.translate import provide_languages

            lang_dict = provide_languages()
            if args["--json"]:
                import json

                print(json.dumps(lang_dict, ensure_ascii=False, indent=2))
            else:
                for language, code in lang_dict.items():
                    print(f"{code}: {language}")
        else:
            from mgimo.translate import run_translation

            answer = run_translation(
                text=args["<text>"], source=args["--from"], target=args["--to"]
            )
            print(answer)


if __name__ == "__main__":
    main()
