import streamlit as st 
from helper import create_vector_db,get_qa_chain

st.title("CourseMate : Educational QA bot")
btn = st.button("Create Knowledgebase")
if btn:
    pass
question = st.text_input("Question : ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer:")
    st.write(response['result'])
    
