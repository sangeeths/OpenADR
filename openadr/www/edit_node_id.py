#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
import cgi

from openadr.www import *
from openadr import sysconfig as sysCfg

from openadr.node.NodeManager import NodeManager
from openadr.node import Node

sub_title = 'Edit Node'

form = cgi.FieldStorage()
old_id = form.getvalue('id')

old_node = NodeManager().getNode(old_id)

if old_node is None:
    print 'Damn.. something wrong, node does not exist with id = %s' % old_id

old_nodeType = old_node.get_nodeType()
old_mode     = old_node.get_mode()
old_profile  = old_node.get_profile()
old_nodeId   = old_node.get_nodeId()
old_ipaddr   = old_node.get_ipaddr()
old_port     = old_node.get_port()
old_prefix   = old_node.get_prefix()


print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.node, action=ACTION.add)


print '<form name="edit_node" action="%s" method="post">' % UPDATE_NODE
print '<input type="hidden" name="action" value="edit">' 
print '<input type="hidden" name="old_id" value="%s">' % old_node.get_nodeId()


# print the table header
print '<table border="1">'
print '<tr><th>Node Parameters</th>'
print '<th>Current Value</th>'
print '<th>New Value</th></tr>'


# Node Type (VEN/VTN/VN)
print '<tr><td>Node Type</td><td>%s</td><td>' % old_nodeType
# drop down - VEN, VTN, VN
print '<select name="node">'
for node in sysCfg.OADR_NODE:
    print '<option%s>%s</option>' % \
          (' selected' if node==old_nodeType else '', node.key)
print '</select>'
print '</td></tr>'


# Mode (PUSH/PULL)
print '<tr><td>Mode</td><td>%s</td><td>' % old_mode
# drop down - PUSH, PULL
print '<select name="mode">'
for mode in sysCfg.OADR_MODE:
    print '<option%s>%s</option>' % \
          (' selected' if mode==old_mode else '', mode.key)
print '</select>'
print '</td></tr>'


# Profile (A/B/C)
print '<tr><td>OADR Profile</td><td>%s</td><td>' % old_profile
# drop down - A, B, C
print '<select name="profile">'
for profile in sysCfg.OADR_PROFILE:
    print '<option%s>%s</option>' % \
          (' selected' if profile==old_profile else '', profile.key)
print '</select>'
print '</td></tr>'


# Node Id
print '<tr><td>Node ID</td><td>%s</td><td>' % old_nodeId
# text box - string/numbers/-/_
print '<input type="text" name="id" value="%s">' % old_nodeId
print '</td></tr>'


# IP Address
print '<tr><td>IP Address</td><td>%s</td><td>' % old_ipaddr
# drop down with list of interfaces!
print '<input type="text" name="ip" value="%s">' % old_ipaddr
print '</td></tr>'


# Port
print '<tr><td>Port</td><td>%s</td><td>' % old_port
# text box - numbers only
print '<input type="text" name="port" value="%s">' % old_port
print '</td></tr>'


# URL Prefix
print '<tr><td>URL Prefix</td><td>%s</td><td>' % old_prefix
# text box - string/numbers/-/_
print '<input type="text" name="prefix" value="%s">' % old_prefix
print '</td></tr>'

print '</table>'

print '<input type="submit" value="Update">'

print '</form>'

print "</body>"
print "</html>"



