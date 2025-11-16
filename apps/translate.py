from random import choice
import streamlit as st
from mgimo.translate import Text, supported_languages, TranslationError

# Initialize session state
if 'captured_text' not in st.session_state:
    st.session_state.captured_text = ""
if 'captured_src' not in st.session_state:
    st.session_state.captured_src = "auto"
# Track if we need to update the widgets from captured values
if 'update_from_capture' not in st.session_state:
    st.session_state.update_from_capture = False

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

# Initialize default values for widgets
if st.session_state.update_from_capture:
    default_text = st.session_state.captured_text
    default_src = st.session_state.captured_src
    # Reset the flag
    st.session_state.update_from_capture = False
else:
    # Use captured values if they exist, otherwise use the sample
    if st.session_state.captured_text:
        default_text = st.session_state.captured_text
    else:
        default_text = choice(starting_texts)
    default_src = st.session_state.captured_src

# Widgets outside the form to prevent reruns on every interaction
user_input = st.text_area("Enter text to translate:", value=default_text, height="content", key="user_input")
src = st.text_input("Translate from:", value=default_src, key="src_input")
dst = st.text_input("Translate to:", value="ru", key="dst_input")

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
            lang_name = supported_languages[translated_text.language].capitalize()
            tag = f"{translated_text.language} ({lang_name})"
            st.badge(tag, color="blue")
            st.write(translated_text.content)
        except TranslationError as e:
            st.error(f"Translation error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if capture_pressed:
    # Update the captured state with current values
    st.session_state.captured_text = user_input
    st.session_state.captured_src = src
    # Set flag to update widgets on next run
    st.session_state.update_from_capture = True
    # Rerun to apply the updates
    st.rerun()

# To run this app, use the command:
# streamlit run translate.py
# Also found at https://huggingface.co/spaces/epogrebnyak/translate/blob/main/src/streamlit_app.py
