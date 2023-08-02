import os
os.environ["OPENAI_API_KEY"] = "API_HERE"


# llm = OpenAI(temperature = 0.7)
# name = llm("I want to open a restaurant for indian food and want to come up with a fancy name for it.")

# print(name)

from langchain.prompts import PromptTemplate

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

prompt_template_template_name = PromptTemplate(
    input_variables= ['cuisine'],
    template= "I want to open a restaurant for {cuisine} food and want to come up with a fancy name for it."
)

name_chain = LLMChain(llm = OpenAI(temperature=0.6), prompt=prompt_template_template_name, output_key="restaurant_name")

prompt_template_template_items = PromptTemplate(
    input_variables= ['restaurant_name'],
    template= "Suggest some menu items for {restaurant_name}. Return it as comma seperated values."
)

item_chain = LLMChain(llm = OpenAI(temperature=0.6), prompt=prompt_template_template_items, output_key="menu_items")

chain = SequentialChain(chains=[name_chain, item_chain], input_variables=['cuisine'], output_variables=['restaurant_name', 'menu_items'])
print(chain({'cuisine': 'Indian'}))