import streamlit as st
from gtts import gTTS
import os

# Streamlit UI
st.title("🗣️ Text to Speech Converter")
st.write("Convert your text into speech with ease. Select the language, enter your text, and click the button to generate the speech.")

# Sidebar for language selection
st.sidebar.header("Settings")
language = st.sidebar.selectbox("Select Language:", ["English (en)", "Spanish (es)", "French (fr)", "German (de)", "Arabic (ar)", "Urdu (ur)", "Hindi (hi)", "Marathi (mr)"], index=0)

# Text input
st.subheader("Enter your text below:")
text = st.text_area("Your text", placeholder="Type your text here...")

# Convert button
if st.button("🎤 Convert to Speech"):
    if text.strip():
        # Extract language code from the selected language
        lang_code = language.split(" (")[1].strip(")")
        
        # Generate speech using gTTS
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save("output.mp3")
        st.success("Speech conversion successful! Click the play button to listen.")
        st.audio("output.mp3", format="audio/mp3", start_time=0)
        
        # Download button for the audio file
        with open("output.mp3", "rb") as file:
            st.download_button(label="Download Audio", data=file, file_name="output.mp3", mime="audio/mp3")
    else:
        st.warning("Please enter some text to convert.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #2c3e50;
        color: #ecf0f1;
        text-align: center;
        padding: 10px;
        font-family: Arial, sans-serif;
    }
    .footer a {
        color: #1abc9c;
        text-decoration: none;
        margin: 0 5px;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .footer .icons {
        margin-top: 10px;
    }
    .footer .icons img {
        width: 20px;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        Created by Aadil Chauhan | Powered by gTTS & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
