from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel, TypeAdapter
import os

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class subtodoai(BaseModel):
  title: str
  description: list[str]


# Configure Gemini API Key
client=genai.Client(api_key=GEMINI_API_KEY)


def generate_subtodos(todo_title: str, todo_description: str):
    prompt = f"Break down the task '{todo_title}' into smaller, actionable sub-tasks. Here is more context: {todo_description}. Return the tasks as a numbered list."
    response = client.models.generate_content(
        model = 'gemini-1.5-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[subtodoai],
        },
    )
    return response.parsed  

