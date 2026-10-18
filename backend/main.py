# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def hello():
#     return {"message":"AI Business Support Platfor API"}

# @app.get("/health")
# def health_check():
#     return {"status":"healthy"}

# @app.get("/about")
# def about():
#     return {
#         "project":"AI Business Support Platform",
#         "version":"1.0"
#     }

# @app.post("/chat")
# def chat():
#     return{
#         "chat":"chat endpoint is working here"
#     }

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class chatRequest(BaseModel):
    message:str

@app.get("/")
def hello():
    return {"message":"AI business support platform API"}

@app.post("/chat")
def chat(request:chatRequest):
    return{
        "user_message":request.message,
        "response":"I received your message!"
    }
