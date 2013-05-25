from BaseHTTPServer import BaseHTTPRequestHandler

def VTNHttpServerStartCB():
    print "This is VTN Server Start Callback"

class VTNHttpServer(BaseHTTPRequestHandler):
    def do_POST(self):
        print "This is vtn.py:VTNHttpServer"
        print "CONTENT TYPE   = ", self.headers['Content-Type']
        print "CONTENT LENGTH = ", self.headers['Content-Length']
        print "CONTENT DATA   = "
        length = int(self.headers.getheader('content-length'))
        print self.rfile.read(length)

        self.send_response(200)
        self.send_header('Content-type',self.headers['Content-Type'])
        self.end_headers()

