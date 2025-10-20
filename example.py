from random import choice

from mgimo.data import country_to_capital
from mgimo.grading import convert_to_letter
from mgimo.logging import Mark, Transcript

countries = list(country_to_capital.keys())
assert len(countries) == 193
country = choice(countries)
city = country_to_capital[country]
print(f"Выбрана страна: {country}, столица - {city}.")


Mark("это было простое задание").score(19, out_of=20).save("1.json")
Mark("это было задание посложнее").score(8, out_of=10).save("2.json")
t = Transcript()
t.register("1.json")
t.register("2.json")
p = t.summary.percent
print(convert_to_letter(p), p)  # A 90
