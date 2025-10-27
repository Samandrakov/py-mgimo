from mgimo.utils.grading import Grade, convert_to_letter, score_to_grade


def test_letter_converts_to_string():
    assert Grade.E.value == "E"


def test_converts_to_A_grade():
    assert convert_to_letter(95) == "A"


def test_rounding_goes_to_higher_grade():
    assert score_to_grade(66.9) == Grade.D
