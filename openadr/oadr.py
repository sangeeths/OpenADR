import logging 
from BaseHTTPServer import HTTPServer


from openadr import config as oadrCfg
from openadr.util import * 
from openadr.exception import InvalidOADRNodeType
from openadr.http import HttpHandler, HttpServerStartCB

logging.basicConfig(filename=oadrCfg.LOG_FILENAME,
                    stream=oadrCfg.LOG_STREAM,
                    level=oadrCfg.LOG_LEVEL,
                    format=oadrCfg.LOG_FORMAT)

try:
    server = HTTPServer((oadrCfg.IPADDR, oadrCfg.CONFIG['port']), HttpHandler)

    # print the current running setup
    print_startup_message()

    # wait forever for incoming http requests!
    server.serve_forever()

    # this is unreachable code as of now!!
    # TODO: find a way to make a callback
    HttpServerStartCB()
    
except KeyboardInterrupt:
    print_shutdown_message()
    server.socket.close()



