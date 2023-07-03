import streamlit as st

import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from apikey_huggingface import apikey_huggingface

model = "tiiuae/falcon-7b-instruct"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = apikey_huggingface # we import the file that contains the hugging face access tokens

st.sidebar.header("CHOOSE THE PARAMETER")
st.sidebar.write("---")

temperature = st.sidebar.slider('TEMPERATURE', 0.0, 1.0, 0.5)
len = st.sidebar.number_input('MAX', 0, 200, 10)

llm = HuggingFaceHub(repo_id = model, model_kwargs={"temperature": temperature, "max_new_tokens": len, "max_length": 0})
# keep temperature under 1 as anything above 1, the model will start generating random texts.

st.header("NEWS HEADLINE GENERATOR")

template = """Question: {question} \n\n

Answer: Lets think step by step.

"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)


st.write("---")

response = ''

article = st.text_area("enter the article: ", height=200)
if st.button("Generate"):
    with st.spinner("Generating Headlines..."):
        response = llm_chain.run(article) 


st.write("---")

st.header("Generated headlines: ")

 
st.success(response)

    
