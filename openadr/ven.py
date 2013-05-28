from BaseHTTPServer import BaseHTTPRequestHandler

from openadr import config as oadrCfg
from openadr.util import *
from openadr.services.EiEvent import manager as EiEventManager

def VENHttpServerStartCB():
    print "this is VEN Http Server Start Callback"

    # TODO: perform registration with VTN
    # TODO: securtiy - tls 1.0

    #
    # if running in PULL mode then send
    # oadrRequestEvent message to the VTN
    #
    if oadrCfg.MODE == oadrCfg.HTTP_MODE.PULL:
        eievent = EiEvent()
        eievent.poll()
 

class VENHttpServer(BaseHTTPRequestHandler):
    def do_POST(self):
        
        # get the url and data
        dlen = int(self.headers.getheader('content-length'))
        data = self.rfile.read(dlen)
        url  = self.path

        # TODO: client info : self.client_address

        msg = 'VEN HTTP Server received a request\n' \
              '         url : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url, dlen, data)

        logging.debug(msg)

        print get_schema_ns()

        # valid_incoming_data() retruns 
        # request dictionary - req_d
        #
        # on failure: req_d['valid'] == False
        #   req_d['http_resp_code']
        #   req_d['http_resp_msg']
        #
        # on success: req_d['valid'] == True
        #   req_d['oadr_service']
        #   req_d['oadr_message']
        #   req_d['oadr_msg_xml_h']
        req_d = valid_incoming_data(url, data)
    
        # on failure, send a http repsonse 
        # with the following parameters
        #   req_d['http_resp_code']
        #   req_d['http_resp_msg']
        #
        if not req_d['valid']:
            self.send_response(req_d['http_resp_code'])
            self.end_headers()
            self.wfile.write(req_d['http_resp_msg'])
            return

        msg_d = process_ven_message(req_d['oadr_service'],
                                    req_d['oadr_message'],
                                    req_d['oadr_xml_msg_h'])

        self.send_response(msg_d['http_resp_code'])
        self.end_headers()
        self.wfile.write(msg_d['http_resp_msg'])
        return

def process_ven_message(service, message, xml_h):

    msg_d= {'http_resp_code': 200,
            'http_resp_msg' : ''
           }

    print 'processing service: %s, message: %s, xml_handle: %s' % \
          (service, message, xml_h)

    if service == oadrCfg.OADR_SERVICE.EiEvent:
        response_xml_s = EiEventManager.Response(xml_h)
        print 'response_xml_s : %s' % response_xml_s

    return msg_d


