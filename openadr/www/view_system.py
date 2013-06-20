#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
from openadr.www import *

from openadr.system import NODE, MODE, PROFILE, ID, IPADDR, \
                           PORT, PREFIX, GUI_PORT, SUMMARY

sub_title = 'View System Configuration'
logging.info(sub_title)

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.system, action=ACTION.view)

print '<table border="1">'
print '<tr><th>System Parameters</th><th>Values</th></tr>'
print '<tr><td>Node Type   </td><td>%s</td></tr>' % NODE
print '<tr><td>Mode        </td><td>%s</td></tr>' % MODE
print '<tr><td>OADR Profile</td><td>%s</td></tr>' % PROFILE
print '<tr><td>Node ID     </td><td>%s</td></tr>' % ID
print '<tr><td>IP Address  </td><td>%s</td></tr>' % IPADDR
print '<tr><td>Port        </td><td>%s</td></tr>' % PORT
print '<tr><td>URL Prefix  </td><td>%s</td></tr>' % PREFIX
print '<tr><td>Summary     </td><td>%s</td></tr>' % SUMMARY
print '<tr><td>GUI Port    </td><td>%s</td></tr>' % GUI_PORT
print '</table>'

print "</body>"
print "</html>"



