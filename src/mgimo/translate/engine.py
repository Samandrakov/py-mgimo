"""Модуль для перевода текста."""

import langdetect
from deep_translator import GoogleTranslator


def run_translation(
    text: str, source: str | None = None, target: str | None = None
) -> str:
    """Переводит предоставленный текст с одного языка на другой.
    Если язык источника не указан, используется автоопределение языка.
    Если язык назначения не указан, используется русский.
    """
    if not source:
        source = "auto"
    if not target:
        target = "ru"
    translator = GoogleTranslator(source=source, target=target)
    return translator.translate(text)


def run_detect(text: str) -> str:
    """Определяет язык предоставленного текста, возвращает код языка в формате ISO 639-1."""
    return langdetect.detect(text)


def provide_languages() -> dict[str, str]:
    """Возвращает словарь поддерживаемых для перевода языков.
    Ключи словаря - названия языков на английском, значения - коды языков в формате ISO 639-1.
    """
    return GoogleTranslator().get_supported_languages(as_dict=True)


# Примеры предложений
sentences = {
    "hausa": {
        "code": "ha",
        "sentence": "Da sanyin safiya, yakan sha shayi mai yawa kafin ya fita noma a cikin rana.",
        "translation": "In the cool of the morning, he usually drinks a lot of tea before going out to farm in the sun.",
    },
    "hawaiian": {
        "code": "haw",
        "sentence": "Ke kūkulu nei mākou i ke ala loa no ka hoʻolauleʻa o ka lā hānau o ke kupuna.",
        "translation": "We are setting up the long tables for the celebration of our grandparent's birthday.",
    },
    "hebrew": {
        "code": "iw",
        "sentence": "אימא שלי תמיד אומרת, 'תרד מהטלפון שלך ותסדר כבר את החדר!'",
        "translation": "My mom always says, 'Get off your phone and clean your room already!'",
    },
    "hindi": {
        "code": "hi",
        "sentence": "दफ़्तर जाने की जल्दी में, मैंने बस एक कप चाय पी और दो बिस्कुट खाए।",
        "translation": "In a hurry to get to the office, I just drank one cup of tea and ate two biscuits.",
    },
    "hmong": {
        "code": "hmn",
        "sentence": "Tub nkeeg nrhiav tau ib cev viav txim los tshuaj nws tus menyuam uas mob.",
        "translation": "The shaman found a special herb to medicine his sick child.",
    },
    "hungarian": {
        "code": "hu",
        "sentence": "A nagymamám mindig extra sót tesz a babgulyásba, azt mondja, hogy így lesz igazán finom.",
        "translation": "My grandmother always puts extra salt in the bean goulash; she says that's how it becomes truly delicious.",
    },
}
