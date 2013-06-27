from openadr import sysconfig as sysCfg

from openadr.util2 import str_to_enum

from openadr.exception import ValueNotFound, \
                              InvalidOADRNodeType, \
                              InvalidOADRMode, \
                              InvalidOADRProfile


def get_node_type_from_str(nodeType):
    try:
        return str_to_enum(sysCfg.OADR_NODE, nodeType)
    except Exception, e:
        msg = 'Invalid OADR Node Type [%s]; Reason: %s' % \
              (nodeType, e)
        raise InvalidOADRNodeType(msg)


def get_mode_from_str(mode):
    try:
        return str_to_enum(sysCfg.OADR_MODE, mode)
    except Exception, e:
        msg = 'Invalid OADR Mode [%s]; Reason: %s' % \
              (mode, e)
        raise InvalidOADRMode(msg)


def get_profile_from_str(profile):
    try:
        return str_to_enum(sysCfg.OADR_PROFILE, profile)
    except Exception, e:
        msg = 'Invalid OADR Profile [%s]; Reason: %s' % \
              (profile, e)
        raise InvalidOADRProfile(msg)


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


