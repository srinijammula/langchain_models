from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(template="Write a detailed report on {topic}", input_variables=["topic"])

prompt2=PromptTemplate.from_template("Write a summary of the following for 500 words: {text}")

str_parser=StrOutputParser()

chain = prompt1 | model | str_parser | prompt2 | model | str_parser
topic = "Srini Jammula"
result = chain.invoke(topic)
print(result)
