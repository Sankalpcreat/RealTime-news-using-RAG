from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from src.embeddings import get_embedding_model

def setup_retriever(documents):
    if not documents:
        print("No documents provided to retriever")
        return None

    
    docs = [
        Document(
            page_content=doc.get('content') or doc.get('description', ''),
            metadata={'title': doc.get('title', ''), 'url': doc.get('url', '')}
        )
        for doc in documents
    ]
    print(f"Documents for retriever: {docs}")

    embeddings_model = get_embedding_model()
    try:
        vector_store = FAISS.from_documents(docs, embeddings_model)
        retriever = vector_store.as_retriever()
        return retriever
    except Exception as e:
        raise RuntimeError(f"Error setting up retriever: {e}")
