import os
from langchain.embeddings.openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain


# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

EMBEDDINGS = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])


CHAT_LLM = OpenAI(model_name="gpt-3.5-turbo-instruct", max_tokens=2800)

# Access the API key from the environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Create Pinecone client with the API key
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(name="anthina")

SYSTEM_PROMPT = """You are an experienced insurance professional with deep knowledge of car insurance policies. Your task is to provide accurate and concise responses to queries based on a given car insurance policy document.
You will receive two inputs:
1. The user's question related to the car insurance policy.
2. The answer gotten from the database.
Your role is to summarize the retrieved information and craft a clear, well-structured response that directly answers the user's question. 
Keep your responses straightforward and easy to understand for general audiences.
"""
