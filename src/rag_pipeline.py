# src/rag_pipeline.py
from src.fetch_news import fetch_latest_news
from src.summarize import summarize_text
from src.retriever import setup_retriever

def rag_pipeline(topic):
    articles = fetch_latest_news(topic)
    if not articles:
        print("No articles found for the given topic.")
        return ["No articles found for the given topic."]

    retriever = setup_retriever(articles)
    if retriever is None:
        print("Error setting up retriever.")
        return ["Error setting up the retriever."]

    query = topic
    try:
        retrieved_documents = retriever.invoke(query)
        
        print(f"Retrieved documents: {retrieved_documents}")  
    except AttributeError:
        print("Error: The retriever object does not have an 'invoke' method.")
        return ["Error: The retriever object does not have an 'invoke' method."]
    except Exception as e:
        return [f"Error during retrieval: {e}"]

    if not retrieved_documents:
        print(f"Error during retrieval: {e}")
        return ["No relevant articles found."]

    summaries = []
    for doc in retrieved_documents:
        summary = summarize_text(doc.page_content)
        if "Error during summarization" in summary:
            print(f"Error summarizing document: {doc.metadata.get('title', 'No Title')}")
            continue  
        summaries.append({
            'title': doc.metadata.get('title', 'No Title'),
            'url': doc.metadata.get('url', '#'),
            'summary': summary,
        })
    print(f"Final summaries: {summaries}")
    return summaries
