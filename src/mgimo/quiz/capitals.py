"""Тест по столицам мира.

Выполним тест на знание столиц мира - мы будем выбирать случайный город или
страну, создадим несколько вариантов ответов, перечислим эти варианты
в случайном порядке и спросим у пользователя правильный ответ.
Тест можно запустить несколько раз и указать в конце количество верных
и неверных ответов.

Вопросы и ответы могут выглядеть примерно так:

```
Джорджтаун - это столица какой страны?
 1 Камбоджа
 2 Малави
 3 Демократическая Республика Конго
 4 Гайана
Введите номер ответа (1-4) и нажмите [Enter]: 2
Неверно. Правильный ответ: Гайана

Любляна - это столица какой страны?
 1 Словения
 2 Зимбабве
 3 Гаити
 4 Бахрейн
Введите номер ответа (1-4) и нажмите [Enter]: 1
Верно!
```
"""

from random import choice, sample, shuffle

from mgimo.dataset.data import country_to_capital

city_dict = {v: k for k, v in country_to_capital.items()}


def ask_user(question: str, correct: str, incorrect: list[str]) -> bool:
    options = incorrect + [correct]
    shuffle(options)
    n = len(options)
    print(question)
    # перечисляем варианты
    for i, option in enumerate(options, 1):
        print(f"  {i}", option)
    answer = input(f"Введите номер ответа (1-{n}) и нажмите [Enter]: ")
    # проверяем введены ли допустимые цифры
    allowed = [str(i) for i in range(1, n + 1)]
    if answer not in allowed:
        print("Такого варианта ответа не предусмотрено.")
        return False
    # переходим к нумерации с нуля
    k = int(answer) - 1
    # проверяем ответ верный или нет
    if options[k] == correct:
        print("Верно!")
        return True
    else:
        print("Неверно. Правильный ответ:", correct)
        return False


def ask_about_capital(country, n=4):
    city = country_to_capital[country]
    options = [text for text in country_to_capital.keys() if text != country]
    incorrect = sample(options, n - 1)
    question = f"\n{city} - это столица какой страны?"
    return ask_user(question, country, incorrect)


def prepare_incorrect_options(k, options, correct):
    incorrect = [text for text in options if text != correct]
    return sample(incorrect, k)


def ask_about_country(city, n=4):
    country = city_dict[city]
    incorrect = prepare_incorrect_options(n - 1, city_dict.keys(), country)
    question = f"\nУкажите столицу страны {country}:"
    return ask_user(question, city, incorrect)


def run(n_capitals=2, n_countries=2):
    countries = list(country_to_capital.keys())
    capitals = list(country_to_capital.values())
    n_success = 0
    for _ in range(n_capitals):
        country = choice(countries)
        result = ask_about_capital(country)
        if result:
            n_success += 1
    for _ in range(n_countries):
        city = choice(capitals)
        result = ask_about_country(city)
        if result:
            n_success += 1
    ratio = int(round(n_success / (n_capitals + n_countries) * 100))
    print("Верных ответов:", n_success, "из", n_capitals + n_countries, f"({ratio}%).")
