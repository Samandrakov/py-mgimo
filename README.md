# Программные утилиты и данные МГИМО

![PyPI - Version](https://img.shields.io/pypi/v/mgimo)

## Установка

```console
pip install mgimo
```

## Использование

Примеры использования приведены также в [example.py](example.py).

### Столицы стран-членов ООН 

```python
from random import choice

from mgimo.data import country_to_capital

countries = list(country_to_capital.keys())
assert len(countries) == 193
country = choice(countries)
city = country_to_capital[country]
print(f"Выбрана страна: {country}, столица - {city}.")
```
