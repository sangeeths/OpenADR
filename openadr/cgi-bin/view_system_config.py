#!/usr/bin/env python


from openadr.system import NODE, MODE, PROFILE, ID, IPADDR, \
                           PORT, PREFIX, GUI_PORT, SUMMARY


from openadr.cgi-bin import INDEX, VIEW_SYSTEM, UPDATE_SYSTEM, VIEW_NODE, UPDATE_NODE, VIEW_EVENTS, UPDATE_EVENTS,






print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>Test URL Encoding</title>"
print "</head>"
print "<body>"
print NODE
print '<br>'
print MODE
print '<br>'
print PROFILE
print '<br>'
print ID
print '<br>'
print IPADDR
print '<br>'
print PORT
print '<br>'
print PREFIX
print '<br>'
print GUI_PORT
print '<br>'
print SUMMARY
print '<br>'
print INDEX
print '<br>'
print VIEW_SYSTEM
print '<br>'
print UPDATE_SYSTEM
print '<br>'
print VIEW_NODE
print '<br>'
print UPDATE_NODE
print '<br>'
print VIEW_EVENTS
print '<br>'
print UPDATE_EVENTS
print '<br>'

#print 'OADR Node Type       = %s' % sn.nodeType.key
#print 'OADR Node Id         = %s' % sn.nodeId
#print 'IP Address           = %s' % sn.ipaddr
#print 'Port                 = %s' % sn.port
##print 'GUI Port             = %s' % sn.gui_port
#print 'OADR URL Path Prefix = %s' % sn.prefix
#print 'OADR Profile         = %s' % sn.profile

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

