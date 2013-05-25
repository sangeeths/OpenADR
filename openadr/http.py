from openadr import config as oadrCfg

from openadr.ven import VENHttpServer, VENHttpServerStartCB
from openadr.vtn import VTNHttpServer, VTNHttpServerStartCB
from openadr.vn import VNHttpServer, VNHttpServerStartCB

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
                     oadrCfg.OADR_NODE.VN:  VNHttpServer
                    }

HttpHandler = OADR_HTTP_HANDLER[oadrCfg.NODE]

#
# the following are the callback functions 
# which are called for the respective nodes
# right after the HTTP server is started
#
# this callback function can be used for 
# registration with VEN/VTN, authentication, 
# polling, pull request, etc.
# 
OADR_HTTP_START_CB = {oadrCfg.OADR_NODE.VEN: VENHttpServerStartCB,
                      oadrCfg.OADR_NODE.VTN: VTNHttpServerStartCB,
                      oadrCfg.OADR_NODE.VN:  VNHttpServerStartCB
                     }

HttpServerStartCB = OADR_HTTP_START_CB[oadrCfg.NODE]


