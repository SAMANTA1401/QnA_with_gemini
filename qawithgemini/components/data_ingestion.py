from llama_index.core import SimpleDirectoryReader
import sys
from qawithgemini.logger.logger import logging
from qawithgemini.exception.exception import customexception
from PyPDF2 import PdfReader
def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        text = ""
        for pdf in data:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        with open("Data/data.txt", "w", encoding="utf-8") as f:
            f.write(text)
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise logging.info(customexception(e,sys))



    