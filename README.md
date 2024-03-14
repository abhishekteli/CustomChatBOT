# Document Processing and Retrieval System

## Introduction and Business Requirement
The objective of this system is to enhance information retrieval and processing capabilities across various document types. By leveraging advanced natural language processing (NLP) and machine learning algorithms, the system provides an efficient and effective way to index, search, and extract relevant information from a corpus of documents. This supports business intelligence, knowledge management, and data-driven decision-making, addressing the need for quick access to accurate and pertinent information from large and diverse document sets.

## System Architecture

### Initialization and Document Loading (main.py)
The main.py script initializes the necessary components and loads documents into the system. It employs OpenAIEmbeddings for vector representation and RecursiveCharacterTextSplitter for breaking down documents into manageable chunks. The system supports various document types, including PDF, DOCX, CSV, JSON, HTML, TXT, and RTF, with appropriate loaders for each. Once a document is loaded, it is split using the text splitter and then indexed using the Chroma vector store, which embeds the text chunks and persists the embeddings for retrieval.

### Prompt Processing and Information Retrieval (prompt.py)
prompt.py handles user queries and information retrieval using a conversational interface. It initializes a ChatOpenAI instance for natural language understanding and a Chroma instance for accessing the indexed embeddings. The RedundantFilterRetriever uses these embeddings to retrieve relevant document snippets based on the user's prompt. The RetrievalQA chain integrates these components to process user prompts, query the indexed data, and return relevant responses, enhancing the user's ability to obtain precise information quickly.

### Redundancy Filtering (redundant_filter_retriever.py)
The RedundantFilterRetriever class is designed to refine search results, minimizing redundant information. It leverages the embeddings to perform a max marginal relevance search, prioritizing diversity in the retrieved documents. This approach ensures that the information presented to the user is not only relevant but also varied, providing a comprehensive overview of the topic in question.

## Execution Flow
The system operates interactively, starting with document upload and indexing (main.py). Users can upload documents of supported types, which are then processed and stored in an indexed format. Following this, users can interact with the system via prompt.py to enter queries and receive relevant, concise, and diverse information excerpts in response. The system's loop continues until the user chooses to exit, allowing for continuous query processing and information retrieval.
