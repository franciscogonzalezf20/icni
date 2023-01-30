from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import requests

from httpcore import request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="./templates"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
  html_address = "./templates/index.html"
  return FileResponse(html_address, status_code=200)

class APIHandler:
    def send_number_to_api(self, number:str):
        url = "https://kjldup.deta.dev/pruebasat"
        data = {"numintegracion": number}
        try:
            
            response = requests.post(url, json=data)
            print(response)

        except:
            response = request.post(url, {"msg": "Se envio mal"})
            print(response)
            
    

class State:
    def handle(self, number:str):
        pass

class ValidNumberState(State):
    def handle(self, number:str, api_handler:APIHandler):
        template = templates.get_template("/search.html")
        content = template.render({"number": number})
        api_handler.send_number_to_api(number)
        return HTMLResponse(content=content, status_code=200)

class InvalidNumberState(State):
    def handle(self, number:str, api_handler:APIHandler):
        template = templates.get_template("/error.html")
        content = template.render({"number": number})
        return HTMLResponse(content=content, status_code=200)


@app.post("/search")
def search(number: str = Form(...)):
    api_handler = APIHandler()
    factory = NumberFactory()
    state = factory.create_number_state(number)
    return state.handle(number, api_handler)



class NumberFactory:
    def create_number_state(self, number:str):
        if len(number) == 13:
            return ValidNumberState()
        elif len(number) == 8:
            return ValidNumberState()
        else:
            return InvalidNumberState()