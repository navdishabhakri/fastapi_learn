from groq import Groq
import os
from dotenv import load_dotenv
from fastapi import FastAPI,status, HTTPException, Depends
from pydantic import BaseModel
app= FastAPI()
load_dotenv() # loads variables from .env
key= os.getenv("API_KEY")
client = Groq(api_key= key ) # create a client

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )
# print(chat_completion.choices[0].message.content)

class Message(BaseModel): # needed because you can only pass a Pydantic model in the 
    content: str
    
# messages=[]
# while True:
#     reply= ""
#     i= input("Enter message")
#     messages.append({"role":"user", "content": i })
#     chat = client.chat.completions.create(messages=messages,model="llama-3.3-70b-versatile", stream=True)
#     for chunk in chat:
#          if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="")
#             reply+= chunk.choices[0].delta.content
    
#     # reply= chat_completion.choices[0].message.content
#     # print(reply) won't work now because i am streaming
#     messages.append({"role":"assistant","content": reply})
#     messages = messages[-10:]

msg=[]
@app.post("/api", status_code =status.HTTP_201_CREATED)
async def create_message(question: Message):
    global msg
    reply= ""
    msg.append({"role":"user", "content": question.content}) # question.content to get content of the model Message
    chat = client.chat.completions.create(messages=msg,model="llama-3.3-70b-versatile", stream=True)
    for chunk in chat:
         if chunk.choices[0].delta.content is not None:
            reply+= chunk.choices[0].delta.content
    msg.append({"role":"assistant","content": reply})
    msg = msg[-10:]
    return reply
    
