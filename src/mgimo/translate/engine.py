"""Модуль для перевода текста."""

import langdetect
from deep_translator import GoogleTranslator


def run_translation(
    text: str, source: str | None = None, target: str | None = None
) -> str:
    """Переводит предоставленный текст с одного языка на другой.

    Если язык источника `source` не указан, используется автоопределение языка.
    Если язык назначения `target` не указан, используется русский язык.
    """
    if not source:
        source = "auto"
    if not target:
        target = "ru"
    translator = GoogleTranslator(source=source, target=target)
    return translator.translate(text)


def run_detect(text: str) -> str:
    """Определяет язык предоставленного текста,
    возвращает код языка в формате [ISO 639-1][iso].

    Используется билиотека [langdetect][langdetect], поддерживаются 55 языков:

    ```
    af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
    hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
    pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
    ```

    [langdetect]: https://pypi.org/project/langdetect/
    [iso]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

    """
    return langdetect.detect(text)


def random_language_code() -> str:
    """Возвращает случайный код языка из списка поддерживаемых языков."""
    import random

    return random.choice(list(provided_languages.keys()))


_provided_languages = {
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "assamese": "as",
    "aymara": "ay",
    "azerbaijani": "az",
    "bambara": "bm",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bhojpuri": "bho",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "chichewa": "ny",
    "chinese (simplified)": "zh-CN",
    "chinese (traditional)": "zh-TW",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dhivehi": "dv",
    "dogri": "doi",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "ewe": "ee",
    "filipino": "tl",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "guarani": "gn",
    "gujarati": "gu",
    "haitian creole": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "iw",
    "hindi": "hi",
    "hmong": "hmn",
    "hungarian": "hu",
    "icelandic": "is",
    "igbo": "ig",
    "ilocano": "ilo",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "kinyarwanda": "rw",
    "konkani": "gom",
    "korean": "ko",
    "krio": "kri",
    "kurdish (kurmanji)": "ku",
    "kurdish (sorani)": "ckb",
    "kyrgyz": "ky",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lingala": "ln",
    "lithuanian": "lt",
    "luganda": "lg",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "maithili": "mai",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "meiteilon (manipuri)": "mni-Mtei",
    "mizo": "lus",
    "mongolian": "mn",
    "myanmar": "my",
    "nepali": "ne",
    "norwegian": "no",
    "odia (oriya)": "or",
    "oromo": "om",
    "pashto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "quechua": "qu",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "sanskrit": "sa",
    "scots gaelic": "gd",
    "sepedi": "nso",
    "serbian": "sr",
    "sesotho": "st",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "tatar": "tt",
    "telugu": "te",
    "thai": "th",
    "tigrinya": "ti",
    "tsonga": "ts",
    "turkish": "tr",
    "turkmen": "tk",
    "twi": "ak",
    "ukrainian": "uk",
    "urdu": "ur",
    "uyghur": "ug",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zulu": "zu",
}

provided_languages = {v: k for k, v in _provided_languages.items()}


def provided_languages_from_source() -> dict[str, str]:
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
