from langchain.embeddings import OpenAIEmbeddings
from config.settings import OPENAI_API_KEY

def get_embedding_model():
    return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def generate_embedding(texts):
    if not texts:
        return []
    embeddings_model=get_embedding_model()
    try:
        return embeddings_model.embed_documents(texts)
    except Exception as e:
        print("Error generating embeddings:{e}")
        return []
    