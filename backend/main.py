import openai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set API key and Groq API base URL
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model = "llama3-70b-8192",   # Groq's supported model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Hi, I’m Nova — your personal AI assistant!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Nova: Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Nova:", response)

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("GROQ_API_KEY")
# openai.api_base = "https://api.groq.com/openai/v1"

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Message(BaseModel):
#     message: str

# @app.post("/chat")
# async def chat(message: Message):
#     try:
#         response = openai.ChatCompletion.create(
#             model="llama3-70b-8192",
#             messages=[{"role": "user", "content": message.message}]
#         )
#         reply = response.choices[0].message.content.strip()
#         return {"reply": reply}
#     except Exception as e:
#         return {"reply": f"Error: {str(e)}"}