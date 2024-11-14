from src.fetch_news import fetch_latest_news
from src.summarize import summarize_text
from src.retriever import setup_retriever

def rag_pipeline(topic):
    articles = fetch_latest_news(topic)
    if not articles:
        return ["No articles found for the given topic."]

    retriever = setup_retriever(articles)
    if retriever is None:
        return ["Error setting up the retriever."]

    query = topic
    retrieved_documents = retriever.get_relevant_documents(query)
    if not retrieved_documents:
        return ["No relevant articles found."]

    summaries = []
    for doc in retrieved_documents:
        summary = summarize_text(doc.page_content)
        summaries.append({
            'title': doc.metadata.get('title', 'No Title'),
            'url': doc.metadata.get('url', '#'),
            'summary': summary,
        })

    return summaries
