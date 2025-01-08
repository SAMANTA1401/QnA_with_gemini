import streamlit as st
from qawithgemini.components.embedding import download_gemini_embedding
from qawithgemini.components.data_ingestion import load_data

    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document", accept_multiple_files=True)
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data(doc)
            query_engine=download_gemini_embedding(document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    