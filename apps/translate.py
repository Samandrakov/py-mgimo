from random import choice
import streamlit as st
from mgimo.translate import Text, supported_languages, TranslationError

# Track the last translated text
if 'last_translated_text' not in st.session_state:
    st.session_state.last_translated_text = None
if 'last_translated_language' not in st.session_state:
    st.session_state.last_translated_language = None

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

# Initialize widget values in session state if they don't exist
if 'user_input' not in st.session_state:
    st.session_state.user_input = choice(starting_texts)
if 'src_input' not in st.session_state:
    st.session_state.src_input = "auto"
if 'dst_input' not in st.session_state:
    st.session_state.dst_input = "ru"

# Widgets bound to session state
user_input = st.text_area("Enter text to translate:", value=st.session_state.user_input, height="content", key="user_input")
src = st.text_input("Translate from:", value=st.session_state.src_input, key="src_input")
dst = st.text_input("Translate to:", value=st.session_state.dst_input, key="dst_input")

# Buttons in columns
col1, col2 = st.columns(2)
with col1:
    translate_pressed = st.button("Translate")
with col2:
    capture_pressed = st.button("Capture")

# Handle button presses
if translate_pressed:
    if not user_input.strip():
        st.warning("Enter some text to translate.")
    else:
        try:
            text = Text(user_input, src)
            translated_text = text.translate(dst)
            # Store the translated text and its language in session state
            st.session_state.last_translated_text = translated_text.content
            st.session_state.last_translated_language = translated_text.language
            
            lang_name = supported_languages[translated_text.language].capitalize()
            tag = f"{translated_text.language} ({lang_name})"
            st.badge(tag, color="blue")
            st.write(translated_text.content)
        except TranslationError as e:
            st.error(f"Translation error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if capture_pressed:
    # Update the widget values directly in session state
    if st.session_state.last_translated_text is not None:
        st.session_state.user_input = st.session_state.last_translated_text
        st.session_state.src_input = st.session_state.last_translated_language
    else:
        # If no translation exists, use current values (though this shouldn't normally happen)
        st.session_state.user_input = user_input
        st.session_state.src_input = src
    # Rerun to update the UI with new widget values
    st.rerun()

# To run this app, use the command:
# streamlit run translate.py
# Also found at https://huggingface.co/spaces/epogrebnyak/translate/blob/main/src/streamlit_app.py
