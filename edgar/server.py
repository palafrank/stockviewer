from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello World !")
        return
    
hostName = "localhost"
serverPort = 8080
webServer = HTTPServer((hostName, serverPort), MyServer)
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()
print("Server stopped.")



