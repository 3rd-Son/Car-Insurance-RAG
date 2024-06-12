# Car Insurance Policy RAG (Retrieval-Augmented Generation) ChatBot

This project is a Streamlit application that allows users to ask questions related to a car insurance policy document and receive accurate and concise responses. The application leverages a Retrieval-Augmented Generation (RAG) model to retrieve relevant information from a vector database and generate human-like responses.

## Files

- **main.py**: This file contains the Streamlit application code. It handles the user interface, input processing, and response generation.
- **utils.py**: This file contains utility functions used within main.py for embedding queries, querying the vector database (Pinecone), and generating final responses using an LLM (Large Language Model).
- **upload.ipynb**: This Jupyter Notebook was used for data preparation, including chunking the car insurance policy document, embedding the chunks, and upserting (inserting or updating) the embeddings and metadata into the Pinecone vector database. It also serves as a testing environment for the RAG pipeline.
- **constants.py**: This file contains constant values used throughout the project, such as the system prompt for the LLM.

## Deployment

The application is hosted on Streamlit Cloud and can be accessed at [https://car-insurance-rag.streamlit.app/](https://car-insurance-rag.streamlit.app/)

## Usage

1. Open the application in your web browser.
2. Enter your question related to the car insurance policy in the provided text input field.
3. Click the "Enter" button or press Enter to submit your query.
4. The application will process your query, retrieve relevant information from the vector database, and generate a response using the LLM.
5. The final response will be displayed on the screen.

