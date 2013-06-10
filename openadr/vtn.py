import logging
from BaseHTTPServer import BaseHTTPRequestHandler

from openadr.util import *
from openadr.handlers.EiEventHandlers import OADR_MESSAGE_HANDLER
from openadr import config as oadrCfg



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

        # get incoming request data
        dlen = int(self.headers.getheader('content-length'))
        data = self.rfile.read(dlen)

        # get the url_path (partial url)
        url_path = self.path

        msg = 'VTN HTTP server received a request\n' \
              '    url path : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url_path, dlen, data)
        logging.debug(msg)

        resp_d = VTNMessageHandler(url_path, data)

        self.send_response(resp_d['code'])
        self.end_headers()
        self.wfile.write(resp_d['msg'])

        msg = 'VTN HTTP server sent the following response\n' \
              '          to : %s\n' \
              ' data length : %s\n' \
              '        data : %s\n' % \
              (self.client_address, resp_d['code'], resp_d['msg'])
        logging.debug(msg)

        return None



def VTNMessageHandler(url_path, data):

    resp_d = {'code': 200,
              'msg' : '' }

    # valid_incoming_data() retruns
    # request dictionary - req_d
    #
    # on failure: req_d['valid'] == False
    #   req_d['code']
    #   req_d['msg']
    #
    # on success: req_d['valid'] == True
    #   req_d['service']
    #   req_d['message']
    #   req_d['xml_h']
    req_d = valid_incoming_data(url_path, data)

    # on failure, send a http repsonse
    # with the following parameters
    #   req_d['code']
    #   req_d['msg']
    #
    if not req_d['valid']:
        return req_d

    # if the incoming request (url, xml schema,
    # message <-> service mapping, etc) is
    # validated and found legitimate then
    # process the message
    service   = req_d['service']
    message   = req_d['message']
    req_xml_h = req_d['xml_h']

    # get the message handler for the
    # respective oadr service
    MessageHandler = OADR_MESSAGE_HANDLER[service]

    resp_xml_s = MessageHandler(req_xml_h)
    #print 'resp_xml_s : %s' % resp_xml_s
    resp_d['msg'] = resp_xml_s

    return resp_d


