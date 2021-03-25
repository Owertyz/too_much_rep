from http.server import SimpleHTTPRequestHandler
import http.client
import logging
import sys
try:
    PORT = int(sys.argv[1])
except:
    PORT = 5050


conn = http.client.HTTPConnection('127.0.0.1', 5050)
conn.request('GET', '/')
r1 = conn.getresponse()
print(r1.status, r1.reason)
