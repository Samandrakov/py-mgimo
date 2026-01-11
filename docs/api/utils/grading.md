# Грейдинг

Модуль для конвертации оценок в буквенную шкалу МГИМО.

## Обзор

Этот модуль предоставляет функции для преобразования числовых оценок (от 0 до 100) в буквенную шкалу МГИМО (A-F), которая используется в университете.

## Шкала оценок МГИМО

| Баллы     | Буква | Описание    |
|-----------|-------|-------------|
| 90-100    | A     | Отлично     |
| 82-89     | B     | Очень хорошо|
| 75-81     | C     | Хорошо      |
| 67-74     | D     | Удовлетв.   |
| 60-66     | E     | Посредственно|
| 0-59      | F     | Неуд.       |

Подробнее: [https://mgimo.ru/study/akadrating/shkala.php](https://mgimo.ru/study/akadrating/shkala.php)

## Примеры использования

### Конвертация в буквенную оценку

```python
from mgimo.utils.grading import convert_to_letter

# Отличная оценка
grade = convert_to_letter(95)
print(grade)  # 'A'

# Хорошая оценка
grade = convert_to_letter(78)
print(grade)  # 'C'

# Неудовлетворительная оценка
grade = convert_to_letter(55)
print(grade)  # 'F'
```

### Получение Grade enum

```python
from mgimo.utils.grading import score_to_grade, Grade

# Получить enum Grade
grade = score_to_grade(85)
print(grade)  # Grade.B
print(grade.value)  # 'B'

# Сравнение оценок
if grade == Grade.B:
    print("Очень хорошо!")
```

### Обработка дробных оценок

```python
from mgimo.utils.grading import convert_to_letter

# Дробные оценки округляются
grade = convert_to_letter(89.5)
print(grade)  # 'A' (округлено до 90)

grade = convert_to_letter(89.4)
print(grade)  # 'B' (округлено до 89)
```

## API Reference

::: mgimo.utils.grading
