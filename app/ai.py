import google.generativeai as genai
from app.schemas import *
from dotenv import load_dotenv
# Loading gemini api key from Environment
load_dotenv()
import os
GEMINI_API_kEY=os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
genai.configure(api_key=GEMINI_API_kEY)

def generate_subtodos(todo_title:str,todo_description:str):
 model='gemini-2.0-flash',
 prompt = f"Break down the task '{todo_title}' into smaller, actionable sub-tasks. Here is more context: {todo_description}. Return the tasks as a numbered list."
 response =model.generate_content(
    contents=prompt,
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[SubTodo],
    },
     )
 return response.parsed

