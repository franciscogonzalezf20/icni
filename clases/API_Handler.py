from httpcore import request
from jinja2 import Environment, FileSystemLoader
import requests

class APIHandler:
    def __init__(self):
        self.templates_folder = '/home/roatech/Desktop/projecto-soto/templates'
        
    def get_template(self, template_name):
        env = Environment(loader=FileSystemLoader(self.templates_folder))
        return env.get_template(template_name)


    def send_number_to_api(self, number:str):
        print(' entra al send')
        url = "http://192.168.100.83:8100/numIntegracion"
        data = {"num_integracion": number}
        headers = {'Content-Type': 'application/json'}
        try:
            print("Antes de enviar: ", data)
            response = requests.post(url, headers=headers, json=data)
            print(response)
        except:
            response = request.post(url, {"msg": "Se envio mal"})
            print(response)
