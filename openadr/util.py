import logging

from lxml import etree
from io import BytesIO

from openadr import config as oadrCfg
from openadr.exception import InvalidOADRNodeType

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
    print 'goodbye!\n'

#
# this function returns a dict 
#   key   = OADR_SERVICE.<service-name>
#   value = partial url_path(s) for all the 
#           all services in the given profile
#  
def get_url_paths(prefix=oadrCfg.CONFIG['prefix'],
                  profile=oadrCfg.PROFILE):
    url_paths = {}
    if prefix is not None:
        prefix = '/' + prefix
    for service in oadrCfg.SERVICE[profile]:
        url_paths[service] = '%s/OpenADR2/Simple/%s' % \
                             (prefix, service.key)
    return url_paths


#
# this function returns a dict 
#   key   = OADR_SERVICE.<service-name>
#   value = absolute url for the service
#  
def get_profile_urls(ipaddr=oadrCfg.IPADDR, 
                     port=oadrCfg.CONFIG['port'],
                     prefix=oadrCfg.CONFIG['prefix'],
                     profile=oadrCfg.PROFILE):

    # dict which contains service url
    # for the given profile 
    urls = {}

    # compose the port number for url
    port = ':' + str(port) 
    
    # compose the prefix string for the url
    prefix = prefix + '/' 
    
    # compose base url
    base_url = 'http://%s%s/%sOpenADR2/Simple/' % \
               (ipaddr, port, prefix)

    # final url = base url + OADR_SERVICE
    for service in oadrCfg.SERVICE[profile]:
        urls[service] = base_url + service.key

    return urls

#
# the incoming 'url_path' is a partial url_path 
# which contains the following:
#   1. prefix (optional)
#   2. 'OpenADR2/Simple'
#   3. OADR_SERVICE
#   
#   [/prefix]/OpenADR2/Simple/<OADR_SERVICE>
#
# success: 
#   for valid url_path, OADR_SERVICE.<service-name> 
#   is returned 
#
# failure:
#   for invalid url_path, None is returned
#
def valid_url_path(url_path):
    url_paths = get_url_paths()
    for service, path in url_paths.iteritems():
        if url_path == path:
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
# validates whether the incoming xml 
# data (string) is compliance with the
# OpenADR Schema
#
# if valid xml document, returns lxml 
# handle to the incoming document
#
# if invalid xml document, returns None
#
def valid_oadr_xml(xml_s):

    # get oadr schema handle
    #   oadr_schema_f = handle to the schema file
    #   oadr_schema_h = lxml handle to the schema xml
    #   oadr_schema   = this is the schema handle that 
    #                   should be used against all the 
    #                   incoming xml data
    #
    with open(oadrCfg.XSD[oadrCfg.PROFILE], 'r') as oadr_schema_f:
        oadr_schema_h = etree.parse(oadr_schema_f)
    oadr_schema = etree.XMLSchema(oadr_schema_h)

    # get lxml handle for the incoming xml data 
    try:
        xml_h = etree.parse(BytesIO(xml_s))
    except Exception, e:
        logging.info(repr(e))
        return None

    compliance = oadr_schema.validate(xml_h)
    #compliance = oadr_schema.assertValid(xml_h)
    print 'compliance : ', compliance

    # if the incoming xml adhere to the 
    # OpenADR Profile Schema then return
    # the lxml handle, else return None
    #
    if compliance is True: return xml_h
    else: return None


# TODO: find lxml way of getting
#       the root element
def root_element(xml_h):
    return xml_h.xpath('local-name()')


#
# for the given service and lxml handle
# to the xml data, this function finds 
# the name of the oadr message
#
# returns None if invalid message
#
def get_oadr_msg(service, xml_h):
    root = root_element(xml_h)
    for msg in oadrCfg.SERVICE_MESSAGE[service]:
        if root == msg.key:
            return msg
    return None

#
# for the given xml document, return a dict 
# which contains the namespace url and its
# respective namespace prefix
#
# if reverse=True then return
# dict = {url: nsprefix}
#
# if reverse=False then return
# dict = {nsprefix: url}
#
def get_ns(xml_h, reverse=False):
    # convert the incoming is etree.parse handler
    # to etree.XML so that we can get nsmap easily
    xml = etree.XML(etree.tostring(xml_h))

    # TIP: nsmap returns only the namespace in the
    #      root element of the given xml document.
    #      to get all namespaces in the given xml
    #      document, iterate through all elements
    #      and get the nsmap for each element
    root = xml_h.getroot()
    ns = {}
    for element in root.iter():
        for nsprefix, url in element.nsmap.iteritems():
            ns[nsprefix] = url

    # reverse dictionaring!! ;)
    if reverse:
        ns = dict((v, k) for k, v in ns.iteritems())

    return ns


def get_schema_ns(prefix=None):
    ns = {}
    for schema_file in oadrCfg.XSD_NS[oadrCfg.PROFILE]:
        with open(schema_file, 'r') as oadr_schema_f:
            oadr_schema = oadr_schema_f.read()
        oadr_schema_h = etree.XML(oadr_schema)
        # union of two dict - ns and nsmap
        ns = dict(oadr_schema_h.nsmap, **ns)
    
    if prefix is None: return ns 
 
    # if namespace of a particular prefix
    # is required, then iterate through ns
    # dict and fetch the correct ns for 
    # the incoming prefix   
    for key, value in ns.iteritems():
        if key == prefix: return value

    return None


#
# this function is called to validate 
# the incoming http url_path and data
#
# the following validation are performed:
#   1. valid url_path
#   2. valid xml data 
#   3. oadr-service <-> oadr-msg mapping
#   4. oadr-node (ven/vtn) <-> oadr-msg mapping
#
# returns a dict - ret_d 
# ret_d = return dictionary
#   ret_d['valid'] -> True/False
#
# on success (ret_d['valid'] == True):
#       variable            example
#   ret_d['service'] -> oadrCfg.OADR_SERVICE.EiEvent
#   ret_d['message'] -> oadrCfg.OADR_EIEVENT.oadrDistributeEvent
#   ret_d['xml_h']   -> lxml handle to the incoming 
#                       oadr xml message
#
# on failure (ret_d['valid'] == False):
#       variable         example
#   ret_d['code'] -> 200
#   ret_d['msg']  -> 'Sample message'
#
def valid_incoming_data(url_path, xml):

    ret_d= {'valid' : False,
            'code'  : 200,
            'msg'   : ''
           }

    service = valid_url_path(url_path)
    if service is None:
        msg = 'Invalid Request URL - %s\n' \
              'Currently supported OpenADR Services ' \
              'and its URL are as follows: \n' % (url_path)
        urls = get_profile_urls()
        for svc, url in urls.iteritems():
            msg += '%15s : %s\n' % (svc.key, url)
        ret_d['msg'] = msg
        logging.info(msg)
        return ret_d

    xml_h = valid_oadr_xml(xml)
    if xml_h is None:
        msg = 'The incoming XML data is not ' \
              'compliant with OpenADR %s Profile ' \
              'Schema\n' % (oadrCfg.PROFILE)
        ret_d['msg'] = msg
        logging.info(msg)
        return ret_d

    message = get_oadr_msg(service, xml_h)
    if message is None:
        msg = '%s is not a valid %s service message\n' % \
              (root_element(xml_h), service.key)
        ret_d['msg'] = msg
        logging.info(msg)
        return ret_d

    if not valid_profile_msg(oadrCfg.OADR_OP.RECV, message):
        msg = '%s is not subjected to receive (%s\'s) %s ' \
              'message\n' % (oadrCfg.CONFIG['node_str'],
              service.key, message.key)
        ret_d['msg'] = msg
        logging.info(msg)
        return ret_d

    # on success, return the following.
    del ret_d['code']
    del ret_d['msg']
    ret_d['service'] = service
    ret_d['message'] = message
    ret_d['xml_h']   = xml_h
    ret_d['valid'] = True
    
    return ret_d


def elements_exist(expected, incoming):
    s1 = set(expected)
    s2 = set(incoming)
    return list(s1.difference(s2))


