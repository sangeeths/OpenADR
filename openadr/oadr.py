import logging 
from openadr import userconfig as usrCfg

logging.basicConfig(filename=usrCfg.LOG_FILENAME, 
                    stream=usrCfg.LOG_STREAM, 
                    level=usrCfg.LOG_LEVEL, 
                    format=usrCfg.LOG_FORMAT)


from BaseHTTPServer import HTTPServer

from openadr.util import * 
from openadr.system import IPADDR, PORT, NODE
from openadr.handlers.httpHandlers import HttpHandler


# Subclass HTTPServer with some additional callbacks
class oadrHTTPServer(HTTPServer):

    def server_activate(self):
        self.RequestHandlerClass.HttpPreStartCallback()
        HTTPServer.server_activate(self)
        self.RequestHandlerClass.HttpPostStartCallback()

    def server_close(self):
        self.RequestHandlerClass.HttpPreStopCallback()
        HTTPServer.server_close(self)
        self.RequestHandlerClass.HttpPostStopCallback()


try:
    # configure the http server
    server = oadrHTTPServer((IPADDR, PORT), HttpHandler)

    # start the http server and wait forever 
    # for the incoming http requests!
    server.serve_forever()

except KeyboardInterrupt:
    # stop the http server
    server.socket.close()
    print_shutdown_message()


