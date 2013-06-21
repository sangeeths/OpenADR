import logging
import json
import os
from threading import Lock as Lock 

from openadr import sysconfig as sysCfg
from openadr.node import Node 


def Load_NodeStore(node_store_lock, 
                   filename=sysCfg.NODE_STORE):
    node_store_lock.acquire()
    try:
        node_store = {}
        logging.debug('Loading Nodes..')
        if not os.path.exists(filename):
            logging.debug('Nodes Information not present in %s' % filename)
            node_dict = {}
        else:
            with open(filename, 'r') as file_h:
                node_dict = json.load(file_h)

        # key = nodeId
        # value = object of type Node()
        for k, v in node_dict.iteritems():
            node_store[k] = Node(**v)
            logging.info('    %s [%s]' % (node_store[k].nodeId,
                                          node_store[k].nodeType))
        logging.debug('Loaded %d Node(s)..')
    except Exception, e:
        print e
    finally:
        node_store_lock.release()
    return node_store



def Save_NodeStore(node_store, 
                   node_store_lock, 
                   filename=sysCfg.NODE_STORE):
    node_store_lock.acquire()
    try:
        logging.debug('Saving Nodes..')
        node_dict = {}
        # key = nodeId 
        # value = dict(object of type Node())
        for k, v in node_store.iteritems():
            node_dict[k] = v.getDict()
        with open(filename, 'w') as file_h:
            json.dump(node_dict, file_h)
        logging.debug('Saved %d Node(s) to %s' % \
                     (len(node_dict), filename))
    except Exception, e:
        print e
    finally:
        node_store_lock.release()
    return None


class NodeManager:
    __node_store_lock = Lock()
    __node_store = Load_NodeStore(__node_store_lock)
    
    def __init__(self): 
        pass
#        tn = {  'nodeType' : 'VTN',
#                'nodeId'   : 'testVTN_Id',
#                'ipaddr'   : '192.168.0.194',
#                'port'     : 9044,
#                'gui_port' : 9033,
#                'prefix'   : 'rioVTN',
#                'profile'  : 'A',
#                'mode'  : 'PULL'
#        }
#        n = Node(**tn)
#        self.addNode(n)
#
#        tn = {  'nodeType' : 'VTN',
#                'nodeId'   : 'testVTN_Id_2',
#                'ipaddr'   : '172.16.11.128',
#                'port'     : 9011,
#                'gui_port' : 9033,
#                'prefix'   : 'rioVTN',
#                'profile'  : 'A',
#                'mode'  : 'PULL',
#        }
#        n = Node(**tn)
#        self.addNode(n)


    def getAllNodes(self):
        return NodeManager.__node_store.values()
    
    def getNode(self, nodeId):
        if nodeId in NodeManager.__node_store:
            return NodeManager.__node_store[nodeId]
        else:
            return None

    def addNode(self, node):
        NodeManager.__node_store_lock.acquire()
        NodeManager.__node_store[node.nodeId] = node
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        return True
 
    def removeNode(self, nodeId):
        NodeManager.__node_store_lock.acquire()
        del NodeManager.__node_store[nodeId]
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        return True


