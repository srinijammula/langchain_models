from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatOpenAI()
json_parser=JsonOutputParser()
prompt=PromptTemplate(template="Give a fictional name, age, profession and city {format_instruction}", input_variables=[],
                      partial_variables={"format_instruction": json_parser.get_format_instructions()})

chain = prompt | model | json_parser
result = chain.invoke({})
print(result)
