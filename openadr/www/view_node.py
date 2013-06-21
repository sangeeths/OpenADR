#!/usr/bin/env python

import logging
from openadr.www import *

from openadr.node.NodeManager import NodeManager


sub_title = 'View Node(s)'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.node, action=ACTION.view)

print '<table border="1">'
print '<tr>'
print '<th>Node ID     </th>' 
print '<th>Node Type   </th>' 
print '<th>Mode        </th>' 
print '<th>OADR Profile</th>' 
print '<th>IP Address  </th>' 
print '<th>Port        </th>' 
print '<th>URL Prefix  </th>' 
print '</tr>'

nodes = NodeManager().getAllNodes()
for node in nodes:
    print '<tr>'
    print '<td>%s</td>' % node.get_nodeId() 
    print '<td>%s</td>' % node.get_nodeType() 
    print '<td>%s</td>' % node.get_mode()
    print '<td>%s</td>' % node.get_profile() 
    print '<td>%s</td>' % node.get_ipaddr() 
    print '<td>%s</td>' % node.get_port() 
    print '<td>%s</td>' % node.get_prefix() 
    print '</tr>'
 
print '</table>'
  
print '<br>'
print 'Total number of Nodes configured = %d' % len(nodes)
 
print "</body>"
print "</html>"



