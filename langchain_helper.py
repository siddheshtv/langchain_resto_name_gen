from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def gen_resto_item(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables={'cuisine': cuisine},
        template='Generate a restaurant name for {cuisine} cuisines.'
    )

    prompt_template_items = PromptTemplate(
        input_variables={'restaurant_name': 'Generated Restaurant Name'},
        template='Give me some menu items for the restaurant named, {restaurant_name}'
    )

    chain_name = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')
    chain_items = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(chains=[chain_name, chain_items])
    return chain({'cuisine': cuisine})