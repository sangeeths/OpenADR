
#
# NOTE: DO NOT import the following:
#   -> Node Manager
#   -> System Manager
#   -> EiEvent Manager
# 

import ipaddr

from openadr.exception import InvalidIncomingElements, \
                              InvalidValue, \
                              InvalidLength, \
                              InvalidInteger, \
                              InvalidPositiveInteger, \
                              InvalidFloatingPoint, \
                              InvalidIPaddress, \
                              InvalidPort


def valid_incoming_elements(expected, incoming):
    s1 = set(expected)
    s2 = set(incoming)
    missing_elements = list(s1.difference(s2))
    if not missing_elements:
        return True
    msg = 'Expected Elements : %s \n' \
          'Incoming Elements : %s \n' \
          'Missing Elements  : %s' % \
          (expected, incoming, missing_elements)
    raise InvalidIncomingElements(msg)


def valid_string(strval, allowed, min_len=None, max_len=None):
    # strval and allowed are mandatory parameters
    # return False if at least on of them in None
    if strval is None or allowed is None:
       return False
    if (min_len is None and max_len is not None) or \
       (min_len is not None and max_len is None):
        return False
    # NOTE: There has to be a better way of validating 
    #       string. This is just absurd and insane to 
    #       use set functions for this!
    # convert the strval and allowed to set 
    # and run the set difference
    allowed = set(allowed)
    entered = set(strval)
    not_allowed = entered.difference(allowed)
    if not_allowed:
        msg = 'Invalid character(s) found in String [%s]; ' \
              'Invalid [%s]' % (strval, not_allowed)
        raise InvalidValue(msg)
    # min_len <= len(strval) <= max_len
    strlen = len(strval)
    if strlen >= min_len and strlen <= max_len:
        return True 
    msg = 'Invalid String Length(%s) [%d]; min_len [%d]; ' \
          'max_len [%d]' % (strval, strlen, min_len, max_len)
    raise InvalidLength(msg)


def valid_integer(intval):
    try:
        int(intval)
        return True
    except Exception, e:
        msg = 'Invalid Integer [%s]; Reason: %s' % \
              (intval, e)
        raise InvalidInteger(msg)


def valid_positive_integer(intval):
    val = valid_integer(intval)
    if val >= 0: 
        return True
    msg = 'Invalid Positive Integer [%s]' % intval
    raise InvalidPositiveInteger(msg)


def valid_float(floatval):
    try:
        int(floatval)
        return True
    except Exception, e:
        msg = 'Invalid Floating Point Value [%s]' % \
              (floatval)
        raise InvalidFloatingPoint(msg)


def valid_ipaddr(ip):
    try:
        ip = ipaddr.IPAddress(ip)
        return True
    except Exception, e:
        msg = 'Invalid IP Address [%s]; Reason: %s' % \
              (ip if ip is not None else 'None', e)
        raise InvalidIPaddress(msg)


def valid_port(port):
    try:
        valid_integer(port)
        return True
    except Exception, e:
        msg = 'Invalid Port [%s]; Reason: %s' % \
              (port, e)
        raise InvalidPort(msg)


