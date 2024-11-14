import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()

def get_embedding_model():
    
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment variables.")
        embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)
        return embeddings_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenAIEmbeddings model: {e}")

def generate_embeddings(texts):
    
    if not texts:
        return []

    embeddings_model = get_embedding_model()
    try:
        embeddings = embeddings_model.embed_documents(texts)
        return embeddings
    except Exception as e:
        raise RuntimeError(f"Error generating embeddings: {e}")
