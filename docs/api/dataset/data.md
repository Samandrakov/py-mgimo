# Данные: Страны и столицы

Модуль с данными о странах-членах ООН и их столицах.

## Обзор

Этот модуль предоставляет словарь с названиями 193 стран-членов ООН и их столицами на русском языке.

## Структура данных

### country_to_capital

Словарь, содержащий соответствие стран и столиц:

```python
country_to_capital = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    # ... всего 193 страны
}
```

## Примеры использования

### Получение столицы страны

```python
from mgimo.dataset.data import country_to_capital

# Получить столицу
capital = country_to_capital["Россия"]
print(capital)  # "Москва"

capital = country_to_capital["Япония"]
print(capital)  # "Токио"
```

### Проверка наличия страны

```python
from mgimo.dataset.data import country_to_capital

country = "Франция"
if country in country_to_capital:
    print(f"Столица {country}: {country_to_capital[country]}")
```

### Получение списка всех стран

```python
from mgimo.dataset.data import country_to_capital

countries = list(country_to_capital.keys())
print(f"Всего стран: {len(countries)}")  # 193
print("Первые 5 стран:", countries[:5])
```

### Получение списка всех столиц

```python
from mgimo.dataset.data import country_to_capital

capitals = list(country_to_capital.values())
print(f"Всего столиц: {len(capitals)}")  # 193
print("Первые 5 столиц:", capitals[:5])
```

### Создание обратного словаря (столица -> страна)

```python
from mgimo.dataset.data import country_to_capital

capital_to_country = {v: k for k, v in country_to_capital.items()}

# Найти страну по столице
country = capital_to_country["Москва"]
print(country)  # "Россия"
```

### Случайный выбор страны

```python
from random import choice
from mgimo.dataset.data import country_to_capital

countries = list(country_to_capital.keys())
random_country = choice(countries)
capital = country_to_capital[random_country]

print(f"Страна: {random_country}")
print(f"Столица: {capital}")
```

### Поиск стран по части названия

```python
from mgimo.dataset.data import country_to_capital

search_term = "Республика"
matching_countries = [
    country for country in country_to_capital.keys()
    if search_term in country
]

print(f"Найдено стран: {len(matching_countries)}")
for country in matching_countries:
    print(f"- {country}: {country_to_capital[country]}")
```

### Создание DataFrame для анализа

```python
import pandas as pd
from mgimo.dataset.data import country_to_capital

# Создать DataFrame
df = pd.DataFrame(
    list(country_to_capital.items()),
    columns=['Страна', 'Столица']
)

print(df.head())
print(f"\nВсего записей: {len(df)}")
```

## Примечания

- Все названия на русском языке
- Словарь содержит 193 страны-члена ООН
- Используется для тестов и обучающих игр
- Данные актуальны на момент версии 0.5.0

## Примеры стран

Вот некоторые страны из словаря:

| Страна | Столица |
|--------|---------|
| Россия | Москва |
| Соединенные Штаты Америки | Вашингтон |
| Китай | Пекин |
| Япония | Токио |
| Германия | Берлин |
| Франция | Париж |
| Великобритания | Лондон |
| Италия | Рим |
| Канада | Оттава |
| Австралия | Канберра |

## API Reference

::: mgimo.dataset.data
