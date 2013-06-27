from openadr import sysconfig as sysCfg

from openadr.node import NodeConfig as nodeCfg

from openadr.validation import valid_string

from openadr.exception import InvalidOADRNodeType, \
                              InvalidOADRMode, \
                              InvalidOADRProfile, \
                              InvalidOADRNodeId, \
                              InvalidOADRURLPrefix, \
                              InvalidOADRSummary


def valid_node_type(nodeType):
    if nodeType in sysCfg.OADR_NODE._values:
        return True
    msg = 'Invalid OADR Node Type [%s]' % nodeType
    raise InvalidOADRNodeType(msg)


def valid_mode(mode):
    if mode in sysCfg.OADR_MODE._values:
        return True
    msg = 'Invalid OADR Mode [%s]' % mode
    raise InvalidOADRMode(msg)


def valid_profile(profile):
    if profile in sysCfg.OADR_PROFILE._values:
        return True
    msg = 'Invalid OADR Profile [%s]' % profile
    raise InvalidOADRProfile(msg)


def valid_node_id(nodeId):
    n = nodeCfg.VALID_NODE_STRING['nodeId']
    try:
        valid_string(nodeId, n['allowed'], n['min_len'], n['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid OADR Node Id [%s]; Reason: %s' % \
              (nodeId, e)
        raise InvalidOADRNodeId(msg)


def valid_prefix(prefix):
    n = nodeCfg.VALID_NODE_STRING['prefix']
    try:
        valid_string(prefix, n['allowed'], n['min_len'], n['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid OADR URL Prefix [%s]; Reason: %s' % \
              (prefix, e)
        raise InvalidOADRURLPrefix(msg)


def valid_summary(summary):
    n = nodeCfg.VALID_NODE_STRING['summary']
    try:
        valid_string(summary, n['allowed'], n['min_len'], n['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid OADR Summary [%s]: Reason: %s' % \
              (summary, e)
        raise InvalidOADRSummary(msg)


