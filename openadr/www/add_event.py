#!/usr/bin/env python

import logging
from datetime import datetime, timedelta

from openadr.www import *
from openadr import sysconfig as sysCfg
from openadr.services.EiEvent.EiEventManager import EiEventManager
from openadr.services.EiEvent import EiEventConfig as evtCfg

from openadr.node.NodeManager import NodeManager

max_signals = 5
max_intervals = 5

sub_title = 'Add Event'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.event, action=ACTION.add)

print '<form name="add_event" action="%s" method="post">' % UPDATE_EVENT
print '<input type="hidden" name="action" value="add">' 

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
print '<td><input type="text" name="eventID" value="EventID"></td>' 
print '<td><input type="text" name="modificationNumber" value="0"></td>' 
print '<td><input type="text" name="priority" value="0"></td>' 
print '<td><input type="text" name="eiMarketContext" value="http://tempuri.org"></td>' 
print '<td><input type="text" name="createdDateTime" value="%s"></td>' % \
      datetime.now().isoformat()
print '<td>'
print '<select name="eventStatus">'
for eventStatus in evtCfg.EVENT_STATUS:
    print '<option>%s</option>' % eventStatus.key
print '</select>'
print '</td>' 
print '<td>'
print '<select name="testEvent">'
print '<option>True</option>'
print '<option selected>False</option>'
print '</select>'
print '</td>' 
print '<td><input type="text" name="vtnComment" value="sample comment"></td>' 
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
print '<td><input type="text" name="dtstart" value="%s"></td>' % \
      (datetime.now() + timedelta(minutes=30)).isoformat() 
print '<td><input type="text" name="duration" value="%s"></td>' % 'PT1H'
print '<td><input type="text" name="tolerance" value="%s"></td>' % 'PT2H'
print '<td><input type="text" name="x_eiNotification" value="%s"></td>' % 'PT3H'
print '<td><input type="text" name="x_eiRampUp" value="%s"></td>' % 'PT4H'
print '<td><input type="text" name="x_eiRecovery" value="%s"></td>' % 'PT5H'
print '</tr>'
print '<tr>'
print '<th>components</th>'
print '</tr>'
print '<tr>'
print '<td><input type="text" name="components" value="None"></td>' 
print '</tr>'

# eiEventSignals
print '<tr><th colspan="8">eiEventSignals</th></tr>'
for signal in range(max_signals):
    print '<tr>'
    print '<th>[%d] eiEventSignal <br>' % signal
    print '<input type="checkbox" name="cb_eiEventSignal_%d" value="Add this!">Add this!</th>' % signal
    print '</tr>'
    print '<tr>'
    print '<th>signalName  </th>'
    print '<th>signalType  </th>'
    print '<th>signalID    </th>'
    print '<th>currentValue</th>'
    print '</tr>'
    print '<tr>'
    print '<td><input type="text" name="signalName_%d" value="signalName_%d"></td>' % (signal, signal)
    print '<td>'
    print '<select name="signalType_%d">' % signal
    for signalType in evtCfg.SIGNAL_TYPE:
        print '<option>%s</option>' % signalType.key
    print '</select>'
    print '</td>'
    print '<td><input type="text" name="signalID_%d" value="signalID_%d"></td>' % (signal, signal)
    print '<td><input type="text" name="currentValue_%d" value="0"></td>' % signal
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
        print '<td><input type="text" name="duration_%d_%d" value="%s"></td>' % (signal, interval, 'PT1H')
        print '<td><input type="text" name="uid_%d_%d" value="uid_%d_%d"></td>' % (signal, interval, signal, interval)
        print '<td><input type="text" name="signalPayload_%d_%d" value="%s"></td>' % (signal, interval, '0.0')
        print '<td><input type="checkbox" name="cb_interval_%d_%d"></th>' % (signal, interval)
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
print '<td><input type="text" name="groupID" value="testGroupID"></td>' 
print '<td><input type="text" name="resourceID" value="testResourceID"></td>' 
print '<td>'
nm = NodeManager()
nodes = nm.getAllNodes()
for node in nodes:
    if node.nodeType == sysCfg.OADR_NODE.VEN:
        print '<input type="checkbox" name="%s">%s<br>' % (node.nodeId, node.nodeId)
print '</td>'
print '<td><input type="text" name="partyID" value="testPartyID"></td>' 
print '</tr>'

print '</table>'
print '<br>'

print '<input type="submit" value="Add">'

print '</form>'

print "</body>"
print "</html>"



