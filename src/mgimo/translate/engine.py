"""Модуль для перевода текста."""

from deep_translator import GoogleTranslator


def run_translation(text: str, source: str | None = None, target: str = "ru") -> str:
    return f"Doing translation: {text}, {source}, {target}"


def run_detect(text: str) -> str:
    return f"Detecting language for: {text}"


def provide_languages() -> dict[str, str]:
    return GoogleTranslator().get_supported_languages(as_dict=True)
