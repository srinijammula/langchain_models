from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatOpenAI()

class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment on feedback")

pydantic_parser=PydanticOutputParser(pydantic_object=Sentiment)

prompt1= PromptTemplate(template="Give sentiment on feedback: {feedback} {format_instruction}", input_variables=["feedback"],
                        partial_variables={"format_instruction": pydantic_parser.get_format_instructions()})

chain1= prompt1 | model | pydantic_parser

str_parser=StrOutputParser()
prompt2=PromptTemplate(template="Write a response on this negative feedback: {feedback}", input_variables=["feedback"])
prompt3=PromptTemplate(template="Write a response on this positive feedback: {feedback}", input_variables=["feedback"])

branching_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt3 | model | str_parser),
    (lambda x:x.sentiment == 'negative', prompt2 | model | str_parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chain = chain1 | branching_chain
feedback = "The product quality is fantastic"
result = chain.invoke({"feedback": feedback})   
print(result)