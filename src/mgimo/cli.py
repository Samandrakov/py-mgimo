"""My Awesome CLI Tool

Usage:
  mgimo quiz [--city]
  mgimo --version
  mgimo --help

Options:
  -h --help       Show this screen
  --version       Show version
  -c --capital       City quiz mode
"""

from docopt import docopt
from mgimo.quiz.capital_quiz import city_main

__version__ = "1.0.0"

def cmd_quiz(args):
    """Обработчик команды quiz"""
    city_mode = args['--capital']
    print("Starting capital quiz...")
#todo Добавить количество вопросов
    if city_mode:
        city_main()
    else:
        print("Режим по умолчанию - Тест по столицам мира, количество вопросов - 4")
#todo Добавить dataset, translate

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