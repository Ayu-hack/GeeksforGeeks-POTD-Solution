import os
import wget
import streamlit as st
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def bar_custom(current, total, width=80):
    print("Downloading %d%% [%d / %d] bytes" % (current / total * 100, current, total))

model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"
model_path = os.path.join(os.getcwd(), "llama-2-7b-chat.Q2_K.gguf")
wget.download(model_url, model_path, bar=bar_custom)

def init_page() -> None:
    st.set_page_config(
        page_title="Personal Chatbot"
    )
    st.header("Personal Chatbot")
    st.sidebar.title("Options")

def select_llm() -> LlamaCPP:
    return LlamaCPP(
        model_path=model_path,
        temperature=0.1,
        max_new_tokens=500,
        context_window=3900,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": 1},
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )

def init_messages() -> None:
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content="you are a helpful AI assistant. Reply to your answer in markdown format."
            )
        ]

def get_answer(llm, messages) -> str:
    response = llm.complete(messages)
    return response.text

def main() -> None:
    init_page()
    llm = select_llm()
    init_messages()

    if user_input := st.text_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Bot is typing ..."):
            answer = get_answer(llm, user_input)
            print(answer)
        st.session_state.messages.append(AIMessage(content=answer))

    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.beta_container():
                st.write("Assistant:")
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.beta_container():
                st.write("User:")
                st.markdown(message.content)

if __name__ == "__main__":
    main()
