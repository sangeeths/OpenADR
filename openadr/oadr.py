import logging 
from BaseHTTPServer import HTTPServer

from openadr import config as oadrCfg
from openadr.util import * 
from openadr.ven import VENHttpServer
from openadr.vtn import VTNHttpServer
from openadr.vn import VNHttpServer
from openadr.exception import InvalidOADRNodeType

logging.basicConfig(filename=oadrCfg.LOG_FILENAME,
                    stream=oadrCfg.LOG_STREAM,
                    level=oadrCfg.LOG_LEVEL,
                    format=oadrCfg.LOG_FORMAT)



# print_config_from_file()
print_startup_message()

try: 
    node = get_node_info(oadrCfg.NODE)
except InvalidOADRNodeType as e:
    print e.value
    exit(1)

try:
    server = HTTPServer((oadrCfg.IPADDR, node['port']), node['http_handler'])
    print '%s HTTP Server started on port %d' % (str(node['node']), node['port'])
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()



