import logging
import sys
from enum import Enum

from openadr import sysconfig as sysCfg


# # # # # # # # # # # # # # # # # # # # # # # #
#
#            System Default Settings 
#
# NOTE: JSON does not support enum in 
#       default encoding. So, store values
#       as either int or str
#
# VTN default settings
VTN_DEFAULT_SETTINGS = {
    'nodeType' : sysCfg.OADR_NODE.VTN,
    'mode'     : sysCfg.OADR_MODE.PULL,
    'profile'  : sysCfg.OADR_PROFILE.A,
    'nodeId'   : 'vtnId',
    'ipaddr'   : '127.0.0.1',
    'port'     : 9001,
    'gui_port' : 9002,
    'prefix'   : 'VTN',
    'summary'  : 'Virtual Top Node (VTN)',
}
#
# VEN default settings
VEN_DEFAULT_SETTINGS = {
    'nodeType' : sysCfg.OADR_NODE.VEN,
    'mode'     : sysCfg.OADR_MODE.PULL,
    'profile'  : sysCfg.OADR_PROFILE.A,
    'nodeId'   : 'venId',
    'ipaddr'   : '127.0.0.1',
    'port'     : 9011,
    'gui_port' : 9012,
    'prefix'   : 'VEN',
    'summary'  : 'Virtual End Node (VEN)',
}
#
# VN default settings
VN_DEFAULT_SETTINGS = {
    'nodeType' : sysCfg.OADR_NODE.VN,
    'mode'     : sysCfg.OADR_MODE.PULL,
    'profile'  : sysCfg.OADR_PROFILE.A,
    'nodeId'   : 'vnId',
    'ipaddr'   : '127.0.0.1',
    'port'     : 9021,
    'gui_port' : 9022,
    'prefix'   : 'VN',
    'summary'  : 'Virtual Top Node (VTN) & ' \
                 'Virtual End Node (VEN)',
}
# 
# SYSTEM_DEFAULT_SETTINGS will be used by
# all the applications to pick the default
# configuration for the currently configured 
# OADR_NODE type
#
# Read-only: Do Not Change
SYSTEM_DEFAULT_SETTINGS = {
    sysCfg.OADR_NODE.VTN : VTN_DEFAULT_SETTINGS,
    sysCfg.OADR_NODE.VEN : VEN_DEFAULT_SETTINGS,
    sysCfg.OADR_NODE.VN  : VN_DEFAULT_SETTINGS 
}
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#            Logging Configuration
#
# Log file name
LOG_FILENAME = '/tmp/openadr.log'
GUI_LOG_FILENAME = '/tmp/openadr.log'
#
# Log level
LOG_LEVEL = logging.DEBUG
GUI_LOG_LEVEL = logging.DEBUG
#
# Log format
LOG_FORMAT = '[%(asctime)s]: %(levelname)s : %(message)s'
GUI_LOG_FORMAT = '[%(asctime)s]: [GUI] : %(levelname)s : %(message)s'
#
# Log Stream
# for time being, print the logs on stdout
LOG_STREAM = sys.stdout
GUI_LOG_STREAM = sys.stdout
#
# # # # # # # # # # # # # # # # # # # # # # # #

