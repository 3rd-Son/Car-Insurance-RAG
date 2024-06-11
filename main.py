import streamlit as st
import pinecone
from constants import SYSTEM_PROMPT
from utils import get_query_embeddings, query_pinecone_index, better_query_response


def main():
    st.title("Car Insurance Policy Question Answering")
    user_question = st.text_input("Ask your question about the car insurance policy:")
    submit_button = st.button("Enter")

    if submit_button:
        query_embeddings = get_query_embeddings(user_question)
        answers = query_pinecone_index(query_embeddings)
        text_answer = " ".join([doc["metadata"]["text"] for doc in answers["matches"]])
        LLM_prompt = f"{SYSTEM_PROMPT}\n\nThis is the question: {user_question}\nThis is the answer from the database: {text_answer}"
        final_answer = better_query_response(LLM_prompt)
        st.write(final_answer)


if __name__ == "__main__":
    main()
