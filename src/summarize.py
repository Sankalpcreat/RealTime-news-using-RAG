# src/summarize.py
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()
from config.settings import OPENAI_API_KEY

def get_llm():
    try:
        llm = OpenAI(openai_api_key=OPENAI_API_KEY)
        return llm
    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenAI LLM: {e}")

def summarize_text(text):
    
    if not text:
        return "No content to summarize."
    MAX_TOKENS = 2000  
    text = text[:MAX_TOKENS]

    llm = get_llm()
    
   
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)
    documents = [Document(page_content=t) for t in texts]
    summarization_chain = load_summarize_chain(llm, chain_type='map_reduce')
    
    try:
        # Run the summarization chain on the list of Document objects
        summary = summarization_chain.invoke(documents)
        return summary.strip()
    except Exception as e:
        return f"Error during summarization: {e}"
