from os.path import dirname, join, normpath, abspath
from enum import Enum

import sys
import logging

# # # # # # # # # # # # # # # # # # # # # # # #
#
#            Logging Configuration
#
# Log file name
LOG_FILENAME = '/tmp/openadr.log'
#
# Log level
LOG_LEVEL = logging.DEBUG
#
# Log format
LOG_FORMAT = '[%(asctime)s]: %(levelname)s : %(message)s'
#
# Log Stream 
# for time being, print the logs on stdout
LOG_STREAM = sys.stdout
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#            Directory Structure
#
# NOTE: do not disturb the following unless 
#       the directory structure is changed!
#
# absolute filesystem path to the OpenADR project directory
OPENADR_ROOT = dirname(abspath(__file__))
#
# configuration file for OpenADR i.e. this file! ;)
# used as a reference in exceptions and error messages
OADR_CONFIG_FILE = abspath(__file__)
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#            Schema Configurations
#
# NOTE: do not disturb the following unless 
#       the directory structure is changed!
#
# absolute filesystem path to the schema directory
# Read-only: Do Not Change
SCHEMA_ROOT = normpath(join(OPENADR_ROOT, 'schema'))
#
# absolute filesystem path to the 2.0A, 
# 2.0B and 2.0C schema directory
# Read-only: Do Not Change
SCHEMA_20_ROOT  = normpath(join(SCHEMA_ROOT, '2.0'))
SCHEMA_20A_ROOT = normpath(join(SCHEMA_20_ROOT, 'a'))
SCHEMA_20B_ROOT = normpath(join(SCHEMA_20_ROOT, 'b'))
SCHEMA_20C_ROOT = normpath(join(SCHEMA_20_ROOT, 'c'))
#
# OpenADR 2.0 A Profile Schema
# Read-only: Do Not Change
SCHEMA_OADR_20A      = normpath(join(SCHEMA_20A_ROOT, 'oadr_20a.xsd'))
SCHEMA_OADR_EI_20A   = normpath(join(SCHEMA_20A_ROOT, 'oadr_ei_20a.xsd'))
SCHEMA_OADR_EMIX_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_emix_20a.xsd'))
SCHEMA_OADR_PYLD_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_pyld_20a.xsd'))
SCHEMA_OADR_STRM_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_strm_20a.xsd'))
SCHEMA_OADR_XCAL_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_xcal_20a.xsd'))
#
# OpenADR 2.0 B Profile Schema
# Read-only: Do Not Change
SCHEMA_OADR_20B         = normpath(join(SCHEMA_20B_ROOT, 'oadr_20b.xsd'))
SCHEMA_OADR_ISO_CC      = normpath(join(SCHEMA_20B_ROOT, 'oadr_ISO_ISO3AlphaCurrencyCode_20100407.xsd'))
SCHEMA_OADR_ATOM        = normpath(join(SCHEMA_20B_ROOT, 'oadr_atom.xsd'))
SCHEMA_OADR_EI_20B      = normpath(join(SCHEMA_20B_ROOT, 'oadr_ei_20b.xsd'))
SCHEMA_OADR_EMIX_20B    = normpath(join(SCHEMA_20B_ROOT, 'oadr_emix_20b.xsd'))
SCHEMA_OADR_GML_20B     = normpath(join(SCHEMA_20B_ROOT, 'oadr_gml_20b.xsd'))
SCHEMA_OADR_GREENBUTTON = normpath(join(SCHEMA_20B_ROOT, 'oadr_greenbutton.xsd'))
SCHEMA_OADR_POWER_20B   = normpath(join(SCHEMA_20B_ROOT, 'oadr_power_20b.xsd'))
SCHEMA_OADR_PYLD_20B    = normpath(join(SCHEMA_20B_ROOT, 'oadr_pyld_20b.xsd'))
SCHEMA_OADR_SISCALE_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_siscale_20b.xsd'))
SCHEMA_OADR_STRM_20B    = normpath(join(SCHEMA_20B_ROOT, 'oadr_strm_20b.xsd'))
SCHEMA_OADR_XCAL_20B    = normpath(join(SCHEMA_20B_ROOT, 'oadr_xcal_20b.xsd'))
SCHEMA_OADR_XMLDSIG     = normpath(join(SCHEMA_20B_ROOT, 'oadr_xmldsig.xsd'))
SCHEMA_OADR_XMLDSIG11   = normpath(join(SCHEMA_20B_ROOT, 'oadr_xmldsig11.xsd'))
#
# OpenADR 2.0 C Profile Schema
# Read-only: Do Not Change
# TODO: Add here!!
SCHEMA_OADR_20C = normpath(join(SCHEMA_20C_ROOT, 'oadr_20c.xsd'))
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#           OADR Configurations
#
# OpenADR profiles
# Read-only: Do Not Change
OADR_PROFILE = Enum('A', 'B', 'C')
#
# Currently operating OpenADR profile
PROFILE = OADR_PROFILE.A
#
# OpenADR node type
# VTN = Virtual Top Node
# VEN = Virtual End Node
# VN  = Combination of both VEN and VTN
# Read-only: Do Not Change
OADR_NODE = Enum('VEN', 'VTN', 'VN')
#
# Current operating OpenADR node type
# The following are the valid values:
#   -> OADR_NODE.VTN for VTN
#   -> OADR_NODE.VEN for VEN
#   -> OADR_NODE.VN  for both VEN and VTN
# Anything other than the above values are 
# considered invalid node type
NODE = OADR_NODE.VEN
#
# HTTP modes
# Read-only: Do Not Change
HTTP_MODE = Enum('PUSH', 'PULL')
#
# Current operating mode for config.NODE
# The following are the valud values:
#   -> HTTP_MODE.PULL
#   -> HTTP_MODE.PUSH
# Anything other than the above values are 
# considered invalid mode for config.NODE
MODE = HTTP_MODE.PULL
#
# Supported operations: send and receive
OADR_OP = Enum('SEND', 'RECV')
#
# OpenADR 2.0 Services
# Read-only: Do Not Change
# NOTE: EiAvail, EiEnroll and EiMarketContext 
#       are applicable only for future releases
#   L = Limited Profile
#   F = Full Profile (includes Limited Profile)
#   N/A = Not Applicable
# +-----------------+-----------------+-----------------+
# |     O A D R     |       VTN       |       VEN       |
# | S E R V I C E S +-----+-----+-----+-----+-----+-----+
# |      2 . 0      |  A  |  B  |  C  |  A  |  B  |  C  |
# +-----------------+-----+-----+-----+-----+-----+-----+
# | EiAvail         | N/A | N/A | N/A | N/A | N/A | N/A |
# | EiEnroll        | N/A | N/A | N/A | N/A | N/A | N/A |
# | EiEvent         |  L  |  F  |  F  |  L  |  F  |  F  |
# | EiMarketContext | N/A | N/A | N/A | N/A | N/A | N/A |
# | EiOpt           | N/A |  F  |  F  | N/A |  F  |  F  |
# | EiQuote         | N/A | N/A |  F  | N/A | N/A |  F  |
# | EiRegisterParty | N/A |  F  |  F  | N/A |  F  |  F  |
# | EiReport        | N/A |  F  |  F  | N/A |  F  |  F  |
# +-----------------+-----+-----+-----+-----+-----+-----+
OADR_SERVICE = Enum('EiAvail',
                    'EiEnroll',
                    'EiEvent',
                    'EiMarketContext',
                    'EiOpt',
                    'EiQuote',
                    'EiRegisterParty',
                    'EiReport')
#
# SERVICE holds the list of OADR_SERVICES
# that are applicable for a given OADR_PROFILE
# Read-only: Do Not Change
SERVICE = {OADR_PROFILE.A: [OADR_SERVICE.EiEvent],
           OADR_PROFILE.B: [OADR_SERVICE.EiEvent, 
                            OADR_SERVICE.EiOpt, 
                            OADR_SERVICE.EiReport, 
                            OADR_SERVICE.EiRegisterParty],
           OADR_PROFILE.C: [OADR_SERVICE.EiEvent, 
                            OADR_SERVICE.EiQuote, 
                            OADR_SERVICE.EiOpt, 
                            OADR_SERVICE.EiReport, 
                            OADR_SERVICE.EiRegisterParty]
          }
#
# OADR EiAvail Messages
# Read-only: Do Not Change
OADR_EIAVAIL = Enum('')
#
# OADR EiEnroll Messages
# Read-only: Do Not Change
OADR_EIENROLL = Enum('')
#
# OADR EiEvent Messages
# Read-only: Do Not Change
OADR_EIEVENT = Enum('oadrCreatedEvent',
                    'oadrDistributeEvent',
                    'oadrPoll',
                    'oadrRequestEvent',
                    'oadrResponse')
#
# OADR EiMarketContext Messages
# Read-only: Do Not Change
OADR_EIMARKETCONTEXT = Enum('')
#
# OADR EiOpt Messages
# Read-only: Do Not Change
OADR_EIOPT = Enum('')
#
# OADR EiQuote Messages
# Read-only: Do Not Change
OADR_EIQUOTE = Enum('')
#
# OADR EiRegisterParty Messages
# Read-only: Do Not Change
OADR_EIREGISTERPARTY = Enum('')
#
# OADR EiReport Messages
# Read-only: Do Not Change
OADR_EIREPORT = Enum('')
#
# 'A' Profile Messages
#   -> VTN can send
#   -> VEN can receive
# Read-only: Do Not Change
A_VTN_SEND = A_VEN_RECV = [OADR_EIEVENT.oadrDistributeEvent, 
                           OADR_EIEVENT.oadrResponse]
#
# 'A' Profile Messages
#   -> VEN can send
#   -> VTN can receive
# Read-only: Do Not Change
A_VEN_SEND = A_VTN_RECV = [OADR_EIEVENT.oadrCreatedEvent, 
                           OADR_EIEVENT.oadrRequestEvent, 
                           OADR_EIEVENT.oadrResponse]
#
# 'B' Profile Messages
#   -> VTN can send
#   -> VEN can receive
# Read-only: Do Not Change
B_VTN_SEND = B_VEN_RECV = []
#
# 'B' Profile Messages
#   -> VEN can send
#   -> VTN can receive
# Read-only: Do Not Change
B_VEN_SEND = B_VTN_RECV = []
#
# 'C' Profile Messages
#   -> VTN can send
#   -> VEN can receive
# Read-only: Do Not Change
C_VTN_SEND = C_VEN_RECV = []
#
# 'C' Profile Messages
#   -> VEN can send
#   -> VTN can receive
# Read-only: Do Not Change
C_VEN_SEND = C_VTN_RECV = []
#
# NOTE: MESSAGE maps the OADR Messages 
#       to the appropriate OADR Profiles
# Read-only: Do Not Change
MESSAGE = {OADR_PROFILE.A: {OADR_NODE.VTN: {OADR_OP.SEND: A_VTN_SEND, 
                                            OADR_OP.RECV: A_VTN_RECV},
                            OADR_NODE.VEN: {OADR_OP.SEND: A_VEN_SEND,
                                            OADR_OP.RECV: A_VEN_RECV}},
           OADR_PROFILE.B: {OADR_NODE.VTN: {OADR_OP.SEND: B_VTN_SEND, 
                                            OADR_OP.RECV: B_VTN_RECV},
                            OADR_NODE.VEN: {OADR_OP.SEND: B_VEN_SEND,
                                            OADR_OP.RECV: B_VEN_RECV}},
           OADR_PROFILE.C: {OADR_NODE.VTN: {OADR_OP.SEND: C_VTN_SEND, 
                                            OADR_OP.RECV: C_VTN_RECV},
                            OADR_NODE.VEN: {OADR_OP.SEND: C_VEN_SEND,
                                            OADR_OP.RECV: C_VEN_RECV}}
          }
#
# mapping OADR_SERVICE.<service-name> 
# and service enums
# Read-only: Do Not Change
SERVICE_MESSAGE = {
    OADR_SERVICE.EiAvail         : [],
    OADR_SERVICE.EiEnroll        : [],
    OADR_SERVICE.EiEvent         : [OADR_EIEVENT.oadrDistributeEvent,
                                    OADR_EIEVENT.oadrCreatedEvent, 
                                    OADR_EIEVENT.oadrRequestEvent, 
                                    OADR_EIEVENT.oadrResponse],
    OADR_SERVICE.EiMarketContext : [],
    OADR_SERVICE.EiOpt           : [],
    OADR_SERVICE.EiQuote         : [],
    OADR_SERVICE.EiRegisterParty : [],
    OADR_SERVICE.EiReport        : []
}
#
# OADR_PROFILE and path to its schema (*.xsd) 
# Read-only: Do Not Change
XSD = {OADR_PROFILE.A: SCHEMA_OADR_20A,
       OADR_PROFILE.B: SCHEMA_OADR_20B,
       OADR_PROFILE.C: SCHEMA_OADR_20C
      }
#
# This is required to gather all the 
# namespace for a given OADR_PROFILE schema
# Read-only: Do Not Change
XSD_NS = {OADR_PROFILE.A: [SCHEMA_OADR_20A, SCHEMA_OADR_EI_20A, 
                           SCHEMA_OADR_EMIX_20A, SCHEMA_OADR_PYLD_20A, 
                           SCHEMA_OADR_STRM_20A, SCHEMA_OADR_XCAL_20A],
          OADR_PROFILE.B: [SCHEMA_OADR_20B, SCHEMA_OADR_ISO_CC, 
                           SCHEMA_OADR_ATOM, SCHEMA_OADR_EI_20B, 
                           SCHEMA_OADR_EMIX_20B, SCHEMA_OADR_GML_20B, 
                           SCHEMA_OADR_GREENBUTTON, SCHEMA_OADR_POWER_20B, 
                           SCHEMA_OADR_PYLD_20B, SCHEMA_OADR_SISCALE_20B, 
                           SCHEMA_OADR_STRM_20B, SCHEMA_OADR_XCAL_20B, 
                           SCHEMA_OADR_XMLDSIG, SCHEMA_OADR_XMLDSIG11],
          OADR_PROFILE.C: [SCHEMA_OADR_20C]
         }
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#           System Configuration
#
# Hostname
HOSTNAME = 'localhost'
#
# IP Address
IPADDR = '192.168.0.195'
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#           Virtual Top Node (VTN)
#
# The following configurations are applicable
# only on VEN OpenADR node types.
#   config.NODE == OADR_NODE.VEN 
#
# HTTP port of VTN
HTTP_VTN_PORT = 9000
#
# VTN URL prefix
VTN_URL_PREFIX = 'rioVTN'
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#           Virtual End Node (VEN)
#
# The following configurations are applicable
# only on VEN OpenADR node types.
#   config.NODE == OADR_NODE.VEN 
#
# HTTP port of VEN
HTTP_VEN_PORT = 9001
#
# VEN URL prefix
VEN_URL_PREFIX = 'rioVEN'
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#             Virtual Node
#          (Both VEN and VTN)
#
# The following configurations are applicable
# only on VN OpenADR node types.
#   config.NODE == OADR_NODE.VN
#
# HTTP port of VN
HTTP_VN_PORT = 9002
#
# VN URL prefix
VN_URL_PREFIX = 'rioVN'
#
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#
#             Node Configuration
#
# Basic configurations like port, prefix,
# description, etc for a given OADR_NODE type
# Read-only: Do Not Change (unless really needed)
OADR_NODE_CONFIG = {
    OADR_NODE.VEN: {
        'node'         : OADR_NODE.VEN, 
        'port'         : HTTP_VEN_PORT,
        'prefix'       : VEN_URL_PREFIX,
        'node_str'     : 'Virtual End Node (VEN)'},
    OADR_NODE.VTN: {
        'node'         : OADR_NODE.VTN, 
        'port'         : HTTP_VTN_PORT,
        'prefix'       : VTN_URL_PREFIX,
        'node_str'     : 'Virtual Top Node (VTN)'},
    OADR_NODE.VN:  {
        'node'         : OADR_NODE.VN, 
        'port'         : HTTP_VN_PORT,
        'prefix'       : VN_URL_PREFIX,
        'node_str'     : 'Virtual Top Node (VTN) & '\
                         'Virtual End Node (VEN)'},
}

#
# Configuration of the current node type
# Read-only: Do Not Change
CONFIG = OADR_NODE_CONFIG[NODE]
#
# # # # # # # # # # # # # # # # # # # # # # # #


# __END__
