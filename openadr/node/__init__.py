#import logging 
from openadr import sysconfig as sysCfg

from openadr.exception import InvalidOADRNodeType, InvalidOADRNodeID, \
                              InvalidIPaddress, InvalidPort, \
                              InvalidOADRURLPrefix, InvalidOADRProfile, \
                              InvalidOADRMode


def oadr_node_from_str(node):
    for n in sysCfg.OADR_NODE:
        if n.key == node:
            return n
    raise InvalidOADRNodeType('Invalid OADR Node Type : %s' % node)

def oadr_profile_from_str(profile):
    for p in sysCfg.OADR_PROFILE:
        if p.key == profile:
            return p
    raise InvalidOADRProfile('Invalid OADR Profile : %s' % profile)

def oadr_mode_from_str(mode):
    for m in sysCfg.OADR_MODE:
        if m.key == mode:
            return m
    raise InvalidOADRMode('Invalid OADR Mode : %s' % mode)



class Node:

    # optional elements: 
    #   gui_port -> applicable only for THIS node
    #               i.e. System (Node) Configuration
    #   summary
    #
    # mandatory elements:
    __elements = ('nodeType', 'profile', 'mode', 'nodeId', 
                  'ipaddr', 'port', 'prefix')

    def __init__(self, **kwargs):

#        missing_elements = elements_exist(Node.__elements, kwargs.keys())
#        if missing_elements:
#            logging.debug(missing_elements, " are expected but missing")
#            return None

        if not self.valid_nodeType(kwargs['nodeType']):
            raise InvalidOADRNodeType('Invalid OADR Node Type : %s' % \
                                       kwargs['nodeType'])
        
        if not self.valid_mode(kwargs['mode']):
            raise InvalidOADRMode('Invalid OADR Mode : %s' % \
                                   kwargs['mode'])

        if not self.valid_profile(kwargs['profile']):
            raise InvalidOADRProfile('Invalid OADR Profile : %s' % \
                                      kwargs['profile'])

        if not self.valid_nodeId(kwargs['nodeId']):
            raise InvalidOADRNodeID('Invalid OADR Node ID : %s' % \
                                     kwargs['nodeId'])

        if not self.valid_ipaddr(kwargs['ipaddr']):
            raise InvalidIPaddress('Invalid IP Address : %s' % \
                                    kwargs['ipaddr'])

        if not self.valid_port(kwargs['port']):
            raise InvalidPort('Invalid Port : %s' % \
                               kwargs['port'])

        if not self.valid_prefix(kwargs['prefix']):
            raise InvalidOADRURLPrefix('Invalid OADR URL Prefix : %s' % \
                                        kwargs['prefix'])

        # applicable only for THIS node; optional for other Nodes
        if 'gui_port' in kwargs and not self.valid_port(kwargs['gui_port']):
            raise InvalidPort('Invalid GUI Port : %s' % \
                               kwargs['gui_port'])

        if 'summary' in kwargs and not self.valid_summary(kwargs['summary']):
            raise InvalidOADRSummary('Invalid OADR Node Summary : %s' % \
                                      kwargs['summary'])

        # setting the mandatory elements
        self.nodeType = oadr_node_from_str(kwargs['nodeType'])
        self.mode     = oadr_mode_from_str(kwargs['mode'])
        self.profile  = oadr_profile_from_str(kwargs['profile'])
        self.nodeId   = kwargs['nodeId']
        self.ipaddr   = kwargs['ipaddr']
        self.port     = kwargs['port']
        self.prefix   = kwargs['prefix']

        # setting the optional elements, if present
        if 'gui_port' in kwargs: 
            self.gui_port = kwargs['gui_port']
        if 'summary' in kwargs: 
            if self.nodeType == sysCfg.OADR_NODE.VEN:
                self.summary = 'Virtual End Node (VEN)'
            if self.nodeType == sysCfg.OADR_NODE.VTN:
                self.summary = 'Virtual Top Node (VTN)'
            if self.nodeType == sysCfg.OADR_NODE.VN:
                self.summary = 'Virtual Top Node (VTN) & ' \
                               'Virtual End Node (VEN)'


    def valid_nodeType(self, nodeType):
        return True

    def valid_mode(self, mode):
        return True

    def valid_profile(self, profile):
        return True

    def valid_nodeId(self, nodeId):
        return True

    def valid_ipaddr(self, ipaddr):
        return True

    def valid_port(self, port):
        return True

    def valid_prefix(self, prefix):
        return True

    def valid_summary(self, prefix):
        return True


    def get_nodeType(self):
        return self.nodeType

    def get_mode(self):
        return self.mode

    def get_profile(self):
        return self.profile

    def get_nodeId(self):
        return self.nodeId

    def get_ipaddr(self):
        return self.ipaddr

    def get_port(self):
        return self.port
    
    def get_prefix(self):
        return self.prefix

    def get_gui_port(self):
        return getattr(self, 'gui_port', None)

    def get_summary(self):
        return getattr(self, 'summary', '')


    def getDict(self):
        n = {'nodeType' : self.nodeType.key,
             'mode'     : self.mode.key,
             'profile'  : self.profile.key,
             'nodeId'   : self.nodeId,
             'ipaddr'   : self.ipaddr,
             'port'     : self.port,
             'prefix'   : self.prefix
        }
        if hasattr(self, 'gui_port'):
            n['gui_port'] = self.gui_port
        if hasattr(self, 'summary'):
            n['summary'] = self.summary
        return n

    def __str__(self):
        node_str  = 'Node:\n'
        node_str += '-----\n'
        node_str += '\tnodeType : %s \n' % self.nodeType
        node_str += '\tmode     : %s \n' % self.mode
        node_str += '\tprofile  : %s \n' % self.profile
        node_str += '\tnodeId   : %s \n' % self.nodeId
        node_str += '\tipaddr   : %s \n' % self.ipaddr
        node_str += '\tport     : %d \n' % self.port
        node_str += '\tprefix   : %s \n' % self.prefix
        if hasattr(self, 'gui_port'):
            node_str += '\tgui_port : %d \n' % self.gui_port
        if hasattr(self, 'summary'):
            node_str += '\tsummary  : %s \n' % self.summary
        return node_str


