import os

import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler


def create_agent_chain():
    chat = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
        streaming=True,
    )

    tools = load_tools(["ddg-search", "wikipedia"])

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")]
    }

    memory = ConversationBufferMemory(
        memory_key="memory", return_messages=True)

    return initialize_agent(
        tools,
        chat,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory
    )


# main
load_dotenv()
st.title("streamlit-langchain-app")

if "agent_chain" not in st.session_state:
    st.session_state.agent_chain = create_agent_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["context"])

prompt = st.chat_input("what is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = st.session_state.agent_chain.run(
            prompt, callbacks=[callback])
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "user", "context": prompt})

    st.session_state.messages.append(
        {"role": "assistant", "context": response})
