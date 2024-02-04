import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.prompts import PromptTemplate
from design import user, bot, css

load_dotenv()

inputURL = "ROOT URL OF YOUR WEBSITE"
urls = [f'{inputURL}']

loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

def get_text_chunks(text):
    doc_splitter = CharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
    docs = doc_splitter.split_documents(text)
    return docs

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user.replace(
                "{{temp}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot.replace(
                "{{temp}}", message.content), unsafe_allow_html=True)
            
def main():
    st.set_page_config(page_title="Web-Chat",
                       page_icon=":robot_face:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chanakya")
    text_chunks = get_text_chunks(data)
    vectorstore = get_vectorstore(text_chunks)

    st.session_state.conversation = get_conversation_chain(
                vectorstore)
    st.empty()
    user_question = st.text_input("Start Conversation Now!!:")
    if user_question:
        handle_userinput(user_question)

if __name__ == '__main__':
    main()