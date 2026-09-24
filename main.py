import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

def init_session_state():
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
    # st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state.messages = [
        {
            "role": "AI",
            "content": "你好，我是你的AI助手，有什么可以帮你的吗？"
        }
    ]

st.title("💬 克隆ChatGPT")

if st.sidebar.button("开启新对话"):
    init_session_state()

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")
    openai_api_base = st.text_input("请输入OpenAI API 基地址：", type="password")


if "memory" not in st.session_state:
    init_session_state()

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()

if prompt:
    if not (openai_api_base and openai_api_key):
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state.messages.append(
        {
            "role": "human",
            "content": prompt
        }
    )
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state.memory, openai_api_key, openai_api_base)

    msg = {"role": "AI", "content": response}
    st.session_state.messages.append(msg)
    # st.chat_message("AI").write(response)
    st.chat_message(msg["role"]).write(msg["content"])
