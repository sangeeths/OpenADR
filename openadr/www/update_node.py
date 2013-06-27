#!/usr/bin/env python

import cgitb; cgitb.enable()
import cgi

from openadr.www import *
from openadr.validation import *

from openadr.node.NodeManager import NodeManager
from openadr.node import Node



form = cgi.FieldStorage()

# get the action to be performed - 'add', 'edit', 'delete'
action = form.getvalue('action')

redirect_form = ''

if action == 'add' or action == 'edit':

    sub_title = "Add Node" if action == 'add' else "Edit Node"

    if action == 'edit':
        old_id = form.getvalue('old_id')

    nodeType = form.getvalue('node')
    nodeid   = form.getvalue('id')
    ipaddr   = form.getvalue('ip')
    port     = form.getvalue('port')
    prefix   = form.getvalue('prefix')
    
    node_dict = {
        'nodeType' : nodeType,
        'nodeId'   : nodeid,
        'ipaddr'   : ipaddr,
        'port'     : int(port),
        'prefix'   : prefix,
    }
 
    node_d = node_str_to_enum(node_dict)
       
    try:
        node = Node(**node_d)
        NodeManager().addNode(node)
        output = "Node added successfully!!"
        if action == 'edit':
            if old_id != nodeid:
                NodeManager().removeNode(old_id)
            output = "Node updated successfully!!"
    except Exception, e:
        output = e
        raise
    new_page = VIEW_NODE if action == 'add' else EDIT_NODE


elif action == 'delete':
    sub_title = 'Delete Node'
    nodeid = form.getvalue('id')
    try:
        NodeManager().removeNode(nodeid)
        output = "Node deleted successfully!!"
    except Exception, e:
        output = e
        raise
    new_page = DELETE_NODE
else:
    sub_title = 'Something wrong!'
    pass


print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print h1()
print h2(sub_title)
print "Output : "
print '<b> %s </b> <br><br>' % output
print 'Click <a href="%s">here</a> to continue...' % new_page
print "</body>"
print "</html>"


