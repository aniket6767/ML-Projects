from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # this is the endpoint , a decorator
def hello() :
    return {"message : hello world"}

@app.get("/about")
def about():
    return{"message : welcome to aniket's fast api world"}