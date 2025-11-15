import pytest

from mgimo.translate import provide_languages, run_detect, run_translation


def test_run_translation_with_valid_input():
    result = run_translation("Hello", "en", "es")
    assert "Hola" in result


@pytest.mark.skip(reason="Language detection not supported.")
def test_run_detect_with_valid_text():
    result = run_detect("Hello world. This text is in English.")
    assert result == "en"


@pytest.mark.skip(reason="Language detection not supported.")
def test_run_detect_hindi():
    result = run_detect("नमस्ते दुनिया")
    assert result == "hi"


def test_show_list():
    result = provide_languages()
    assert result["vietnamese"] == "vi"
