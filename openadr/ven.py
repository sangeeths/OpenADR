from BaseHTTPServer import BaseHTTPRequestHandler
import urllib2
import urllib

from openadr import config as oadrCfg
from openadr.util import *
from openadr.services.EiEvent import manager as EiEventManager
from openadr.services.EiEvent.messages import compose_oadrRequestEvent_msg
from openadr.handlers.EiEventHandlers import OADR_MESSAGE_HANDLER

from openadr.node.NodeManager import NodeManager


class VENHttpServer(BaseHTTPRequestHandler):
    
    @classmethod
    def HttpPreStartCallback(cls):
        pass


    @classmethod
    def HttpPostStartCallback(cls):

        # print the current running setup
        print_startup_message()

        #
        # do the following in the Http Server Post Callback:
        #
        # 1. start XMPP server
        #   1.1 node descovery
        # 2. security, certificate exchange and authentication
        # 3. register polling function if current node is VEN 
        #    and current mode is PULL 
        #
        if oadrCfg.MODE == oadrCfg.OADR_MODE.PULL:
            poll_for_events() 


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
        url_prefix = self.path

        # TODO: client info : self.client_address

        msg = 'VEN HTTP Server received a request\n' \
              '  url prefix : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url_prefix, dlen, data)
    
        logging.debug(msg)

        resp_d = VENMessageHandler(url_prefix, data)

        self.send_response(resp_d['code'])
        self.end_headers()
        self.wfile.write(resp_d['msg'])
        
        msg = 'VEN HTTP Server sent the following response\n' \
              '          to : %s\n' \
              ' data length : %s\n' \
              '        data : %s\n' % \
              (self.client_address, resp_d['code'], resp_d['msg'])
    
        logging.debug(msg)

        return None


def VENMessageHandler(url_prefix, data):

    resp_d = {'code': 200,
              'msg' : '' }
    
    print 'VENMessageHandler :: Incoming :: url = %s, data = %s' % (url_prefix, data)

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
    req_d = valid_incoming_data(url_prefix, data)

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



#
# VEN (PULL) --------------------> VTN
#                RequestEvent 
#
def poll_for_events():

    print 'Polling for new EiEvents...'

    # this function is suppose to be called only when
    # you are a VEN and running in PULL mode
    if oadrCfg.NODE != oadrCfg.OADR_NODE.VEN:
        logging.debug('Attempting to poll for new Events ' \
                      'when not running as VEN.')
    if oadrCfg.MODE != oadrCfg.OADR_MODE.PULL:
        logging.debug('Attempting to poll for new Events ' \
                      'when not running in PULL mode.')
 
    nm = NodeManager()       
    nodes = nm.getAllNodes()
    for node in nodes:
        if node.nodeType != oadrCfg.OADR_NODE.VTN:
            continue
        urls = get_profile_urls(ipaddr=node.ipaddr,
                                port=node.port, 
                                prefix=node.prefix,
                                profile=node.profile)
        request_url = urls[oadrCfg.OADR_SERVICE.EiEvent]
        print "URLS : ", urls
        print "request_url : ", request_url
        
        oadrRE = compose_oadrRequestEvent_msg()
        print "oadrRE : ", oadrRE
        post_request(request_url, oadrRE)
     
        #request_data = urllib.urlencode(oadrRE)
        

def post_request(request_url, request_msg_s):

    msg_d = {'code' : 200,
             'msg'  : request_msg_s}

    my_event_url_prefix = get_url_prefix()[oadrCfg.OADR_SERVICE.EiEvent]

    while msg_d['msg'] is not None:
        print 'post_request : url = %s : sending = %s' % (request_url, msg_d['msg'])
        req = urllib2.Request(request_url, msg_d['msg'])
        response = urllib2.urlopen(req)
        response_msg_s = response.read()
        
        print 'post_request : url = %s : receiving = %s' % (my_event_url_prefix, response_msg_s)
        msg_d = VENMessageHandler(my_event_url_prefix, response_msg_s)


