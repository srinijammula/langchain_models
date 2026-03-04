from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()
prompt=PromptTemplate(template="Write a short story about {topic} under 100 words.", input_variables=["topic"])
parser=StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({"topic": "a boy who came from the future"})
print(result)
#chain.get_graph().print_ascii()