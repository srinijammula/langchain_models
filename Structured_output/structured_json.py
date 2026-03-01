from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

json_schema={
    "title": "Review_analysis",
    "type": "object",   
    "description": "A structured output schema for analyzing product reviews.",
    "properties": {
        "Summary": {
            "type": "string"
        },
        "Sentiment": {
            "type": "string",
            "description": "The overall sentiment of the review (e.g., positive, negative, neutral)."
        }
    },  
    "required": ["Summary", "Sentiment"]
}


review = "The movie was okay.But the ending was a bit disappointing."
structured_model=model.with_structured_output(json_schema)

result=structured_model.invoke(review)
print(result)


