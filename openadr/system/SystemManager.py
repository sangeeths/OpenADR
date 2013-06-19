import json
import os
from threading import Lock as Lock 

#from openadr.util import *
from openadr.node import Node 

from openadr import sysconfig as sysCfg
from openadr import userconfig as usrCfg

import logging

def Load_SysInfo(sysInfo_lock, 
                 filename=sysCfg.SYSTEM_INFO):
    try:
        logging.info('Loading System Information..')
        if not os.path.exists(filename):
            logging.debug('System Information not present in %s; ' \
                          'Loading the defults' % filename)
            # NOTE: assume that you are a VEN!! :)
            sysInfo_dict = usrCfg.SYSTEM_DEFAULT_SETTINGS[sysCfg.OADR_NODE.VEN]
        else:
            with open(filename, 'r') as file_h:
                sysInfo_dict = json.load(file_h)
        
        sysInfo = Node(**sysInfo_dict)
        #print str(sysInfo)
    except Exception, e:
        print e
    # NOTE: store the default settings to the
    #       persistence database
    if not os.path.exists(filename): 
        Save_SysInfo(sysInfo, sysInfo_lock)
    return sysInfo


def Save_SysInfo(sysInfo, sysInfo_lock, 
                 filename=sysCfg.SYSTEM_INFO):
    sysInfo_lock.acquire()
    try:
        with open(filename, 'w') as file_h:
            json.dump(sysInfo.getDict(), file_h)
        logging.info('Successfully saved the following ' \
                     'System (Node) Information to %s' % filename)
        logging.info(str(sysInfo))
    except Exception, e:
        print e
    finally:
        sysInfo_lock.release()
    return None


class SystemManager:
    __sysInfo_lock = Lock()
    __sysInfo = Load_SysInfo(__sysInfo_lock)
    
    def __init__(self): 
        pass
#        tn = {  'nodeType' : 'VEN',
#                'mode'     : 'PULL'
#                'profile'  : 'A'
#                'nodeId'   : 'testVTN_Id',
#                'ipaddr'   : '172.16.11.128',
#                'port'     : '9022',
#                'gui_port' : '9033',
#                'prefix'   : 'RiptideIO-VEN',
#        }
#        n = Node(**tn)
#        self.updateNode(n)
    
    def getSysInfo(self):
        return SystemManager.__sysInfo

    def setSysInfo(self, node):
        SystemManager.__sysInfo_lock.acquire()
        SystemManager.__sysInfo = node
        SystemManager.__sysInfo_lock.release()
        Save_SysInfo(SystemManager.__sysInfo, SystemManager.__sysInfo_lock)
 

