import streamlit as st
from langchain_helper import gen_resto_item
from secret_key import openai_api_key
import os

os.environ["OPENAI_API_KEY"] = openai_api_key

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



if cuisine:
    response = gen_resto_item(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items")
    for item in menu_items:
        st.write(item)
