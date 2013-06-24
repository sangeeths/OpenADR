#!/usr/bin/env python

import logging
from openadr.www import *

from openadr.services.EiEvent.EiEventManager import EiEventManager

sub_title = 'View Event(s)'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print header(sub_title, page=PAGE.event, action=ACTION.view)

events = EiEventManager().getAllEiEvents()

print 'Total number of Events configured = %d<br><br>' % len(events)
for event in events:

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
    print '<td>%s</td>' % event.eventDescriptor.eventID
    print '<td>%s</td>' % event.eventDescriptor.modificationNumber
    print '<td>%s</td>' % event.eventDescriptor.priority
    print '<td>%s</td>' % event.eventDescriptor.eiMarketContext
    print '<td>%s</td>' % event.eventDescriptor.createdDateTime
    print '<td>%s</td>' % event.eventDescriptor.eventStatus
    print '<td>%s</td>' % event.eventDescriptor.testEvent
    print '<td>%s</td>' % event.eventDescriptor.vtnComment
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
    print '<td>%s</td>' % event.eiActivePeriod.dtstart
    print '<td>%s</td>' % event.eiActivePeriod.duration
    print '<td>%s</td>' % event.eiActivePeriod.tolerance
    print '<td>%s</td>' % event.eiActivePeriod.x_eiNotification
    print '<td>%s</td>' % event.eiActivePeriod.x_eiRampUp
    print '<td>%s</td>' % event.eiActivePeriod.x_eiRecovery
    print '</tr>'
    print '<tr>'
    print '<th>components</th>'
    print '</tr>'
    print '<tr>'
    print '<td>%s</td>' % event.eiActivePeriod.components
    print '</tr>'

    # eiEventSignals
    print '<tr><th colspan="8">eiEventSignals</th></tr>'
    for eventSignal in event.eiEventSignals:
        print '<tr><th>eiEventSignal</th></tr>'
        print '<tr>'
        print '<th>signalName  </th>'
        print '<th>signalType  </th>'
        print '<th>signalID    </th>'
        print '<th>currentValue</th>'
        print '</tr>'
        print '<tr>'
        print '<td>%s</td>' % eventSignal.signalName
        print '<td>%s</td>' % eventSignal.signalType
        print '<td>%s</td>' % eventSignal.signalID
        print '<td>%s</td>' % eventSignal.currentValue
        print '</tr>'
        # intervals
        print '<tr><th>intervals</th></tr>'
        print '<tr>'
        print '<th>duration</th>'
        print '<th>uid</th>'
        print '<th>signalPayload</th>'
        print '</tr>'
        for interval in eventSignal.intervals:
            print '<tr>'
            print '<td>%s</td>' % interval.duration
            print '<td>%s</td>' % interval.uid
            print '<td>%s</td>' % interval.signalPayload
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
    print '<td>%s</td>' % event.eiTarget.groupID
    print '<td>%s</td>' % event.eiTarget.resourceID
    print '<td>%s</td>' % event.eiTarget.venID
    print '<td>%s</td>' % event.eiTarget.partyID
    print '</tr>'

    print '</table>'
    print '<br><br><br>'



print "</body>"
print "</html>"



