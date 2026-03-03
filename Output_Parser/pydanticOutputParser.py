from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18,description="The age of the person")
    profession: str = Field(description="The profession of the person")
    city: str = Field(description="The city where the person lives")

model=ChatOpenAI()
parser=PydanticOutputParser(pydantic_object=Person)

prompt=PromptTemplate(template="Give a fictional name, age, profession and city {format_instruction}", input_variables=[],
                      partial_variables={"format_instruction": parser.get_format_instructions()})

chain = prompt | model | parser
result = chain.invoke({})
print(result)
