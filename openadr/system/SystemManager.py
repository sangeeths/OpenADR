import json
import os
import logging
from threading import Lock as Lock 

from openadr.node import Node 

from openadr import sysconfig as sysCfg
from openadr import userconfig as usrCfg

from openadr.node.NodeUtil import node_enum_to_str, \
                                  node_str_to_enum


def Load_SysInfo(filename=sysCfg.SYSTEM_INFO):

    # if the persistence file does not exist,
    # then create one from the user config
    if not os.path.exists(filename): 
        logging.debug('%s does not exist; creating one ' \
                      'based on user config' % filename)
        usrConfig = usrCfg.SYSTEM_DEFAULT_SETTINGS[sysCfg.OADR_NODE.VEN]
        sysNode_d = node_enum_to_str(usrConfig, sysNode=True)
        with open(filename, 'w') as file_h:
            json.dump(sysNode_d, file_h)

    # if the persistence file already exist, 
    # then read from that!
    with open(filename, 'r') as file_h:
        usrConfig = json.load(file_h)
    sysNode_d = node_str_to_enum(usrConfig, sysNode=True)
    sysInfo = Node(sysNode=True, **sysNode_d)
    logging.debug('Loaded System Information Successfully ' \
                  'from %s' % filename)
    logging.info(str(sysInfo))
    return sysInfo


def Save_SysInfo(sysInfo, sysInfo_lock, 
                 filename=sysCfg.SYSTEM_INFO):
    sysInfo_lock.acquire()
    try:
        sysInfo_d = node_enum_to_str(sysInfo.getDict(), sysNode=True)
        with open(filename, 'w') as file_h:
            json.dump(sysInfo_d, file_h)
        logging.debug('Successfully saved the following ' \
                      'System (Node) Information to %s \n%s' % \
                      (filename, str(sysInfo)))
    finally:
        sysInfo_lock.release()


class SystemManager:
    __sysInfo_lock = Lock()
    __sysInfo = Load_SysInfo()
    
    def __init__(self): 
        pass
    
    def getSysInfo(self):
        return SystemManager.__sysInfo

    def setSysInfo(self, node):
        SystemManager.__sysInfo_lock.acquire()
        SystemManager.__sysInfo = node
        SystemManager.__sysInfo_lock.release()
        Save_SysInfo(SystemManager.__sysInfo, SystemManager.__sysInfo_lock)
 

