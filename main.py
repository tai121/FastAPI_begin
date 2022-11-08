from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data': {'name': 'Victor'}}

    
@app.get("/about")
def about():
    return {'data': {'about': 'about page'}}