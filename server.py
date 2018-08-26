import os
import requests
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server
import socketserver
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg = "GET /HTTP/1.1"
ip = '127.0.0.1'
port = 80
ip = input('IP to start server on [127.0.0.1 or a local IP]: ')
port = input('Port To Start Server On. [defualt 80]: ')
from http.server import BaseHTTPRequestHandler, HTTPServer
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
        userip = socket.gethostname()
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello! Welcome to " + ip + "!!"
        self.wfile.write(bytes(message, "utf8"))
        return
def run():
  print('starting server...')


  server_address = (ip, int(port))
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  print('server started on ' + ip + ':' + str(port) + '...')
  print('ctrl + c to shutdown...')
  httpd.serve_forever()

run()
