import os
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate

from secret_key import openai_key

os.environ["OPENAI_API_KEY"] = openai_key
from langchain.chains import SequentialChain, LLMChain

llm = OpenAI(temperature=0.7)


def generate_res_name_and_items(cuisine):
    # Cahin 1 Restaurant Name
    prompt_template_name1 = PromptTemplate(input_variables=["cuisine"],
                                           template="I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
                                           )
    name_chain1 = LLMChain(llm=llm, prompt=prompt_template_name1, output_key="restaurant_name")

    # Chain2: Menu Items
    prompt_template_items1 = PromptTemplate(input_variables=["restaurant_name"],
                                            template="suggest some menu items for {restaurant_name}."
                                            )
    food_items_chain1 = LLMChain(llm=llm, prompt=prompt_template_items1, output_key="menu_items")

    chain1 = SequentialChain(chains=[name_chain1, food_items_chain1],
                             input_variables=['cuisine'],
                             output_variables=["restaurant_name", "menu_items"]
                             )
    response = chain1({"cuisine": cuisine})

    return response


if __name__ == "__main__":
    print(generate_res_name_and_items("Italian"))
