from mgimo.dataset.data import country_to_capital


def test_capital_cities():
    assert country_to_capital["Италия"] == "Рим"


def test_n_countries():
    assert len(country_to_capital) == 193
