import logging
import json
import os
from threading import Lock as Lock 

from openadr import sysconfig as sysCfg
from openadr.node import Node 
from openadr.validation import *


def Load_NodeStore(filename=sysCfg.NODE_STORE):

    # if the nodes configuration file does not exist
    # then simple return {}
    if not os.path.exists(filename):
        logging.debug('Unable to load Node(s) Information; ' \
                      '%s not present' % filename)
        return {}

    with open(filename, 'r') as file_h:
        nodeConfig = json.load(file_h)

    # key = nodeId
    # value = object of type Node()
    node_store = {}
    for nodeId, node in nodeConfig.iteritems():
        node_d = node_str_to_enum(node)
        node_store[nodeId] = Node(**node_d)
    logging.debug('Loaded %d Node(s) from %s' % \
                 (len(nodeConfig), filename))
    print 'Load_NodeStore: ', node_store
    return node_store


def Save_NodeStore(node_store, node_store_lock, 
                   filename=sysCfg.NODE_STORE):
    node_store_lock.acquire()
    try:
        node_dict = {}
        # key = nodeId 
        # value = dict(object of type Node())
        for nId, n in node_store.iteritems():
            node_dict[nId] = node_enum_to_str(n.getDict())
        with open(filename, 'w') as file_h:
            json.dump(node_dict, file_h)
        logging.debug('Saved %d Node(s) to %s' % \
                     (len(node_dict), filename))
    finally:
        node_store_lock.release()


class NodeManager:
    __node_store_lock = Lock()
    __node_store = Load_NodeStore()
    
    def __init__(self): 
        pass

    def getAllNodes(self):
        return NodeManager.__node_store.values()
    
    def getNode(self, nodeId):
        if nodeId not in NodeManager.__node_store:
            return None
        return NodeManager.__node_store[nodeId]

    def addNode(self, node):
        NodeManager.__node_store_lock.acquire()
        NodeManager.__node_store[node.nodeId] = node
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        return True
 
    def removeNode(self, nodeId):
        if nodeId not in NodeManager.__node_store:
            return False
        NodeManager.__node_store_lock.acquire()
        del NodeManager.__node_store[nodeId]
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        return True


