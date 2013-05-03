from openadr.config import *
import datetime
import time
import inspect
import logging

def line(char='=', length=50):
    print char * length

def print_config():
    # compose the config string
    config_str = '''
            Start-up Configuration 
           ------------------------
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
        LOG_FILENAME,
        NODE,
        MODE,
        HOSTNAME,
        IPADDR,
        VTN_URL_PREFIX,
        HTTP_VTN_PORT,
        VEN_URL_PREFIX,
        HTTP_VEN_PORT,
        VN_URL_PREFIX,
        HTTP_VN_PORT,
        SCHEMA_OADR_20A,
        SCHEMA_OADR_EI_20A)
    print config_str
    logging.debug(config_str)

def print_start_config():
    # get the node type string
    if NODE == OADR_NODE.VEN:
        node = "Virtual End Node (VEN)"
        port = HTTP_VEN_PORT
        prefix = VEN_URL_PREFIX
    elif NODE == OADR_NODE.VTN:
        node = "Virtual Top Node (VTN)"
        port = HTTP_VTN_PORT
        prefix = VTN_URL_PREFIX
    elif NODE == OADR_NODE.VN:
        node = "Virtual Top Node (VTN) & Virtual End Node (VEN)"
        port = HTTP_VN_PORT
        prefix = VN_URL_PREFIX
    else:
        e_str = ("Invalid Node Type; check %s") % OADR_CONFIG_FILE
        print e_str
        logging.debug(e_str)
        exit(1)

    # compose the config string
    config_str = ('Starting OpenADR %s in %s mode '
                  'on %s at port %d configured for '
                  'openADR 2.0 %s profile schema.') % (
                  node, str(MODE), IPADDR, 
                  port, str(PROFILE))

    print config_str
    

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
