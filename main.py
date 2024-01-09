from langchain. document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

def initization():
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size =200,
        chunk_overlap=0
        )

    return text_splitter, embeddings

def file_load(file_type,file_location, text_splitter, embeddings):

    if file_type == "PDF":
        loader = PyPDFLoader(file_path=file_location)
    else:
        loader = TextLoader(file_path=file_location)

    docs = loader.load_and_split(
        text_splitter=text_splitter
    )

    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="emb"
    )

if __name__=="__main__":
    text_splitter, embeddings = initization()
    file_type = input("Enter the File type: ")
    file_location = input("Enter the File location: ")
    file_load(file_type, file_location, text_splitter, embeddings)
