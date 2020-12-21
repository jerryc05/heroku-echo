#!/usr/bin/env python3

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.path, "utf-8"))

if __name__ == "__main__":        
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 17995))
    webServer = HTTPServer((HOST, PORT), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
