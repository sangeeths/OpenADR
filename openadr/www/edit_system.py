#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
from openadr.www import *
from openadr import sysconfig as sysCfg

from openadr.system import NODE, MODE, PROFILE, ID, IPADDR, \
                           PORT, PREFIX, GUI_PORT, SUMMARY

sub_title = 'Edit System Configuration'
logging.info(sub_title)


print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.system, action=ACTION.edit)

# print the table header
print '<table border="1">'
print '<tr><th>System Parameters</th>'
print '<th>Current Value</th>'
print '<th>New Value</th></tr>'

print '<form name="edit_system" action="%s" method="post">' % UPDATE_SYSTEM


# Node Type (VEN/VTN/VN)
print '<tr><td>Node Type</td><td>%s</td><td>' % NODE
# drop down - VEN, VTN, VN
print '<select name="node">'
for node in sysCfg.OADR_NODE:
    print '<option%s>%s</option>' % \
          (' selected' if node==NODE else '', node.key)
print '</select>'
print '</td></tr>'


# Mode (PUSH/PULL)
print '<tr><td>Mode</td><td>%s</td><td>' % MODE
# drop down - PUSH, PULL
print '<select name="mode">'
for mode in sysCfg.OADR_MODE:
    print '<option%s>%s</option>' % \
          (' selected' if mode==MODE else '', mode.key)
print '</select>'
print '</td></tr>'


# Profile (A/B/C)
print '<tr><td>OADR Profile</td><td>%s</td><td>' % PROFILE
# drop down - A, B, C
print '<select name="profile">'
for profile in sysCfg.OADR_PROFILE:
    print '<option%s>%s</option>' % \
          (' selected' if profile==PROFILE else '', profile.key)
print '</select>'
print '</td></tr>'


# Node Id
print '<tr><td>Node ID</td><td>%s</td><td>' % ID
# text box - string/numbers/-/_
print '<input type="text" name="id" value="%s">' % ID
print '</td></tr>'


# IP Address
print '<tr><td>IP Address</td><td>%s</td><td>' % IPADDR
# drop down with list of interfaces!
ipaddr = get_ip_address()
print '<select name="ip">'
for ip in ipaddr.values():
    print '<option%s>%s</option>' % \
          (' selected' if ip==IPADDR else '', ip)
print '</select>'
print '</td></tr>'


# Port
print '<tr><td>Port</td><td>%s</td><td>' % PORT
# text box - numbers only
print '<input type="text" name="port" value="%s">' % PORT
print '</td></tr>'


# URL Prefix
print '<tr><td>URL Prefix</td><td>%s</td><td>' % PREFIX
# text box - string/numbers/-/_
print '<input type="text" name="prefix" value="%s">' % PREFIX
print '</td></tr>'


# Summary
# NOTE: Do not allow to change this!
print '<tr><td>Summary</td><td>%s</td><td>' % SUMMARY
# text box - GRAY this!
print SUMMARY
print '<input type="hidden" name="summary" value="%s">' % SUMMARY
print '</td></tr>'


# GUI Port
print '<tr><td>GUI Port</td><td>%s</td><td>' % GUI_PORT
# text box - numbers only
print '<input type="text" name="gui_port" value="%s">' % GUI_PORT
print '</td></tr>'

print '</table>'

print '<input type="submit" value="Update">'

print '</form>'

print "</body>"
print "</html>"


