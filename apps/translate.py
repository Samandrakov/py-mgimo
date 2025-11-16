from random import choice
import streamlit as st
from mgimo.translate import Text, supported_languages, TranslationError

# add extra pages

starting_texts = [
    """До чего дошел прогресс
Труд физический исчез
Да и умственный заменит
Механический процесс""",
    """Позабыты хлопоты
Останoвлен бег
Вкалывают роботы
А не человек""",
    """Чтобы цифровые двойники выглядели правдоподобно, все члены квартета на протяжении пяти недель приходили в съемочный павильон в Стокгольме. 
Там их обвешивали датчиками, чтобы зафиксировать мимику, пластику и характерные движения при помощи 160 камер с помощью технологии motion capture.
""",
    """Права человека будут находиться в центре подхода ПРООН к цифровизации, так
как цифровые технологии все чаще становятся неотъемлемой частью всех сфер
жизни — от здравоохранения, занятости и образования до участия в социальной,
культурной и политической жизни.""",
]


st.title("Translate")
sample_text = choice(starting_texts)
user_input = st.text_area("Enter text to translate:", sample_text)
src = st.text_input("Translate from:", value="auto")
dst = st.text_input("Translate to:", value="ru")
if st.button("Translate"):
    if not user_input.strip():
        st.warning("Enter some text to translate.")
    else:
        try:
            text = Text(user_input, src)
            translated_text = text.translate(dst)
            lang_name = supported_languages[translated_text.language].capitalize()
            tag = f"{translated_text.language} ({lang_name})"
            st.badge(tag, color="blue")
            st.write(translated_text.content)
        except TranslationError as e:
            st.error(f"Translation error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
if st.button("Capture"):
    pass  # pass *text* to *user_input* and *src* field

# To run this app, use the command:
# streamlit run translate.py
# Also found at https://huggingface.co/spaces/epogrebnyak/translate/blob/main/src/streamlit_app.py
