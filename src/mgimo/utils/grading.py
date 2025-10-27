from enum import Enum


class Grade(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


def convert_to_letter(score: int | float) -> str:
    """Перевести оценку в баллах от до 100 в буквенную шкалу A-E.
    Подробнее: <https://mgimo.ru/study/akadrating/shkala.php>
    """
    return score_to_grade(score).value


def score_to_grade(score: int | float) -> Grade:
    score = round(score)
    if score >= 90:
        return Grade.A
    if score >= 82:
        return Grade.B
    if score >= 75:
        return Grade.C
    if score >= 67:
        return Grade.D
    if score >= 60:
        return Grade.E
    return Grade.F
