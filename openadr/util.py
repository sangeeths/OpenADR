import logging

from openadr import config as oadrCfg
from openadr.exception import InvalidOADRNodeType
from openadr.exception import ProfileNotImplemented

#
# this function returns a dict 
#   key   = OADR_SERVICE.<service-name>
#   value = absolute url for the service
#  
def get_profile_urls():

    # dict which contains service url
    # for the given profile 
    urls = {}

    # compose the port number for url
    port = ''
    if oadrCfg.CONFIG['port']:
        port = ':' + str(oadrCfg.CONFIG['port']) 
    
    # compose the prefix string for the url
    prefix = ''
    if oadrCfg.CONFIG['prefix']:
        prefix = oadrCfg.CONFIG['prefix'] + '/' 
    
    # compose base url
    base_url = 'http://%s%s/%sOpenADR2/Simple/' % \
               (oadrCfg.IPADDR, port, prefix)

    # final url = base url + OADR_SERVICE
    for service in oadrCfg.SERVICE[oadrCfg.PROFILE]:
        urls[service] = base_url + service.key

    return urls

#
# the incoming 'url' is the relative path which
# contains prefix (optional), OpenADR2/Simple, 
# and service name
#   
#   [/prefix]/OpenADR2/Simple/<OADR_SERVICE>
#
# success: 
# for valid url, OADR_SERVICE.<service-name> 
# is returned 
#
# failure:
# for invalid url, None is returned
#
def valid_url(url):

    base_url = ''
    
    # if optional prefix is present, then 
    # add that to the relative url
    if oadrCfg.CONFIG['prefix']: 
        base_url = '/' + oadrCfg.CONFIG['prefix'] 

    base_url += '/OpenADR2/Simple/'

    for service in oadrCfg.SERVICE[oadrCfg.PROFILE]:
        if url == base_url + service.key:
            return service    

    return None

#
# return true if the incoming oadr message
# is valid (and allowed/expected) to be 
# received at the current NODE.
#
# return false if the NODE (ven/vtn/vn) is 
# not expected to receive this messsage but 
# received it!
#
def valid_profile_msg(op, oadr_msg):
    for msg in oadrCfg.MESSAGE[oadrCfg.PROFILE][oadrCfg.NODE][op]:
        if oadr_msg == msg:
            return True
    return False

#
# print the following information
#   -> OADR_NODE - VEN, VTN or VN
#   -> OADR_MODE - PULL, PUSH
#   -> IP Address 
#   -> HTTP Server Port
#   -> OADR_PROFILE - A, B or C
#   -> List of service urls
#
# NOTE: this function will be called 
#       only during start up to display
#       some useful information
#
def print_startup_message():

    # compose the config string
    msg = 'Starting OpenADR %s in %s mode on %s ' \
          'at port %d configured for openADR 2.0 %s ' \
          'profile schema.\n\n' % (
          oadrCfg.CONFIG['node_str'], 
          oadrCfg.MODE.key, 
          oadrCfg.IPADDR, 
          oadrCfg.CONFIG['port'], 
          oadrCfg.PROFILE.key)

    # print url information for the given node
    urls = get_profile_urls()
    for service, url in urls.iteritems():
        msg += '\t%15s : %s\n' % (service.key, url)
    msg += '\n'

    print msg
    logging.info(msg)
    
    return

#
# print shutdown message, if any.
# else, pass.
#
def print_shutdown_message():
    print '\nShutting down OpenADR %s\n' % \
          oadrCfg.CONFIG['node_str']
    print 'Good bye!\n'

