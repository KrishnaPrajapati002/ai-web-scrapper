"""main.py"""

import streamlit as st
from scrape import scrape_website

st.title("AI Web scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape site"):
    st.write("Scrapping the website")
    result = scrape_website(url)

    print(result)

