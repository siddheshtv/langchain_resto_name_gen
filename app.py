import streamlit as st

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
    "Malaysian",
    "Indonesian",
    "Italian-American",
    "Tex-Mex",
    "Scandinavian",
    "Cuban",
    "Argentinian",
    "Irish",
    "Australian",
    "British",
    "Ukrainian",
    "Dutch",
    "Polish",
    "Canadian",
    "Israeli",
    "Filipino",
    "Jamaican"
]

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisine_options)

from langchain.llms import OpenAI
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def gen_resto_item(cuisine):
    return {
        'restaurant_name' : '',
    }

if cuisine:
    gen_resto_item(cuisine)