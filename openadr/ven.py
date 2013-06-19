import logging
from BaseHTTPServer import BaseHTTPRequestHandler
import urllib2, urllib


from openadr.util import *

from openadr import sysconfig as sysCfg
from openadr import userconfig as usrCfg

from openadr.system import MODE, NODE

from openadr.services.EiEvent.EiEventMessages import compose_oadrRequestEvent_msg
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
    
        # poll for EiEvents from the registered VTN's 
        # only if the ven is running in PULL mode
        if MODE == sysCfg.OADR_MODE.PULL:
            poll_for_events() 


    @classmethod
    def HttpPreStopCallback(cls):
        pass


    @classmethod
    def HttpPostStopCallback(cls):
        pass


    def do_POST(self):

        # get incoming request data
        dlen = int(self.headers.getheader('content-length'))
        data = self.rfile.read(dlen)
        
        # get the url_path (partial url)
        url_path = self.path

        # TODO: client info : self.client_address

        msg = 'VEN HTTP Server received a request\n' \
              '    url path : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url_path, dlen, data)
        logging.debug(msg)

        resp_d = VENMessageHandler(url_path, data)

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


def VENMessageHandler(url_path, data):

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



#
# VEN (PULL) --------------------> VTN
#                RequestEvent 
#
def poll_for_events():

    print 'Polling for new EiEvents...'

    # this function is suppose to be called only when
    # you are a VEN and running in PULL mode
    if NODE != sysCfg.OADR_NODE.VEN:
        logging.debug('Attempting to poll for new Events ' \
                      'when not running as VEN.')
    if MODE != sysCfg.OADR_MODE.PULL:
        logging.debug('Attempting to poll for new Events ' \
                      'when not running in PULL mode.')
 
    nm = NodeManager()       
    nodes = nm.getAllNodes()
    for node in nodes:
        print str(node)
        if node.nodeType != sysCfg.OADR_NODE.VTN:
            continue
        urls = get_profile_urls(ipaddr=node.get_ipaddr(),
                                port=node.get_port(), 
                                prefix=node.get_prefix(),
                                profile=node.get_profile())
        request_url = urls[sysCfg.OADR_SERVICE.EiEvent]
        print "URLS : ", urls
        print "request_url : ", request_url
        
        oadrRE = compose_oadrRequestEvent_msg()
        print "oadrRE : ", oadrRE
        post_request(request_url, oadrRE)
     
        #request_data = urllib.urlencode(oadrRE)
        

def post_request(request_url, request_msg_s):

    msg_d = {'code' : 200,
             'msg'  : request_msg_s}

    my_event_url_path = get_url_paths()[sysCfg.OADR_SERVICE.EiEvent]

    while msg_d['msg'] is not None:
        req = urllib2.Request(request_url, msg_d['msg'])
        msg = 'VEN HTTP client sent the following request:\n' \
              '       to : %s\n' \
              '     data : %s\n' % \
              (request_url, msg_d['msg'])
        logging.info(msg)

        response_msg_s = urllib2.urlopen(req).read()
        msg = 'VEN HTTP client received a response:\n' \
              '    url path : %s\n' \
              '        data : %s\n' % \
              (my_event_url_path, response_msg_s)
        logging.info(msg)
        
        msg_d = VENMessageHandler(my_event_url_path, response_msg_s)


