from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorld(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello world\n")

server = HTTPServer(("0.0.0.0", 32777), HelloWorld).serve_forever()

