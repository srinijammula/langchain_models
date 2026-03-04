from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(template="Write a detailed report on {topic}", input_variables=["topic"])

prompt2=PromptTemplate.from_template("Write 5 points about: {text}")

prompt3=PromptTemplate.from_template("Write 5 mcqs about: {text}")

prompt4=PromptTemplate.from_template("combine the following points and mcqs into a single document: {points} {mcqs}")

str_parser=StrOutputParser()

start_chain = prompt1 | model | str_parser

parallel_chain=RunnableParallel({
    "points": prompt2 | model | str_parser,
    "mcqs": prompt3 | model | str_parser
}
)

merge_chain= prompt4 | model | str_parser

chain = start_chain | parallel_chain | merge_chain
topic = "Graduation day"
result = chain.invoke(topic)    
print(result)