"""MGIMO command line magic and datasets.

Usage:
  mgimo quiz [--capitals=n] [--countries=k]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
"""

from docopt import docopt

from mgimo.quiz.capitals import run

__version__ = "0.5.0"

# todo: Добавить dataset, translate


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


if __name__ == "__main__":
    main()
