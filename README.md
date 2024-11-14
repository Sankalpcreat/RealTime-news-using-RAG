Real-Time News Summarizer
The Real-Time News Summarizer is an application that fetches the latest news articles on a given topic, retrieves relevant content using advanced retrieval mechanisms, and generates concise summaries using Retrieval-Augmented Generation (RAG) with LangChain and OpenAI's GPT-4.

Features
Fetch Latest News: Automatically retrieves up-to-date news articles based on user-specified topics using NewsAPI.org.
Advanced Retrieval: Employs vector embeddings and FAISS (Facebook AI Similarity Search) for efficient and accurate retrieval of relevant articles.
Summarization with GPT-4: Utilizes LangChain and OpenAI's GPT-4 model to generate coherent and concise summaries of retrieved articles.
RESTful API: Provides an easy-to-use API endpoint for seamless integration into other applications or services.
Requirements
Python: Version 3.8 or higher
API Keys:
NewsAPI.org API Key
OpenAI API Key
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/Sankalpcreat/RealTime-news-using-RAG.git
cd RealTime-news-using-RAG
Create a Virtual Environment (Optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the project root directory and add your API keys:

bash
Copy code
touch .env
In .env:

env
Copy code
NEWS_API_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_api_key_here
Usage
Running the Application
Start the Flask server by running:

bash
Copy code
python app.py
The server will start on http://127.0.0.1:5000.

Testing the API Endpoint
You can test the /summarize endpoint using curl or any API testing tool like Postman.


Sample Response:

json
Copy code
{
  "summaries": [
    {
      "title": "AI Revolutionizes Healthcare",
      "url": "http://example.com/article1",
      "summary": "Artificial intelligence is transforming healthcare by improving diagnostics and personalized treatments."
    },
    {
      "title": "Advancements in Machine Learning",
      "url": "http://example.com/article2",
      "summary": "Recent breakthroughs in machine learning are paving the way for more efficient data processing."
    }
    // Additional summaries...
  ]
}

Key Components
app.py: Main Flask application handling API requests.
config/settings.py: Manages configuration settings and environment variables.
src/: Contains source code modules:
fetch_news.py: Fetches news articles from NewsAPI.
embeddings.py: Generates vector embeddings using OpenAI's embedding model.
retriever.py: Sets up the FAISS vector store and retrieval mechanisms.
summarize.py: Summarizes text using LangChain and GPT-4.
rag_pipeline.py: Orchestrates the entire retrieval and summarization process.
utils.py: Contains helper functions like input sanitization.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
LangChain: Framework for building applications with large language models.
OpenAI: Provider of the GPT-4 language model.
NewsAPI.org: Source for news data.
Feel free to explore, modify, and integrate this project into your own applications to provide real-time, summarized news content based on user interests.






