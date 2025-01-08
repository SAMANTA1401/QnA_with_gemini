from llama_index.core import VectorStoreIndex

from llama_index.embeddings.gemini import GeminiEmbedding 
from llama_index.llms.gemini import Gemini

import google.generativeai as genai
import sys
from qawithgemini.exception.exception import customexception
from qawithgemini.logger.logger import logging
import os
from dotenv import load_dotenv

from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.core.node_parser import SentenceSplitter



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def download_gemini_embedding(document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model=GeminiEmbedding(model_name="models/embedding-001")
        Settings.llm = Gemini(model='models/gemini-pro')
        Settings.embed_model = GeminiEmbedding(model="models/embedding-001")
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)
        
        logging.info("")
        index = VectorStoreIndex.from_documents(document, embed_model=gemini_embed_model)
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise logging.info(customexception(e,sys))