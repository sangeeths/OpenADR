#import logging 
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler 

from openadr.system import IPADDR, PORT
from openadr import userconfig as usrCfg

#
#logging.basicConfig(filename=sysCfg.LOG_FILENAME,
#                    stream=sysCfg.LOG_STREAM,
#                    level=sysCfg.LOG_LEVEL,
#                    format=sysCfg.LOG_FORMAT)
#

try:
    # configure the http server
    webHandler = CGIHTTPRequestHandler
    webHandler.cgi_directories = ['/openadr/cgi-bin']
    server = HTTPServer((IPADDR, GUI_PORT), webHandler)

    # start the http server and wait forever 
    # for the incoming http requests!
    server.serve_forever()

except KeyboardInterrupt:
    # stop the http server
    server.socket.close()



