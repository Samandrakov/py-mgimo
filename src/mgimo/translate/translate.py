"""Перевод текста с одного языка на другой.

Модуль предназначен для перевода текста с одного естественного языка на другой.
При переводе могут быть заданы язык с которого переводим и язык на который переводим.
Также может быть задана модель (или сервис) с использованием которой будет
производится перевод.
Если языки, задающие направление перевода, и модель не указаны будет выполнен перевод
введенного текста на английский язык.

Пример перевода введенного текста:

```
Привет, как дела?
Hi, how are you?
```
"""


from deep_translator import GoogleTranslator


def translate_google(text, lang_src="auto", lang_to="en"):

    translator = GoogleTranslator(source=lang_src, target=lang_to)
    translated_text = translator.translate(text=text)

    return translated_text


def run(text, lang_src="auto", lang_to="en", engine="google"):

    if not text:
        print("Введите текст для перевода.")
    
    if not lang_src:
        lang_src = "auto"
    if not lang_to:
        lang_to = "en"
    if not engine:
        engine = "google"

    translated_text = ""
    match engine:
        case "google":
            translated_text = translate_google(text, lang_src, lang_to)
        case _:
            translated_text = translate_google(text, lang_src, lang_to)

    print(f"Перевод: {translated_text}")
