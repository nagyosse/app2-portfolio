import streamlit as st
from seng_email import send_email
st.header("Contact Me")

with st.form(key="memail_form"):
    user_email = st.text_input("Your email address")
    row_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{row_message}
"""
    button = st.form_submit_button("Submit")
    if button:
       send_email(message)
       st.info("Your email send!")
