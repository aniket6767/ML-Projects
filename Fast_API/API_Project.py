from fastapi import FastAPI
import json

app = FastAPI()


def load_data():
    with open('C:\ML Projects\Fast_API\patients.json' ,'r') as f :
        data = json.load(f)

    return data 




@app.get("/") 
def hello():
    return ("message : patient managemeny system api")

@app.get("/about")
def about():
    return ("message : A fully functional API to manage your patients recors")

@app.get("/view")
def view():
    data = load_data()
    return data


load_data()