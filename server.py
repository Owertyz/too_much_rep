from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import logging
import sys

try:
    PORT = int(sys.argv[1])
except:
    PORT = 5050

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):

        print(self.headers["User-Agent"])
        if "android" in (self.headers["User-Agent"]).lower():
            self.send_response(403, self.headers)
        else:
            self.send_response(200, self.headers)
        self.end_headers()


Handler = GetHandler
httpd = TCPServer(('', PORT), Handler)

httpd.serve_forever()