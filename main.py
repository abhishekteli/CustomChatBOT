import langchain. document_loaders as ld
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

def initization():
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n","\n",". "," ",""],
        chunk_size =256,
        chunk_overlap=0
        )

    return text_splitter, embeddings

def file_load(file, text_splitter, embeddings):

    name, extension = os.path.splitext(file)
    if extension == '.pdf':
        loader = ld.PyPDFLoader(file)
    elif extension == '.docx':
        loader = ld.Docx2txtLoader(file)
    elif extension == '.csv':
        loader = ld.CSVLoader(file)
    elif extension == '.json':
        loader = ld.JSONLoader(file)
    elif extension == '.html':
        loader = ld.UnstructuredHTMLLoader(file)
    elif extension == '.txt' or extension == '.rtf':
        loader = ld.TextLoader(file)
    else:
        print(f'{file} type not supported')
        return None
    

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
    while True:
        answer = input("Do you want to upload document(Y/N) : ")
        if answer == 'Y' or answer == 'y':
            file_type = input("Enter the File type: ")
            file_location = input("Enter the File location: ")
            file_load(file_type, file_location, text_splitter, embeddings)
        else:
            break
