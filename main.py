from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st

def ai_poet():
    chat_model = ChatOpenAI(openai_api_key="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")

    st.title("인공지능 시인")

    content = st.text_input("시의 주제를 제시해주세요.")

    if st.button('시 작성 요청하기'):
        with st.spinner('Wait for it...'):
            result = chat_model.predict(content + "에 대한 시를 써줘!")
            st.write(result)  

def test5():
    st.title("인공지능 시인")
    title = st.text_input("시의 주제를 제시해주세요.")
    st.write("시의 주제는", title)

def test4():
    st.title("인공지능 시인")
    title = st.text_input("Movie title", "Life of Brian")
    st.write("The current movie title is", title)


def test3():
    st.title("This is a title")
    st.title("_Streamlit_ is : blue[cool] :sunglasses:")


def test2():
    chat_model = ChatOpenAI(openai_api_key="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")

    content = "코딩"
    result = chat_model.predict(content + "에 대한 시를 써줘!")
    print(result)     

def test1():
    llm = OpenAI(openai_api_key="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")

    result = llm.predict("내가 좋아하는 동물은 ")
    print(result)

    chat_model = ChatOpenAI(openai_api_key="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")
    result = chat_model.predict("내가 좋아하는 동물은 ")
    print(result)



ai_poet()
