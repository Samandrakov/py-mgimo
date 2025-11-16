# create streamlit app for text translation using mgimo.translate module
import streamlit as st
from mgimo.translate import Text, supported_languages, TranslationError


# The app should have a text input and Translate Random buttion
# after pressing the button the app should translate the text to a random language
# and display the translated text along with the language code and name.
st.title("Translate")
st.write("Enter text to translate to a random language.")
user_input = st.text_area("Enter text here:")
if st.button("Translate Random"):
    if not user_input.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            text = Text(user_input)
            translated_text = text.translate_to_random()
            lang_name = supported_languages[translated_text.language]
            st.subheader("Translated Text")
            st.write(f"Language: {translated_text.language} ({lang_name})")
            st.write(translated_text.content)
        except TranslationError as e:
            st.error(f"Translation Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# To run this app, use the command: 
# streamlit run src/mgimo/translate/app.py
