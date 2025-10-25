"""My Awesome CLI Tool

Usage:
  cli.py quiz [--city]
  cli.py --version
  cli.py --help

Options:
  -h --help       Show this screen
  --version       Show version
  -c --city       City quiz mode
"""

from docopt import docopt
from city_quiz import city_main
import os

__version__ = "1.0.0"

def cmd_quiz(args):
    """Обработчик команды quiz"""
    city_mode = args['--city']
    print("✅ Starting quiz...")

    if city_mode:
        city_main()
    else:
        print("Режим по умолчанию")
        city_main()

def main():
    args = docopt(__doc__, version=__version__)

    try:
        if args['quiz']:
            cmd_quiz(args)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()