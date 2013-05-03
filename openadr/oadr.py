from openadr.config import *
from openadr.util import * 
import logging 

from BaseHTTPServer import HTTPServer
from openadr.ven import VENHttpServer
from openadr.vtn import VTNHttpServer
from openadr.vn import VNHttpServer

logging.basicConfig(filename=LOG_FILENAME,
                    stream=LOG_STREAM,
                    level=LOG_LEVEL,
                    format=LOG_FORMAT)



print_config()
print_start_config()

if NODE == OADR_NODE.VEN:
    port = HTTP_VEN_PORT
    httpHandler = VENHttpServer
elif NODE == OADR_NODE.VTN:
    port = HTTP_VTN_PORT
    httpHandler = VTNHttpServer
elif NODE == OADR_NODE.VN:
    port = HTTP_VN_PORT
    httpHandler = VNHttpServer
else:
    exit(1)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer((IPADDR, port), httpHandler)
    print '%s HTTP Server started on port %d' % (str(NODE), port)
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()



