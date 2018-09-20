from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from story import get_story
from story import _init_
import SocketServer
import requests
import json

_init_()

class S(BaseHTTPRequestHandler):
	def do_OPTIONS(self):
		self.send_response(200, "ok")
		self.send_header('Access-Control-Allow-Origin', 'http://plotomatic.com')
		self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
		self.send_header("Access-Control-Allow-Headers", "Content-Type")
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		self.wfile.write("<html><body><h1>hi!</h1></body></html>")

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		# Doesn't do anything with posted data
		#self._set_headers()
		#self.send_header('Access-Control-Allow-Origin', 'http://plotomatic.com')
		#self.send_response(200)
		self.do_OPTIONS()

		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)

		print 'got a post request!'
		#now, send the data to azure
		resp_text = get_story(self.call_azure(post_body))
		self.wfile.write(resp_text)

	def call_azure(self, payload):
		url = "http://canadacentral.api.cognitive.microsoft.com/vision/v1.0/tag"
		headers = {
			'Ocp-Apim-Subscription-Key': "[MS AZURE API KEY GOES HERE]",
			'Content-Type': "application/octet-stream",
			'Cache-Control': "no-cache"
		}

		response = requests.request("POST", url, data=payload, headers=headers)

		print(response.text)
		return(response.text)

def run(server_class=HTTPServer, handler_class=S, port=8585):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd...'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
