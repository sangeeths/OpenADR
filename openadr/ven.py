from BaseHTTPServer import BaseHTTPRequestHandler

from openadr import config as oadrCfg
from openadr.util import *
from openadr.xml import *

class VENHttpServer(BaseHTTPRequestHandler):
    def do_POST(self):
        
        # get the url and data
        dlen = int(self.headers.getheader('content-length'))
        data = self.rfile.read(dlen)
        url  = self.path

        msg = 'VEN HTTP Server received a request\n' \
              '         url : %s\n' \
              ' data length : %d\n' \
              '        data : %s\n' % \
              (url, dlen, data)

        logging.debug(msg)

        response = process_ven_message(url, data)

        self.send_response(response['code'])
#        self.send_header('Content-type',self.headers['Content-Type'])
        self.end_headers()
        self.wfile.write(response['msg'])


def process_ven_message(url, xml):
    
    #
    # return this dict at any stage of processing
    #   http_resp['code'] = http response code
    #   http_resp['msg']  = response message for the
    #                       operation performed on 
    #                       incoming 'xml'
    #
    http_resp = {'code':200, 'msg': 'Alright!!'}

    service = valid_url(url)
    if service is None: 
        msg = 'Invalid Request URL - %s\n' \
              'Currently supported OpenADR Services ' \
              'and its URL are as follows: \n' % (url)
        urls = get_profile_urls()
        for service, url in urls.iteritems():
            msg += '%15s : %s\n' % (service.key, url)
        http_resp['msg'] = msg
        print msg
        logging.info(msg)
        return http_resp

    xml_h = valid_oadr_xml(xml)
    if xml_h is None:
        msg = 'The incoming XML data is not ' \
              'compliant with OpenADR %s Profile ' \
              'Schema\n' % (oadrCfg.PROFILE)
        http_resp['msg'] = msg
        print msg
        logging.info(msg)
        return http_resp

    oadr_msg = get_oadr_msg(service, xml_h)
    if oadr_msg is None:
        msg = '%s is not a valid %s service message\n' % \
              (root_element(xml_h), service.key) 
        http_resp['msg'] = msg
        print msg
        logging.info(msg)
        return http_resp
        
    if not valid_profile_msg(oadrCfg.OADR_OP.RECV, oadr_msg):
        msg = '%s is not subjected to receive (%s\'s) %s ' \
              'message\n' % (oadrCfg.CONFIG['node_str'], 
              oadr_msg.key, service.key) 
        http_resp['msg'] = msg
        print msg
        logging.info(msg)
        return http_resp

    # return the default response 
    # code and message
    return http_resp
        
