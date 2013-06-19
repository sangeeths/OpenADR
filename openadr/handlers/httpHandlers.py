from openadr import sysconfig as sysCfg

from openadr.system import NODE

from openadr.ven import VENHttpServer
from openadr.vtn import VTNHttpServer
from openadr.vn  import VNHttpServer

#
# NOTE: ideally the http_handler for the 
#       current NODE should be part of 
#       config.py::CONFIG['http_handler']
#       but importing the following in 
#       config.py leads to circular import
#           -> openadr.vtn.VTNHttpServer
#           -> openadr.ven.VENHttpServer
#           -> openadr.vn.VNHttpServer
#       so to avoid the circular import
#       this file has been introduced
#       for time being.
#
# TODO: find a way to push the http_handler
#       to config.py
#
OADR_HTTP_HANDLER = {sysCfg.OADR_NODE.VEN: VENHttpServer,
                     sysCfg.OADR_NODE.VTN: VTNHttpServer,
                     sysCfg.OADR_NODE.VN:  VNHttpServer
                    }

HttpHandler = OADR_HTTP_HANDLER[NODE]


