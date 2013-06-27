
#
# NOTE: DO NOT INCLUDE 
#   -> Node Manager
#   -> System Manager
#   -> EiEvent Manager
# 
# NOTE: include only openadr.exception 
#       and standard python packages/modules
#

import string
import ipaddr
import logging

from openadr.exception import *
from openadr import sysconfig as sysCfg


def valid_incoming_elements(expected, incoming):
    s1 = set(expected)
    s2 = set(incoming)
    missing_elements = list(s1.difference(s2))
    if not missing_elements:
        return True
    msg  = 'Expected Elements : %s \n' % expected
    msg += 'Incoming Elements : %s \n' % incoming
    msg += 'Missing Elements  : %s' % missing_elements
    raise InvalidIncomingElements(msg)


def valid_string(strval, allowed, min_len=None, max_len=None):
    if strval is None or allowed is None:
       return False

    allowed = set(allowed)
    entered = set(strval)
    not_allowed = entered.difference(allowed)
    if not_allowed:
        raise InvalidValue('%s should not contain %s' % \
                          (nodeId, not_allowed))

    strlen = len(strval)
    if min_len is None and max_len is None:
        return True
    
    if strlen < min_len or strlen > max_len:
        raise InvalidLength('length(%s) should be >%d and <%d' % \
                           (nodeId, min_len, max_len))
    return True 


def get_oadr_type(oadr_type, param):
    for item in oadr_type:
        if item.key == param:
            return item
    raise ValueNotFound('%s is not found in %s' % (param, oadr_type._keys))


def valid_node_type(nodeType):
    if nodeType in sysCfg.OADR_NODE._values:
        return True
    raise InvalidOADRNodeType('Invalid OADR Node Type : %s' % nodeType)


def valid_mode(mode):
    if mode in sysCfg.OADR_MODE._values:
        return True
    raise InvalidOADRMode('Invalid OADR Mode : %s' % mode)


def valid_profile(profile):
    if profile in sysCfg.OADR_PROFILE._values:
        return True
    raise InvalidOADRProfile('Invalid OADR Profile : %s' % profile)


def valid_node_id(nodeId):
    min_len = 5
    max_len = 15
    allowed = set(string.ascii_lowercase + \
                  string.digits + \
                  string.ascii_uppercase  + \
                  '_' + '-' + '.') 
    try:
        valid_string(nodeId, allowed, min_len, max_len)
        return True
    except Exception, e:
        raise InvalidOADRNodeId('Invalid OADR Node Id : %s' % nodeId)


def valid_ipaddr(ip):
    try:
        ip = ipaddr.IPAddress(ip)
        return True
    except Exception, e:
        raise InvalidIPaddress('Invalid IP Address - %s' % ip)


def valid_port(port):
    return True


def valid_prefix(prefix):
    min_len = 3
    max_len = 15
    allowed = set(string.ascii_lowercase + \
                  string.digits + \
                  string.ascii_uppercase  + \
                  '_' + '-') 
    try:
        valid_string(prefix, allowed, min_len, max_len)
        return True
    except Exception, e:
        raise InvalidOADRURLPrefix('Invalid OADR URL Prefix : %s' % prefix)


def valid_summary(summary):
    min_len = 15
    max_len = 100
    allowed = set(string.ascii_lowercase + \
                  string.digits + \
                  string.ascii_uppercase  + \
                  '_' + '-' + '(' + ')' + ' ' + '&') 
    try:
        valid_string(summary, allowed, min_len, max_len)
        return True
    except Exception, e:
        raise InvalidOADRSummary('Invalid OADR Summary : %s' % summary)





def get_node_type_from_str(nodeType):
    try:
        return get_oadr_type(sysCfg.OADR_NODE, nodeType)
    except Exception, e:
        logging.debug(e)
        raise InvalidOADRNodeType('Invalid OADR Node Type : %s' % nodeType)


def get_mode_from_str(mode):
    try:
        return get_oadr_type(sysCfg.OADR_MODE, mode)
    except Exception, e:
        logging.debug(e)
        raise InvalidOADRMode('Invalid OADR Mode : %s' % mode)


def get_profile_from_str(profile):
    try:
        return get_oadr_type(sysCfg.OADR_PROFILE, profile)
    except Exception, e:
        logging.debug(e)
        raise InvalidOADRProfile('Invalid OADR Profile : %s' % profile)


def node_str_to_enum(node_d, sysNode=False):
    node_d['nodeType'] = get_node_type_from_str(node_d['nodeType'])
    if sysNode:
        node_d['mode']    = get_mode_from_str(node_d['mode'])
        node_d['profile'] = get_profile_from_str(node_d['profile'])
    return node_d


def node_enum_to_str(node_d, sysNode=False):
    node_d['nodeType'] = str(node_d['nodeType'])
    #node_d['nodeType'] = node_d['nodeType'].key
    if sysNode:
        #node_d['mode']    = node_d['mode'].key
        #node_d['profile'] = node_d['profile'].key
        node_d['mode']    = str(node_d['mode'])
        node_d['profile'] = str(node_d['profile'])
    return node_d






