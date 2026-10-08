from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"AI Business Support Platfor API"}

@app.get("/health")
def health_check():
    return {"status":"healthy"}

@app.get("/about")
def about():
    return {
        "project":"AI Business Support Platform",
        "version":"1.0"
    }
