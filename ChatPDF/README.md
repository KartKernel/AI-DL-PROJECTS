# ChatPDF App

ChatPDF is a Streamlit-based application that allows users to interact with multiple PDF documents using natural language processing. This application leverages Langchain, OpenAI's embedding API (OpenAIEmbeddings), HuggingFace's embedding API (HuggingFaceInstructEmbeddings), and PyPDF2 for reading PDFs. It uses the ChatOpenAI model for the chat functionality and FAISS for vector storage, ensuring efficient and effective retrieval of information from the PDFs.

## Features

- **Multiple PDF Input**: Upload multiple PDF files for processing.
- **Embeddings**: Use OpenAI's embedding API (OpenAIEmbeddings) or HuggingFace's embedding API (HuggingFaceInstructEmbeddings) for creating embeddings from the PDFs.
- **PDF Reading**: PyPDF2 is used to read and extract text from the PDF files.
- **Chat Functionality**: Chat with the bot and ask any number of questions related to the PDFs.
- **Conversation Memory**: The bot remembers the conversation using Langchain's conversation buffer memory, allowing for context-aware responses.
- **Vector Store**: FAISS is used to store and retrieve vector embeddings efficiently.

## Installation

To get started with ChatPDF, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatpdf.git
    cd chatpdf
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload PDFs**: Drag and drop your PDF files into the designated area on the web interface.
2. **Processing**: The application will read and process the PDFs, creating embeddings using the selected embedding API (OpenAIEmbeddings or HuggingFaceInstructEmbeddings).
3. **Chat**: Start chatting with the bot by asking questions related to the content of the uploaded PDFs. The bot will respond based on the information retrieved from the PDFs, utilizing the conversation memory to maintain context.

## Dependencies
- Langchain
- OpenAI API: For embeddings and chat model (OpenAIEmbeddings, ChatOpenAI)
- HuggingFace API: Alternative embeddings (HuggingFaceInstructEmbeddings) --> free.
- PyPDF2: For reading and extracting text from PDFs.
- FAISS: For efficient vector storage and retrieval.
- Streamlit: For the web-based interface.

