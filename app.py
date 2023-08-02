import streamlit as st
import os
from langchain.llms import OpenAI

from langchain_helper import gen_resto_item

os.environ["OPENAI_API_KEY"] = "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"

cuisine_options = [
    "Italian",
    "Mexican",
    "Chinese",
    "Japanese",
    "Indian",
    "Thai",
    "French",
    "Greek",
    "Spanish",
    "Korean",
    "Middle Eastern",
    "Vietnamese",
    "Brazilian",
    "Cajun/Creole",
    "German",
    "Ethiopian",
    "Turkish",
    "Caribbean",
    "Moroccan",
    "Russian",
    "Peruvian",
    "Lebanese",
    "South African",
]

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisine_options)

llm = OpenAI(temperature=0.6)

if cuisine:
    result = gen_resto_item(cuisine)
    st.write(result)
