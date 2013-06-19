#!/usr/bin/env python

from openadr.util import *
from openadr.system.SystemManager import SystemManager


sn = SystemManager().getSysInfo()

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>Test URL Encoding</title>"
print "</head>"
print "<body>"
print 'OADR Node Type       = %s' % sn.nodeType.key
print 'OADR Node Id         = %s' % sn.nodeId
print 'IP Address           = %s' % sn.ipaddr
print 'Port                 = %s' % sn.port
#print 'GUI Port             = %s' % sn.gui_port
print 'OADR URL Path Prefix = %s' % sn.prefix
print 'OADR Profile         = %s' % sn.profile

#
#        tn = {  'nodeType' : 'VEN',
#                'nodeId'   : 'testVTN_Id',
#                'ipaddr'   : '172.16.11.128',
#                'port'     : '9022',
#                'gui_port' : '9033',
#                'prefix'   : 'RiptideIO-VEN',
#                'profile'  : 'A'
#        }
#

print "</body>"
print "</html>"

