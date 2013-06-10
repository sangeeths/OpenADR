import logging 
from BaseHTTPServer import HTTPServer


from openadr import config as oadrCfg
from openadr.util import * 
from openadr.exception import InvalidOADRNodeType
from openadr.handlers.httpHandlers import HttpHandler

logging.basicConfig(filename=oadrCfg.LOG_FILENAME,
                    stream=oadrCfg.LOG_STREAM,
                    level=oadrCfg.LOG_LEVEL,
                    format=oadrCfg.LOG_FORMAT)


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
    server = oadrHTTPServer((oadrCfg.IPADDR, oadrCfg.CONFIG['port']), HttpHandler)

    # start the http server and wait forever 
    # for the incoming http requests!
    server.serve_forever()

except KeyboardInterrupt:
    # stop the http server
    server.socket.close()



