import json
import os
import logging
from threading import Lock as Lock 

from openadr.node import Node 

from openadr import sysconfig as sysCfg
from openadr import userconfig as usrCfg


def Load_SysInfo(sysInfo_lock, 
                 filename=sysCfg.SYSTEM_INFO):
    try:
        logging.debug('Loading System Information..')
        if not os.path.exists(filename):
            logging.debug('System Information not present in %s; ' \
                          'Loading the defults from user config' % filename)
            # NOTE: assume that you are a VEN!! :)
            # TBD: is there a better way of dealing this scenario?! 
            sysInfo_dict = usrCfg.SYSTEM_DEFAULT_SETTINGS[sysCfg.OADR_NODE.VEN]
        else:
            with open(filename, 'r') as file_h:
                sysInfo_dict = json.load(file_h)
        
        sysInfo = Node(**sysInfo_dict)
        #print str(sysInfo)
    except Exception, e:
        print e
    # NOTE: store the default settings to the
    #       persistent SYSTEM_INFO file 
    if not os.path.exists(filename): 
        Save_SysInfo(sysInfo, sysInfo_lock)
    return sysInfo


def Save_SysInfo(sysInfo, sysInfo_lock, 
                 filename=sysCfg.SYSTEM_INFO):
    sysInfo_lock.acquire()
    try:
        with open(filename, 'w') as file_h:
            json.dump(sysInfo.getDict(), file_h)
        logging.debug('Successfully saved the following ' \
                      'System (Node) Information to %s \n%s' % \
                      (filename, str(sysInfo)))
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
 

