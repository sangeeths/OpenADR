#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
import cgi

from openadr.www import *
from openadr import sysconfig as sysCfg

from openadr.node.NodeManager import NodeManager
from openadr.node import Node


form = cgi.FieldStorage()

# get the action to be performed - 'add', 'edit', 'delete'
action = form.getvalue('action')

nm = NodeManager()
redirect_form = ''

if action == 'add' or action == 'edit':

    sub_title = "Add Node" if action == 'add' else "Edit Node"

    if action == 'edit':
        old_id = form.getvalue('old_id')

    nodeType = form.getvalue('node')
    mode     = form.getvalue('mode')
    profile  = form.getvalue('profile')
    nodeid   = form.getvalue('id')
    ipaddr   = form.getvalue('ip')
    port     = form.getvalue('port')
    prefix   = form.getvalue('prefix')
    

    output = ''
    if nodeType is None:
        output += 'Enter valid Node Type - VEN/VTN/VN<br>'
    if mode is None:
        output += 'Enter valid mode - PULL/PUSH<br>'
    if profile is None:
        output += 'Enter valid profile - A/B/C<br>'
    if nodeid is None:
        output += 'Enter valid node id - [A-Za-z0-9-_]<br>'
    if ipaddr is None:
        output += 'Enter valid ip address - A.B.C.D<br>'
    if port is None:
        output += 'Enter valid port - [0-9]<br>'
    if prefix is None:
        output += 'Enter valid url prefix - [A-Za-z0-9-_]<br>'

    if output == '':
        node_dict = {
        'nodeType' : nodeType,
        'profile'  : profile,
        'mode'     : mode,
        'nodeId'   : nodeid,
        'ipaddr'   : ipaddr,
        'port'     : int(port),
        'prefix'   : prefix,
        }
        
        try:
            node = Node(**node_dict)
            nm.addNode(node)
            output = "Node added successfully!!"
            if action == 'edit':
                if old_id != node.get_nodeId():
                    nm.removeNode(old_id)
                output = "Node updated successfully!!"
        except Exception, e:
            output = e
        new_page = VIEW_NODE
    else:
        output = 'Enter valid values for the following parameters..<br>' + output
        new_page = ADD_NODE if action == 'add' else EDIT_NODE

elif action == 'delete':
    sub_title = 'Delete Node'
    nodeid = form.getvalue('id')
    try:
        nm.removeNode(nodeid)
        output = "Node deleted successfully!!"
    except Exception, e:
        output = e
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


