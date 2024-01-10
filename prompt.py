from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from redundant_filter_retriever import RedundantFilterRetriever

def initization():
    load_dotenv()
    chat = ChatOpenAI()
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory="emb",
        embedding_function=embeddings
    )
    retriever = RedundantFilterRetriever(
        embeddings=embeddings,
        chroma=db
    )
    return chat, retriever

def prompt_execution(chat, retriever):
    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff"
    )
    return chain


if __name__ == "__main__":

    chat, retriever = initization()
    chain = prompt_execution(chat, retriever)
    while True:
        prompt = input("Enter a prompt: ")
        result = chain.run(prompt)
        print(result)
