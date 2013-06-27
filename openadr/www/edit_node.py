#!/usr/bin/env python

import logging
from openadr.www import *

from openadr.node.NodeManager import NodeManager

sub_title = 'Edit Node'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.node, action=ACTION.edit)

print '<table border="1">'
print '<tr>'
print '<th>Node ID     </th>' 
print '<th>Node Type   </th>' 
print '<th>IP Address  </th>' 
print '<th>Port        </th>' 
print '<th>URL Prefix  </th>' 
print '<th>Click Edit  </th>' 
print '</tr>'

nodes = NodeManager().getAllNodes()
for node in nodes:
    print '<form name="edit_node" action="%s" method="post">' % EDIT_NODE_ID
    print '<tr>'
    print '<input type="hidden" name="action" value="edit">' 
    print '<input type="hidden" name="id" value="%s">' % node.nodeId
    print '<td>%s</td>' % node.nodeId 
    print '<td>%s</td>' % node.nodeType 
    print '<td>%s</td>' % node.ipaddr 
    print '<td>%s</td>' % node.port 
    print '<td>%s</td>' % node.prefix 
    print '<td><input type="submit" value="Edit"></td>'
    print '</tr>'
    print '</form>'

print '</table>'
  
print '<br>'
print 'Total Nodes Configured = %d' % len(nodes)
 

print "</body>"
print "</html>"



