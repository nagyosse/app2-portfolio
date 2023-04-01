import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Adri Lacika")
    content = """
    Hi I'm a python programmer, teacher, and founder of PythonHow. I graduated in 2023
    I have worked with companies from various countries, such as the Center for Conservation Geography  
    """
    st.info(content)

    content2 = """
    Below you can find some of te apps I have build in Python. Feel free to contact me!
    """
    st.write(content2)

    print("Hello")