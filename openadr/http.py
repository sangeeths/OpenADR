from openadr import config as oadrCfg
from openadr.ven import VENHttpServer
from openadr.vtn import VTNHttpServer
from openadr.vn import VNHttpServer

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
OADR_HTTP_HANDLER = {oadrCfg.OADR_NODE.VEN: VENHttpServer,
                     oadrCfg.OADR_NODE.VTN: VTNHttpServer,
                     oadrCfg.OADR_NODE.VN:  VNHttpServer}

HttpHandler = OADR_HTTP_HANDLER[oadrCfg.NODE]



