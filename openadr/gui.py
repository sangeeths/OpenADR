import logging 

from openadr import userconfig as usrCfg
from openadr import sysconfig as sysCfg

logging.basicConfig(filename=usrCfg.GUI_LOG_FILENAME,
                    stream=usrCfg.GUI_LOG_STREAM,
                    level=usrCfg.GUI_LOG_LEVEL,
                    format=usrCfg.GUI_LOG_FORMAT)

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler 

from openadr.util import *
from openadr.system import IPADDR, GUI_PORT

try:
    # configure the http server
    webHandler = CGIHTTPRequestHandler
    webHandler.cgi_directories = [sysCfg.GUI_URL_PATH]
    server = HTTPServer((IPADDR, GUI_PORT), webHandler)

    print_gui_startup_message()

    # start the http server and wait forever 
    # for the incoming http requests!
    server.serve_forever()

except KeyboardInterrupt:
    # stop the http server
    server.socket.close()
    print_gui_shutdown_message()


