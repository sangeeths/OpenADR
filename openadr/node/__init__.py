from openadr import userconfig as usrCfg

from openadr.validation import valid_incoming_elements, \
                               valid_ipaddr, \
                               valid_port

from openadr.node.NodeValidation import valid_node_type, \
                                        valid_mode, \
                                        valid_profile, \
                                        valid_node_id, \
                                        valid_prefix, \
                                        valid_summary

class Node(object):

    # mandatory elements for a OADR Node
    __oadrNode_elements = ('nodeType', 'nodeId', 'ipaddr', 'port', 'prefix')

    # mandatory elements for a System Node
    __sysNode_elements  = ('nodeType', 'nodeId', 'ipaddr', 'port', 'prefix', \
                           'profile', 'gui_port', 'summary', 'mode')

    def __init__(self, sysNode=False, **kwargs):

        if sysNode:
            valid_incoming_elements(Node.__sysNode_elements, kwargs.keys())
        else:
            valid_incoming_elements(Node.__oadrNode_elements, kwargs.keys())

        if valid_node_type(kwargs['nodeType']):
            self.nodeType = kwargs['nodeType']
           
        # mode is a mandatory parameter for sysNode
        if sysNode and valid_mode(kwargs['mode']):
            self.mode = kwargs['mode']

        # profile is a mandatory parameter for sysNode
        if sysNode and valid_profile(kwargs['profile']):
            self.profile = kwargs['profile']

        if valid_node_id(kwargs['nodeId']):
            self.nodeId = kwargs['nodeId']
        
        if valid_ipaddr(kwargs['ipaddr']):
            self.ipaddr = kwargs['ipaddr']

        if valid_port(kwargs['port']):
            self.port = kwargs['port']

        if valid_prefix(kwargs['prefix']):
            self.prefix = kwargs['prefix']

        # gui_port is a mandatory parameter for sysNode
        if sysNode and valid_port(kwargs['gui_port']):
            self.gui_port = kwargs['gui_port']

        # summary is a mandatory parameter for sysNode
        # NOTE: for now, hardcode the summary to the 
        #       default summary for the incoming NODE. 
        if sysNode and valid_summary(kwargs['summary']):
            self.summary = usrCfg.SYSTEM_DEFAULT_SETTINGS[self.nodeType]['summary']


    def getDict(self):
        return self.__dict__


    def __str__(self):
        node_str  = 'Node:\n'
        node_str += '-----\n'
        node_str += '\tnodeType : %s \n' % self.nodeType
        node_str += '\tnodeId   : %s \n' % self.nodeId
        node_str += '\tipaddr   : %s \n' % self.ipaddr
        node_str += '\tport     : %d \n' % self.port
        node_str += '\tprefix   : %s \n' % self.prefix
        # the following parameters are only for system node
        if hasattr(self, 'mode'):
            node_str += '\tmode     : %s \n' % self.mode
        if hasattr(self, 'profile'):
            node_str += '\tprofile  : %s \n' % self.profile
        if hasattr(self, 'gui_port'):
            node_str += '\tgui_port : %d \n' % self.gui_port
        if hasattr(self, 'summary'):
            node_str += '\tsummary  : %s \n' % self.summary
        return node_str


