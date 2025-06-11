import os
import sys
from dotenv import load_dotenv
from google import genai  
from google.genai import types 

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print ("Error: String required as command prompt input")
    sys.exit(1)
# Generating content using the Gemini API

user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]
response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
)

prompt_token = response.usage_metadata.prompt_token_count
candidate_token = response.usage_metadata.candidates_token_count

if len(sys.argv) == 2:
    print (response.text)
if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
    user_prompt = sys.argv[1]
    print (f"User prompt: {user_prompt}")
    print (f"Prompt tokens: {prompt_token}")
    print (f"Response tokens: {candidate_token}")

