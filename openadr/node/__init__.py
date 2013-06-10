

from openadr.util import *
from openadr import config as oadrCfg

from openadr.exception import InvalidOADRNodeType
from openadr.exception import InvalidOADRProfile


class Node:
    def __init__(self, nodeType, nodeId, ipaddr, port, 
                 prefix, profile=oadrCfg.OADR_PROFILE.A):
        if nodeType not in oadrCfg.OADR_NODE:
            raise InvalidOADRNodeType('Invalid Node Type : %s' % nodeType)
        if not self.valid_nodeId(nodeId):
            raise InvalidOADRNodeType('Invalid Node ID : %s' % nodeId)
        if profile not in oadrCfg.OADR_PROFILE:
            raise InvalidOADRProfile('Invalid OADR Profile : %s' % profile)
        self.profile = profile
        self.prefix = prefix
        self.port = port
        self.nodeType = nodeType
        self.nodeId = nodeId
        self.ipaddr = ipaddr
        

    def valid_nodeId(self, nodeId):
        return True

    def getDict(self):
        return self.__dict__

    def __str__(self):
        node_str  = 'Node:\n'
        node_str += '-----\n'
        node_str += '\tnodeType : \n' % self.nodeType
        node_str += '\tnodeId   : \n' % self.nodeId
        node_str += '\tipaddr   : \n' % self.ipaddr
        node_str += '\tport     : \n' % self.port
        node_str += '\tprefix   : \n' % self.prefix
        node_str += '\tprofile  : \n' % self.profile
        return node_str
