
from http import HTTPStatus
from http.client import HTTPResponse
from http.server import BaseHTTPRequestHandler
from jinja2 import Template
from .API_Handler import APIHandler
from .State_handle import State
import os
"""
class InvalidNumberState(State):
    def handle(self, number:str, api_handler:APIHandler):
        template = api_handler.get_template("/error.html")
        content = template.render({"number": number})
        return HTTPResponse(body=content, status=200)

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
"""
class InvalidNumberState(State):
    def handle(self, number:str, api_handler:APIHandler):
        template = api_handler.get_template("/error.html")
        content = template.render({"number": number})
        headers = [('Content-type', 'text/html; charset=utf-8')]
        response = HTTPResponse(status_code=HTTPStatus.OK, headers=headers, content=content)
        return response
