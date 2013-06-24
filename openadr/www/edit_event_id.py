#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
import cgi
from datetime import datetime, timedelta

from openadr.www import *
from openadr import sysconfig as sysCfg
from openadr.services.EiEvent.EiEventManager import EiEventManager
from openadr.services.EiEvent import EiEventConfig as evtCfg

from openadr.node.NodeManager import NodeManager

max_signals = 5
max_intervals = 5

sub_title = 'Edit Event'

form = cgi.FieldStorage()
old_id = form.getvalue('id')

old_evt = EiEventManager().getEiEvent(old_id)

if old_evt is None:
    print 'Damn.. something wrong, event does not exist with id = %s' % old_id


print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.event, action=ACTION.edit)

print '<form name="edit_event" action="%s" method="post">' % UPDATE_EVENT
print '<input type="hidden" name="action" value="edit">' 
print '<input type="hidden" name="old_id" value="%s">' % old_evt.eventDescriptor.eventID

print '<table border="1">'

# eventDescriptor
print '<tr><th colspan="8">eventDescriptor</th></tr>'
print '<tr>'
print '<th>eventID           </th>'
print '<th>modificationNumber</th>'
print '<th>priority          </th>'
print '<th>eiMarketContext   </th>'
print '<th>createdDateTime   </th>'
print '<th>eventStatus       </th>'
print '<th>testEvent         </th>'
print '<th>vtnComment        </th>'
print '</tr>'
print '<tr>'
print '<td><input type="text" name="eventID" value="%s"></td>' % old_evt.eventDescriptor.eventID
print '<td><input type="text" name="modificationNumber" value="%s"></td>' % old_evt.eventDescriptor.modificationNumber
print '<td><input type="text" name="priority" value="%s"></td>' % old_evt.eventDescriptor.priority
print '<td><input type="text" name="eiMarketContext" value="%s"></td>' % old_evt.eventDescriptor.eiMarketContext
print '<td><input type="text" name="createdDateTime" value="%s"></td>' % old_evt.eventDescriptor.createdDateTime
print '<td>'
print '<select name="eventStatus">'
for eventStatus in evtCfg.EVENT_STATUS:
    print '<option%s>%s</option>' % \
    (' selected' if old_evt.eventDescriptor.eventStatus==eventStatus.key else '' ,eventStatus.key)
print '</select>'
print '</td>' 
print '<td>'
print '<select name="testEvent">' 
if old_evt.eventDescriptor.testEvent == "True":
    print '<option selected>True</option>'
    print '<option>False</option>'
else:
    print '<option>True</option>'
    print '<option selected>False</option>'
print '</select>'
print '</td>' 
print '<td><input type="text" name="vtnComment" value="%s"></td>' % old_evt.eventDescriptor.vtnComment
print '</tr>'
 
# eiActivePeriod
print '<tr><th colspan="8">eiActivePeriod</th></tr>'
print '<tr><th>properties</th></tr>'
print '<tr>'
print '<th>dtstart         </th>'
print '<th>duration        </th>'
print '<th>tolerance       </th>'
print '<th>x_eiNotification</th>'
print '<th>x_eiRampUp      </th>'
print '<th>x_eiRecovery    </th>'
print '</tr>'
print '<tr>'
# start time is 30 minutes from now
print '<td><input type="text" name="dtstart" value="%s"></td>' % old_evt.eiActivePeriod.dtstart
print '<td><input type="text" name="duration" value="%s"></td>' % old_evt.eiActivePeriod.duration
print '<td><input type="text" name="tolerance" value="%s"></td>' % old_evt.eiActivePeriod.tolerance
print '<td><input type="text" name="x_eiNotification" value="%s"></td>' % old_evt.eiActivePeriod.x_eiNotification
print '<td><input type="text" name="x_eiRampUp" value="%s"></td>' % old_evt.eiActivePeriod.x_eiRampUp
print '<td><input type="text" name="x_eiRecovery" value="%s"></td>' % old_evt.eiActivePeriod.x_eiRecovery
print '</tr>'
print '<tr>'
print '<th>components</th>'
print '</tr>'
print '<tr>'
print '<td><input type="text" name="components" value="%s"></td>' % old_evt.eiActivePeriod.components
print '</tr>'

# eiEventSignals
print '<tr><th colspan="8">eiEventSignals</th></tr>'
#evt['EventID']['eiEventSignals'][0]['intervals'][0]
#eiEventSignals = old_evt.eiEventSignals

old_evt_d = old_evt.getDict()

# s = signal index
def get_signalItem(item, s): 
    if s < len(old_evt_d['eiEventSignals']):
        return old_evt_d['eiEventSignals'][s][item]
    return ''

# s = signal index
def signalItem_checked(s):
    if s < len(old_evt_d['eiEventSignals']):
        return 'checked'
    return ''

# s = signal index
# i = interval index
def get_intervalItem(item, s, i): 
    if s < len(old_evt_d['eiEventSignals']):
        if i < len(old_evt_d['eiEventSignals'][s]['intervals']):
            return old_evt_d['eiEventSignals'][s]['intervals'][i][item]
    return ''

# s = signal index 
# i = interval index
def intervalItem_checked(s, i): 
    if s < len(old_evt_d['eiEventSignals']):
        if i < len(old_evt_d['eiEventSignals'][s]['intervals']):
            return 'checked'
    return ''


for signal in range(max_signals):
    print '<tr>'
    print '<th>[%d] eiEventSignal <br>' % signal
    print '<input type="checkbox" name="cb_eiEventSignal_%d" value="Add this!"%s>Add this!</th>' % (signal, signalItem_checked(signal))
    print '</tr>'
    print '<tr>'
    print '<th>signalName  </th>'
    print '<th>signalType  </th>'
    print '<th>signalID    </th>'
    print '<th>currentValue</th>'
    print '</tr>'
    print '<tr>'
    print '<td><input type="text" name="signalName_%d" value="%s"></td>' % (signal, get_signalItem('signalName', signal))
    print '<td>'
    print '<select name="signalType_%d">' % signal
    st = get_signalItem('signalType', signal)
    for signalType in evtCfg.SIGNAL_TYPE:
        print '<option%s>%s</option>' % \
              (' selected' if st == signalType.key else '' , signalType.key)
    print '</select>'
    print '</td>'
    print '<td><input type="text" name="signalID_%d" value="%s"></td>' % (signal, get_signalItem('signalID', signal))
    print '<td><input type="text" name="currentValue_%d" value="%s"></td>' % (signal, get_signalItem('currentValue', signal))
    print '</tr>'
    # intervals
    print '<tr><th>[%d] intervals</th></tr>' % signal
    print '<tr>'
    print '<th>duration</th>'
    print '<th>uid</th>'
    print '<th>signalPayload</th>'
    print '<th>Add this!</th>'
    print '</tr>'
    for interval in range(max_intervals):
        print '<tr>'
        print '<td><input type="text" name="%d_duration_%d" value="%s"></td>' % (signal, interval, get_intervalItem('duration', signal, interval))
        print '<td><input type="text" name="%d_uid_%d" value="%s"></td>' % (signal, interval, get_intervalItem('uid', signal, interval))
        print '<td><input type="text" name="%d_signalPayload_%d" value="%s"></td>' % (signal, interval, get_intervalItem('signalPayload', signal, interval))
        print '<td><input type="checkbox" name="cb_%d_interval_%d"%s></th>' % (signal, interval, intervalItem_checked(signal, interval))
        print '</tr>'
        
# eiTarget
print '<tr><th colspan="8">eiTarget</th></tr>'
print '<tr>'
print '<th>groupID</th>'
print '<th>resourceID</th>'
print '<th>venID</th>'
print '<th>partyID</th>'
print '</tr>'
print '<tr>'
print '<td><input type="text" name="groupID" value="%s"></td>' % old_evt.eiTarget.groupID
print '<td><input type="text" name="resourceID" value="%s"></td>' % old_evt.eiTarget.resourceID
print '<td>'
venID = old_evt.eiTarget.venID
venID = venID.split(';')
nm = NodeManager()
nodes = nm.getAllNodes()
for node in nodes:
    if node.get_nodeType() == sysCfg.OADR_NODE.VEN:
        nodeId = node.get_nodeId()
        print '<input type="checkbox" name="%s"%s>%s<br>' % \
        (nodeId, ' checked' if nodeId in venID else '', nodeId)
print '</td>'
print '<td><input type="text" name="partyID" value="%s"></td>' % old_evt.eiTarget.partyID
print '</tr>'

print '</table>'
print '<br>'

print '<input type="submit" value="Update">'

print '</form>'

print "</body>"
print "</html>"



