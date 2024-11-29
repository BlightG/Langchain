from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_token = os.getenv('OPEN_API_TOKEN')
os.environ["OPENAI_API_KEY"] = openai_api_token

# Define a prompt template
template = "Write a poem about {topic}."
prompt = PromptTemplate(template=template, input_variables=["topic"])

# Combine with an LLM
llm = OpenAI(temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("nature")
print(result)
