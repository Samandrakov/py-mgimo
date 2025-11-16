import random
from collections import UserDict

from deep_translator import GoogleTranslator


class LanguageDictionary(UserDict[str, str]):
    """Возвращает словарь поддерживаемых для перевода языков.
    Ключи словаря - коды языков в формате ISO 639-1,
    значения - названия языков на английском.
    """

    def __init__(self, data: dict[str, str] | None = None):
        if data is None:
            self.data = self.reverse(supported_languages_cached())
        else:
            self.data = data

    @staticmethod
    def reverse(d: dict[str, str]) -> dict[str, str]:
        return {v: k for k, v in d.items()}

    def filter(self, substring: str) -> dict[str, str]:
        substring = substring.lower()
        return LanguageDictionary(
            {
                k: v
                for k, v in self.items()
                if substring in k.lower() or substring in v.lower()
            }
        )

    def random(self) -> str:
        return random.choice(list(self.data.keys()))


def get_supported_languages() -> dict[str, str]:
    return GoogleTranslator().get_supported_languages(as_dict=True)


def supported_languages_cached() -> dict[str, str]:
    """Результат вызова `GoogleTranslator().get_supported_languages(as_dict=True)`
    в виде константы.
    """
    return {
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


supported_languages = LanguageDictionary()

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
