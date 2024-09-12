from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama3-8b-8192")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a quiz generator. Create a multiple-choice question based on the following content:"),
    ("user", "Please provide the question and 4 options, marking one as correct on {content}")
])

parser = StrOutputParser()

chain = prompt_template | model | parser

def generate_quiz(content):
    return chain.invoke({"content": content})