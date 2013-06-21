#!/usr/bin/env python

import logging
from openadr.www import *

from openadr import sysconfig as sysCfg
from openadr.node.NodeManager import NodeManager

sub_title = 'Add Node'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.node, action=ACTION.add)


# print the table header
print '<table border="1">'
print '<tr><th>Node Parameters</th>'
print '<th>Value</th></tr>'

print '<form name="add_node" action="%s" method="post">' % UPDATE_NODE
print '<input type="hidden" name="action" value="add">' 


# Node Type (VEN/VTN/VN)
print '<tr><td>Node Type</td><td>'
# drop down - VEN, VTN, VN
print '<select name="node">'
for node in sysCfg.OADR_NODE:
    print '<option>%s</option>' % node.key
print '</select>'
print '</td></tr>'


# Mode (PUSH/PULL)
print '<tr><td>Mode</td><td>'
# drop down - PUSH, PULL
print '<select name="mode">'
for mode in sysCfg.OADR_MODE:
    print '<option>%s</option>' % mode.key
print '</select>'
print '</td></tr>'


# Profile (A/B/C)
print '<tr><td>OADR Profile</td><td>'
# drop down - A, B, C
print '<select name="profile">'
for profile in sysCfg.OADR_PROFILE:
    print '<option>%s</option>' % profile.key
print '</select>'
print '</td></tr>'


# Node Id
print '<tr><td>Node ID</td><td>'
# text box - string/numbers/-/_
print '<input type="text" name="id">'
print '</td></tr>'


# IP Address
print '<tr><td>IP Address</td><td>'
# drop down with list of interfaces!
print '<input type="text" name="ip">'
print '</td></tr>'


# Port
print '<tr><td>Port</td><td>'
# text box - numbers only
print '<input type="text" name="port">' 
print '</td></tr>'


# URL Prefix
print '<tr><td>URL Prefix</td><td>'
# text box - string/numbers/-/_
print '<input type="text" name="prefix">'
print '</td></tr>'

print '</table>'

print '<input type="submit" value="Add">'

print '</form>'

print "</body>"
print "</html>"



