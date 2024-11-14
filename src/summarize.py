# src/summarize.py
import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.docstore.document import Document
from config.settings import OPENAI_API_KEY

load_dotenv()

def get_llm():
    try:
        llm = OpenAI(openai_api_key=OPENAI_API_KEY)
        return llm
    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenAI LLM: {e}")

def summarize_text(text):
    if not text:
        return "No content to summarize."

    llm = get_llm()
    document = Document(page_content=text)
    summarization_chain = MapReduceDocumentsChain(llm_chain=llm)
    
    try:
        summary = summarization_chain.run([document])
        return summary.strip()
    except Exception as e:
        return f"Error during summarization: {e}"
