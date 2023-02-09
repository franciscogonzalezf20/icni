from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from httpcore import Request 
from clases.API_Handler import APIHandler
from clases.Number_Factory import NumberFactory


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="./templates"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
  html_address = "./templates/index.html"
  return FileResponse(html_address, status_code=200)


@app.post("/search")
def search(number: str = Form(...)):
    api_handler = APIHandler()
    factory = NumberFactory()
    print(f'\n\tEntra: {number}')
    state = factory.create_number_state(number)
    return state.handle(number, api_handler)
  
    #return FileResponse("")


