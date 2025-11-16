import pytest

from mgimo.translate import Text, TranslationError, supported_languages


def test_show_language_list():
    assert supported_languages["vi"] == "vietnamese"


def test_run_translation_with_valid_input():
    text = Text("Hello", "en")
    translated_text = text.translate("es")
    assert "Hola" in translated_text.content


def test_run_detect_with_valid_text():
    result = Text("Hello world. This text is in English.").detect_language()
    assert result == "en"


def test_run_detect_hindi():
    result = Text("नमस्ते दुनिया। यह हिंदी में एक पाठ है।").detect_language()
    assert result == "hi"


def test_random_language_code():
    code = supported_languages.random()
    assert code in supported_languages


def test_unsupported_language_code():
    with pytest.raises(TranslationError):
        Text("Hello", "bzz")


def test_chain():
    text = Text("Hello", "en")
    languages = ["en", "es", "fr", "en"]
    chain = text.translate_chain(languages)
    assert len(chain) == 3
    assert chain[0].language == "es"
    assert chain[1].language == "fr"
    assert chain[2].language == "en"
