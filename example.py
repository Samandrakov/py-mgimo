from random import choice

from mgimo.dataset.data import country_to_capital
from mgimo.utils.grading import convert_to_letter

countries = list(country_to_capital.keys())
assert len(countries) == 193
country = choice(countries)
city = country_to_capital[country]
print(f"Выбрана страна: {country}, столица - {city}.")

p = 90
print(convert_to_letter(p), p)  # A 90
