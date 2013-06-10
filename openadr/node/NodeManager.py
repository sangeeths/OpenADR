
import pickle
from threading import Lock as Lock 

from openadr import config as oadrCfg
from openadr.util import *

from openadr.node import Node 

def Load_NodeStore(node_store_lock, 
                   pickle_db=oadrCfg.NODE_STORE):
    node_store_lock.acquire()
    try:
        node_store_pkl = open(pickle_db, 'rb')
        pkl_d = pickle.load(node_store_pkl)
        node_store_pkl.close() 
        node_store = {}
        print 'Loading Node Information..'
        for k, v in pkl_d.iteritems():
            node_store[k] = Node(**v)
            print '    %s [%s]' % (node_store[k].nodeId,
                                   node_store[k].nodeType)
    except Exception, e:
        print e
    finally:
        node_store_lock.release()
        return {}
    return node_store



def Save_NodeStore(node_store, 
                   node_store_lock, 
                   pickle_db=oadrCfg.NODE_STORE):
    node_store_lock.acquire()
    try:
        pkl_d = {}
        for k, v in node_store.iteritems():
            pkl_d[k] = v.getDict()

        node_store_pkl = open(pickle_db, 'wb')
        pickle.dump(pkl_d, node_store_pkl)
        node_store_pkl.close() 
    except Exception, exc:
        print exc
    finally:
        node_store_lock.release()
    return None


class NodeManager:
    __node_store_lock = Lock()
    __node_store = Load_NodeStore(__node_store_lock)
    
    def __init__(self): 
        print "NodeManager :: __init__()"
        n = Node(oadrCfg.OADR_NODE.VTN, 'testVTN_Id', 
                 '172.16.11.128', '9011', 'rioVTN', 
                 oadrCfg.OADR_PROFILE.A) 
        self.addNode(n)
    def getAllNodes(self):
        print "NodeManager :: getAllNodes()"
        return NodeManager.__node_store.values()

    def addNode(self, node):
        print "NodeManager :: addNode() :: enter"
        NodeManager.__node_store_lock.acquire()
        NodeManager.__node_store[node.nodeId] = node
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        print "NodeManager :: addNode() :: done"
 
    def removeNode(self, node):
        print "NodeManager :: removeNode() :: enter"
        NodeManager.__node_store_lock.acquire()
        del NodeManager.__node_store[node.nodeId]
        NodeManager.__node_store_lock.release()
        Save_NodeStore(NodeManager.__node_store, NodeManager.__node_store_lock)
        print "NodeManager :: removeNode() :: done"

