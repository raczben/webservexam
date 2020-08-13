#!/usr/bin/env python3

import http.server

from io import BytesIO
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mywebpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

        

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()