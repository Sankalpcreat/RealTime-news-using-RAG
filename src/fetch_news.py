import requests
from config.settings import NEWS_API_KEY
from src.utils import sanitize_input

NEWS_API_URL = 'https://newsapi.org/v2/everything'


def fetch_latest_news(topic,language='en',page_size=20):
    topic=sanitize_input(topic)
    params={
        'q':topic,
        'language':language,
        'apikey':NEWS_API_KEY,
        'pageSize':page_size,
    }
    try:
        response=requests.get(NEWS_API_KEY,params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching news:{e}")
        return []
    
    articles =response.json().get('articles',[])

    return [
        {
            'title': article.get('title', ''),
            'content': article.get('content', ''),
            'description': article.get('description', ''),
            'url': article.get('url', '')
        }
        for article in articles if article.get('content') or article.get('description')
    ]
