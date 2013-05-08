import datetime
import time
import inspect
import logging

from openadr import config as oadrCfg
from openadr.ven import VENHttpServer
from openadr.vtn import VTNHttpServer
from openadr.vn import VNHttpServer
from openadr.exception import InvalidOADRNodeType


def line(char='=', length=50):
    print char * length

def print_config_from_file():
    # compose the config string
    config_str = '''

            Config parameters from  

    LOG_FILENAME       : %s 
    NODE               : %s
    MODE               : %s 
    HOSTNAME           : %s 
    IPADDR             : %s 
    VTN_URL_PREFIX     : %s 
    HTTP_VTN_PORT      : %d 
    VEN_URL_PREFIX     : %s 
    HTTP_VEN_PORT      : %d 
    VN_URL_PREFIX      : %s 
    HTTP_VN_PORT       : %d 
    SCHEMA_OADR_20A    : %s 
    SCHEMA_OADR_EI_20A : %s 

    ''' % (
        oadrCfg.OADR_CONFIG_FILE,
        oadrCfg.LOG_FILENAME,
        oadrCfg.NODE,
        oadrCfg.MODE,
        oadrCfg.HOSTNAME,
        oadrCfg.IPADDR,
        oadrCfg.VTN_URL_PREFIX,
        oadrCfg.HTTP_VTN_PORT,
        oadrCfg.VEN_URL_PREFIX,
        oadrCfg.HTTP_VEN_PORT,
        oadrCfg.VN_URL_PREFIX,
        oadrCfg.HTTP_VN_PORT,
        oadrCfg.SCHEMA_OADR_20A,
        oadrCfg.SCHEMA_OADR_EI_20A)
    logging.debug(config_str)

#
# read the 'OADR_CONFIG_FILE' and retrieve the 
# config paramaters for a given node
#
# success: 
# return a dict which contains the following:
#   node = 'VEN', 'VTN' or 'VN' (enum value)
#   port = http port for the node 
#   prefix = http url prefix for the node
#   http_handler = http web server handler for the node
#   .. keep adding any node type related parameters here!!
#
# failure:
# raise InvalidOADRNodeType exception and 
# return an empty dict if invalid node 
# type is passed.
#
def get_node_info(node):
    cfg = {}
    if oadrCfg.NODE == oadrCfg.OADR_NODE.VEN:
        cfg['node']         = oadrCfg.OADR_NODE.VEN
        cfg['port']         = oadrCfg.HTTP_VEN_PORT
        cfg['prefix']       = oadrCfg.VEN_URL_PREFIX
        cfg['http_handler'] = VENHttpServer
        cfg['node_str']     = 'Virtual End Node (VEN)'
    elif oadrCfg.NODE == oadrCfg.OADR_NODE.VTN:
        cfg['node']         = oadrCfg.OADR_NODE.VTN
        cfg['port']         = oadrCfg.HTTP_VTN_PORT
        cfg['prefix']       = oadrCfg.VTN_URL_PREFIX
        cfg['http_handler'] = VTNHttpServer
        cfg['node_str']     = 'Virtual Top Node (VTN)'
    elif oadrCfg.NODE == oadrCfg.OADR_NODE.VN:
        cfg['node']         = oadrCfg.OADR_NODE.VN
        cfg['port']         = oadrCfg.HTTP_VN_PORT
        cfg['prefix']       = oadrCfg.VN_URL_PREFIX
        cfg['http_handler'] = VNHttpServer
        cfg['node_str']     = 'Virtual Top Node (VTN) & Virtual End Node (VEN)'
    else:
        e_str = ('get_node_info(): Invalid Node Type: %s; check %s') % \
                (str(oadrCfg.NODE), oadrCfg.OADR_CONFIG_FILE)
        raise InvalidOADRNodeType(e_str)
        logging.critical(e_str)
    
    l_str = ('get_node_info(): Node Info - node: %s, port: %d, ' 
             'prefix: %s, http_handler: %s, node_str: %s') % \
            (cfg['node'], cfg['port'], cfg['prefix'], 
             cfg['http_handler'], cfg['node_str'])
    logging.info(l_str)

    return cfg

def print_startup_message():
    try: 
        node = get_node_info(oadrCfg.NODE)
    except InvalidOADRNodeType as e:
        print e.value
        exit(1)
        
    # compose the config string
    config_str = ('Starting OpenADR %s in %s mode '
                  'on %s at port %d configured for '
                  'openADR 2.0 %s profile schema.') % (
                  node['node_str'], str(oadrCfg.MODE), 
                  oadrCfg.IPADDR, node['port'], 
                  str(oadrCfg.PROFILE))

    print config_str
    logging.info(config_str)
    

def debug(dstr):
    # get the current date and time
    t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    
    # get the caller information
    stack = inspect.stack()[1]
    fname = stack[1]    # caller file name
    line = stack[2]     # caller line number
    func = stack[3]     # caller function name

    # if the debug() is not called from a function
    # then just print the string 'global' 
    if func == "<module>": func = "global"
    else: func = func + "()"

    # print the debug string with timestamp and caller info
    if oadr.DEBUG: print "[%s] %s:%s:%d -> %s" % \
                         (t, fname, func, line, dstr)
