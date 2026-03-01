from typing import Optional
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

class Review(BaseModel):
    Summary: str
    Sentiment: str=Field(description='Positive, Negative or Neutral')
    Pros: Optional[str]

review = "The movie was okay.But the ending was a bit disappointing."
structured_model=model.with_structured_output(Review)

result=structured_model.invoke(review)
print(result)
print(result.Summary + " " + result.Sentiment)

