from BaseHTTPServer import BaseHTTPRequestHandler
import urllib2
import urllib

from openadr import config as oadrCfg
from openadr.util import *
from openadr.services.EiEvent import manager as EiEventManager
from openadr.services.EiEvent.message import compose_oadrRequestEvent_msg
from openadr.msgHandlers import OADR_MESSAGE_HANDLER


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
    
    @classmethod
    def pre_start_cb(cls):
        print 'VENHttpServer_pre_start_cb'

    @classmethod
    def post_start_cb(cls):
        print 'VENHttpServer_post_start_cb'
        urls = get_profile_urls(ipaddr=oadrCfg.ENTITY['ipaddr'], 
                                port=oadrCfg.ENTITY['port'], 
                                prefix=oadrCfg.ENTITY['prefix'],
                                profile=oadrCfg.ENTITY['profile'])
        request_url = urls[oadrCfg.OADR_SERVICE.EiEvent]
        print "URLS : ", urls
        print "request_url : ", request_url
        
        oadrRE = compose_oadrRequestEvent_msg()
        print "oadrRE : ", oadrRE
 
        #request_data = urllib.urlencode(oadrRE)
        
        req = urllib2.Request(request_url, oadrRE)
        response = urllib2.urlopen(req)
 
        print "response = ", response.read()
 
   


    @classmethod
    def pre_stop_cb(cls):
        print 'VENHttpServer_pre_stop_cb'

    @classmethod
    def post_stop_cb(cls):
        print 'VENHttpServer_post_stop_cb'

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

        resp_d = VENMessageHandler(url, data)

        self.send_response(resp_d['code'])
        self.end_headers()
        self.wfile.write(resp_d['msg'])

        return


def VENMessageHandler(url, data):

    resp_d = {'code': 200,
              'msg' : '' }
    
    print 'VENMessageHandler :: Incoming :: url = %s, data = %s' % (url, data)

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


