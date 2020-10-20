import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self.path = 'web/index.html'


            stuff = os.listdir("web/")
            print(stuff)

        try:
     
            file_to_open = open(self.path).read()
            print("File to open: {}".format(file_to_open))
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def run():
    httpd = HTTPServer(('localhost', 6900), Serv)
    httpd.serve_forever()


run()

