"""Модуль для перевода текста."""

from dataclasses import dataclass

import langdetect
from deep_translator import GoogleTranslator

from .constants import supported_languages


class TranslationError(Exception):
    """Исключение, возникающее при ошибке перевода."""

    pass


@dataclass
class Text:
    content: str
    language: str = "auto"

    def __post_init__(self):
        if self.language != "auto" and self.language not in supported_languages:
            raise TranslationError(f"Unsupported language code: {self.language}")

    def __str__(self):
        lang_name = supported_languages.get(self.language, self.language)
        return self.language + " (" + lang_name + "): " + self.content

    def translate(self, target_language: str) -> "Text":
        translator = GoogleTranslator(source=self.language, target=target_language)
        translated_content = translator.translate(self.content)
        return Text(content=translated_content, language=target_language)

    def translate_to_random(self) -> "Text":
        target_language = supported_languages.random()
        return self.translate(target_language)

    def translate_roundtrip(self, target_language: str) -> tuple["Text", "Text"]:
        translated = self.translate(target_language)
        roundtrip = translated.translate(self.language)
        return translated, roundtrip

    def translate_chain(self, languages: list[str]) -> list["Text"]:
        if self.language != languages[0]:
            raise TranslationError("Chain must start with origitnal text language.")
        current_text = self
        results = []
        for lang in languages[1:]:
            current_text = current_text.translate(lang)
            results.append(current_text)
        return results

    def detect_language(self) -> str:
        return langdetect.detect(self.content)
