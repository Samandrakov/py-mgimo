# Логирование

Модуль для отслеживания и оценки выполнения заданий.

## Обзор

Этот модуль предоставляет классы для оценки и учета результатов выполнения заданий. Он позволяет сохранять оценки в файлы JSON и агрегировать результаты из нескольких заданий.

## Основные классы

- **Mark** - оценка за отдельное задание
- **Transcript** - набор выполненных заданий

## Примеры использования

### Создание и сохранение оценки

```python
from mgimo.utils.logging import Mark

# Создать оценку за задание
mark = Mark("Простое задание")
mark.score(19, out_of=20)
mark.save("task1.json")

# Создать оценку с комментарием
mark = Mark("Сложное задание")
mark.score(8, out_of=10)
mark.comment("Отличная работа!")
mark.save("task2.json")
```

### Использование цепочки вызовов

```python
from mgimo.utils.logging import Mark

# Все методы возвращают self для цепочки вызовов
Mark("Задание с данными") \
    .score(15, out_of=20) \
    .comment("Нужно больше внимания к деталям") \
    .attach({"details": "some data"}) \
    .save("task3.json")
```

### Загрузка оценки из файла

```python
from mgimo.utils.logging import Mark

# Загрузить оценку
mark = Mark.load("task1.json")
print(f"{mark.title}: {mark.points}/{mark.out_of} ({mark.percent}%)")
```

### Работа с транскриптом

```python
from mgimo.utils.logging import Mark, Transcript

# Создать несколько оценок
Mark("Задание 1").score(19, out_of=20).save("1.json")
Mark("Задание 2").score(8, out_of=10).save("2.json")
Mark("Задание 3").score(45, out_of=50).save("3.json")

# Создать транскрипт
transcript = Transcript()
transcript.register("1.json")
transcript.register("2.json")
transcript.register("3.json")

# Получить суммарную оценку
summary = transcript.summary
print(f"Итого: {summary.points}/{summary.out_of} ({summary.percent}%)")
```

### Добавление дополнительных данных

```python
from mgimo.utils.logging import Mark

mark = Mark("Анализ данных")
mark.score(18, out_of=20)

# Прикрепить данные в формате JSON
mark.attach({"dataset": "countries.csv", "rows": 193})
mark.attach({"method": "analysis", "result": "successful"})

mark.save("analysis.json")
```

### Получение всех комментариев

```python
from mgimo.utils.logging import Transcript

transcript = Transcript()
transcript.register("1.json")
transcript.register("2.json")
transcript.register("3.json")

# Получить все комментарии
notes = transcript.notes
for note in notes:
    if note:
        print(f"- {note}")
```

## Формат JSON файла

Пример содержимого сохраненного файла:

```json
{
  "title": "Простое задание",
  "points": 19,
  "out_of": 20,
  "note": "Хорошая работа",
  "payload": [],
  "iso_timestamp": "2024-01-15T10:30:45.123456"
}
```

## API Reference

::: mgimo.utils.logging
