from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI


from secret_key import openai_api_key

import os
os.environ["OPENAI_API_KEY"] = openai_api_key
llm = OpenAI(temperature=0.6)

def gen_resto_item(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='Generate a restaurant name for {cuisine} cuisines.'
    )

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Give me some menu items for the restaurant named, {restaurant_name}'
    )

    chain_name = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')
    chain_items = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(chains=[chain_name, chain_items], input_variables=['cuisine'], output_variables=['restaurant_name', 'menu_items'])

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(gen_resto_item("Italian"))