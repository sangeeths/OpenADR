#!/usr/bin/env python

import logging
from openadr.www import *
from openadr.services.EiEvent.EiEventManager import EiEventManager

sub_title = 'Edit Event'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.event, action=ACTION.edit)

print '<table border="1">'
print '<tr><th>Event ID</th><th>Edit</th></tr>'
events = EiEventManager().getAllEiEvents()

for event in events:
    print '<form name="edit_event" action="%s" method="post">' % EDIT_EVENT_ID
    print '<tr>'
    print '<input type="hidden" name="action" value="edit">'
    print '<input type="hidden" name="id" value="%s">' % event.eventDescriptor.eventID
    print '<td>%s</td>' % event.eventDescriptor.eventID
    print '<td><input type="submit" value="Edit"></td>'
    print '</tr>'
    print '</form>'

print '</table>'

print "</body>"
print "</html>"


