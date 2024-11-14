# Real-Time News Summarizer

This project is a Real-Time News Summarizer that fetches the latest news articles on a given topic, retrieves relevant content, and summarizes them using Retrieval-Augmented Generation (RAG) with LangChain and OpenAI's GPT-4.

## **Features**

- **Fetch Latest News**: Retrieves news articles based on a given topic using NewsAPI.org.
- **Retrieval-Augmented Generation**: Uses vector embeddings and FAISS for efficient retrieval.
- **Summarization**: Summarizes the content of each article using LangChain and OpenAI's GPT-4.
- **API Endpoint**: Provides a RESTful API for easy integration.

## **Requirements**

- Python 3.8 or higher
- API keys for NewsAPI.org and OpenAI
- Internet connection

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/real_time_news_summarizer.git
cd real_time_news_summarizer
