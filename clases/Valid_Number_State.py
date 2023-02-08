from http import HTTPStatus
from http.client import HTTPResponse
from http.server import BaseHTTPRequestHandler
from jinja2 import Template
from .API_Handler import APIHandler
from .State_handle import State
from http.client import HTTPResponse

from http import HTTPStatus
from http.client import HTTPResponse
from http.server import BaseHTTPRequestHandler
from jinja2 import Template
from .API_Handler import APIHandler
from .State_handle import State

class ValidNumberState(State):
    def handle(self, number:str, api_handler:APIHandler):
        api_handler.send_number_to_api(number)
        template = api_handler.get_template("/search.html")
        content = template.render({"number": number})
        return HTTPStatus.OK, [('Content-type', 'text/html; charset=utf-8')], content



