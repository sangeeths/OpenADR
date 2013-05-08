"""Common settings and globals"""

from os.path import dirname, join, normpath, abspath
import sys, os
from enum import Enum
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


# --------------------------------------------
# Begin: USER CONFIGURATION
#
# OpenADR profiles
OADR_PROFILE = Enum('A', 'B', 'C')
#
# Currently operating OpenADR profile
PROFILE = OADR_PROFILE.A
#
# OpenADR node type
# VTN = Virtual Top Node
# VEN = Virtual End Node
# VN  = Combination of both VEN and VTN
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
# Hostname
HOSTNAME = 'localhost'
#
# IP Address
IPADDR = '192.168.0.198'
#
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
#
#
# End: USER CONFIGURATION 
# --------------------------------------------


#
# DO NOT DISTURB 
#
# The following configuration variables captures 
# directory structure of OpenADR implementation.
# They are NOT expected to change!
# 
# absolute filesystem path to the schema directory
# openadr                   OPENADR_ROOT
# |-- schema                SCHEMA_ROOT
# |   `-- 2.0               SCHEMA_20_ROOT
# |       |-- a             SCHEMA_20A_ROOT
# |       |   `-- *.xsd     2.0a schemas
# |       `-- b             SCHEMA_20B_ROOT
# |           `-- *.xsd     2.0b schemas
# `-- ...                   other directories 
#
# --------------------------------------------
# Begin: SYSTEM CONFIGURATION 
# 
# absolute filesystem path to the OpenADR project directory
OPENADR_ROOT = dirname(dirname(abspath(__file__)))
print 'OPENADR_ROOT', OPENADR_ROOT
#
# absolute filesystem path to the config directory
CONFIG_ROOT = normpath(join(OPENADR_ROOT, 'config'))
#
# configuration file for OpenADR i.e. this file! ;)
OADR_CONFIG_FILE = abspath(__file__)
#
# absolute filesystem path to the schema directory
SCHEMA_ROOT = normpath(join(OPENADR_ROOT, 'schema'))
#
# absolute filesystem path to the 2.0a and 2.0b schema directory
SCHEMA_20_ROOT   = normpath(join(SCHEMA_ROOT, '2.0'))
SCHEMA_20A_ROOT  = normpath(join(SCHEMA_20_ROOT, 'a'))
SCHEMA_20B_ROOT  = normpath(join(SCHEMA_20_ROOT, 'b'))
#
# OpenADR 2.0a schema
SCHEMA_OADR_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_20a.xsd'))
SCHEMA_OADR_EI_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_ei_20a.xsd'))
SCHEMA_OADR_EMIX_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_emix_20a.xsd'))
SCHEMA_OADR_PYLD_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_pyld_20a.xsd'))
SCHEMA_OADR_STRM_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_strm_20a.xsd'))
SCHEMA_OADR_XCAL_20A = normpath(join(SCHEMA_20A_ROOT, 'oadr_xcal_20a.xsd'))
#
# OpenADR 2.0b schema
SCHEMA_OADR_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_20b.xsd'))
SCHEMA_OADR_ISO_CC = normpath(join(SCHEMA_20B_ROOT, 'oadr_ISO_ISO3AlphaCurrencyCode_20100407.xsd'))
SCHEMA_OADR_ATOM = normpath(join(SCHEMA_20B_ROOT, 'oadr_atom.xsd'))
SCHEMA_OADR_EI_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_ei_20b.xsd'))
SCHEMA_OADR_EMIX_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_emix_20b.xsd'))
SCHEMA_OADR_GML_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_gml_20b.xsd'))
SCHEMA_OADR_GREENBUTTON = normpath(join(SCHEMA_20B_ROOT, 'oadr_greenbutton.xsd'))
SCHEMA_OADR_POWER_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_power_20b.xsd'))
SCHEMA_OADR_PYLD_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_pyld_20b.xsd'))
SCHEMA_OADR_SISCALE_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_siscale_20b.xsd'))
SCHEMA_OADR_STRM_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_strm_20b.xsd'))
SCHEMA_OADR_XCAL_20B = normpath(join(SCHEMA_20B_ROOT, 'oadr_xcal_20b.xsd'))
SCHEMA_OADR_XMLDSIG = normpath(join(SCHEMA_20B_ROOT, 'oadr_xmldsig.xsd'))
SCHEMA_OADR_XMLDSIG11 = normpath(join(SCHEMA_20B_ROOT, 'oadr_xmldsig11.xsd'))
#
# End: SYSTEM CONFIGURATION 
# --------------------------------------------

# __END__


