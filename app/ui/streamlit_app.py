from fastapi import logger
import streamlit as st
import requests 

st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖"
)

st.title("🤖 AI Agent Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        logger.info(f"Displayed {message['role']} message: {message['content']}")

if prompt := st.chat_input("Ask me Anything!"):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(
        "http://localhost:8000/chat",
        json={"goal": prompt}
    )

    answer = response.json()["response"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        while answer is None:
            st.info("Waiting for response... This may take a moment.")
        st.markdown(answer)