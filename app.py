
import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi API
import streamlit as st

genai.configure(
    api_key=st.secrets["AQ.Ab8RN6IfY9vyTPU4HOhRUKR5fZoW8KZcxGDpeD4ZGlg03Cer1g"]
)

# Gemini Flash
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓"
)

st.title("🎓 StudyMate AI")
st.caption("Personal Learning Assistant")

st.sidebar.title("⚙️ Pengaturan AI")

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.7
)

st.sidebar.markdown("---")

st.sidebar.info("""
🎓 StudyMate AI

Model: Gemini 2.5 Flash

Domain: Pendidikan

Memory: Aktif

Versi: 1.0
""")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []
    st.rerun()

# Membuat chat memory
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Menyimpan pesan untuk ditampilkan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan chat sebelumnya
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input user
prompt = st.chat_input("Tanyakan sesuatu...")

if prompt:

    # tampilkan pesan user
    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # kirim ke Gemini
    response = st.session_state.chat.send_message(
    prompt,
    generation_config={
        "temperature": temperature
    }
)

    answer = response.text

    # tampilkan jawaban AI
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })
