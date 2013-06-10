from openadr import config as oadrCfg
from openadr.util import *

from openadr.services.EiEvent import manager as EiEventManager    

import logging
from BaseHTTPServer import BaseHTTPRequestHandler

from openadr.msgHandlers import OADR_MESSAGE_HANDLER


def VTNHttpServerStartCB():
    print "This is VTN Server Start Callback"

class VTNHttpServer(BaseHTTPRequestHandler):

    @classmethod
    def HttpPreStartCallback(cls):
        pass 


    @classmethod
    def HttpPostStartCallback(cls):
        # print the current running setup
        print_startup_message()



    @classmethod
    def HttpPreStopCallback(cls):
        pass

    @classmethod
    def HttpPostStopCallback(cls):

        # print goodbye message!
        print_shutdown_message()


    def do_POST(self):

        # get the url and data
        dlen = int(self.headers.getheader('content-length'))
        data = self.rfile.read(dlen)
        url  = self.path

        # TODO: client info : self.client_address

        msg = 'VTN HTTP Server received a request\n' \
              '         url : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url, dlen, data)

        logging.debug(msg)

        resp_d = VTNMessageHandler(url, data)

        self.send_response(resp_d['code'])
        self.end_headers()
        self.wfile.write(resp_d['msg'])

        msg = 'VTN HTTP Server sent the following response\n' \
              '      to : %s\n' \
              '    code : %s\n' \
              ' message : %s\n' % \
              (self.client_address, resp_d['code'], resp_d['msg'])

        logging.debug(msg)

        return None



def VTNMessageHandler(url, data):

    resp_d = {'code': 200,
              'msg' : '' }

    print 'VTNMessageHandler :: Incoming :: url = %s, data = %s' % (url, data)

    # valid_incoming_data() retruns
    # request dictionary - req_d
    #
    # on failure: req_d['valid'] == False
    #   req_d['code']
    #   req_d['msg']
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
        return req_d

    # if the incoming is validated and found
    # legitimate then process the message
    service   = req_d['service']
    message   = req_d['message']
    req_xml_h = req_d['xml_h']

    MessageHandler = OADR_MESSAGE_HANDLER[service]
    resp_xml_s = MessageHandler(req_xml_h)
    print 'resp_xml_s : %s' % resp_xml_s
    resp_d['msg'] = resp_xml_s

    return resp_d


