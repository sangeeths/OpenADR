#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
import cgi

from openadr.www import *
from openadr import sysconfig as sysCfg

from openadr.services.EiEvent.EiEventManager import EiEventManager
from openadr.services.EiEvent import EiEvent

from openadr.services.EiEvent import EiEventConfig as evtCfg

from openadr.node.NodeManager import NodeManager

from openadr.services.EiEvent.EiEventUtil import str_to_eievent



max_signals = 5
max_intervals = 5

form = cgi.FieldStorage()

# get the action to be performed - 'add', 'edit', 'delete'
action = form.getvalue('action')


if action == 'add' or action == 'edit':

    sub_title = "Add Event" if action == 'add' else "Edit Event"

    if action == 'edit':
        old_id = form.getvalue('old_id')

    # eventDescriptor
    eventID            = form.getvalue('eventID')
    modificationNumber = form.getvalue('modificationNumber')
    priority           = form.getvalue('priority')
    eiMarketContext    = form.getvalue('eiMarketContext')
    createdDateTime    = form.getvalue('createdDateTime')
    eventStatus        = form.getvalue('eventStatus')
    testEvent          = form.getvalue('testEvent')
    vtnComment         = form.getvalue('vtnComment')

    # eiActivePeriod
    dtstart          = form.getvalue('dtstart')
    duration         = form.getvalue('duration')
    tolerance        = form.getvalue('tolerance')
    x_eiNotification = form.getvalue('x_eiNotification')
    x_eiRampUp       = form.getvalue('x_eiRampUp')
    x_eiRecovery     = form.getvalue('x_eiRecovery')
    components       = form.getvalue('components')

    # eiEventSignals
    # NOTE: no validation done on eiEventSignals 
    # TODO: perform NULL check on this!

    # eiTarget
    resourceID = form.getvalue('resourceID')
    partyID    = form.getvalue('partyID')
    groupID    = form.getvalue('groupID')
    venID      = []
    nodes = NodeManager().getAllNodes()
    for node in nodes:
        if node.nodeType == sysCfg.OADR_NODE.VEN:
            if form.getvalue(node.nodeId):
                venID.append(node.nodeId)
   
    eiEvent = {}
    # eventDescriptor
    eiEvent['eventDescriptor'] = {
    'eventID'            : eventID,
    'modificationNumber' : modificationNumber,
    'priority'           : priority,
    'eiMarketContext'    : eiMarketContext,
    'createdDateTime'    : createdDateTime,
    'eventStatus'        : eventStatus,
    'testEvent'          : testEvent,
    'vtnComment'         : vtnComment,
    }
    # eiActivePeriod
    eiEvent['eiActivePeriod'] = {
    'dtstart'          : dtstart,
    'duration'         : duration,
    'tolerance'        : tolerance,
    'x_eiNotification' : x_eiNotification,
    'x_eiRampUp'       : x_eiRampUp,
    'x_eiRecovery'     : x_eiRecovery,
    'components'       : components,
    }
    # eiEventSignals
    eiEventSignals = []
    for signal in range(max_signals):
        if form.getvalue('cb_eiEventSignal_%d' % signal):
            eiEventSignal = {
                'signalName'   : form.getvalue('signalName_%d' % signal),
                'signalType'   : form.getvalue('signalType_%d' % signal),
                'signalID'     : form.getvalue('signalID_%d' % signal),
                'currentValue' : form.getvalue('currentValue_%d' % signal),
            }
            interval_list = []
            for interval in range(max_intervals):
                if form.getvalue('cb_interval_%d_%d' % (signal, interval)):
                    i = {
                        'uid'           : form.getvalue('uid_%d_%d' % (signal, interval)),
                        'signalPayload' : form.getvalue('signalPayload_%d_%d' % (signal, interval)),
                        'duration'      : form.getvalue('duration_%d_%d' % (signal, interval)),
                    }
                    interval_list.append(i)
            eiEventSignal['intervals'] = interval_list
            eiEventSignals.append(eiEventSignal)
    eiEvent['eiEventSignals'] = eiEventSignals    
    # eiTarget
    eiEvent['eiTarget'] = {
    'groupID'    : groupID,
    'resourceID' : resourceID,
    'venID'      : venID,
    'partyID'    : partyID,
    }

    eiEvent = str_to_eievent(eiEvent)
    
    try:
        event = EiEvent(**eiEvent)
        em = EiEventManager()
        em.addEiEvent(event)
        output = "Event added successfully!!"
        if action == 'edit':
            if old_id != event.eventDescriptor.eventID:
                em.removeEiEvent(old_id)
            output = "Event updated successfully!!"
    except Exception, e:
        output = e
        raise
    next_page = VIEW_EVENT


elif action == 'delete':

    sub_title = 'Delete Event'
    eventId = form.getvalue('id')
    try:
        EiEventManager().removeEiEvent(eventId)
        output = "Event deleted successfully!!"
    except Exception, e:
        output = e
        raise
    
    next_page = DELETE_EVENT
 
   
# incoming action is not 'add', 'edit', 'delete'
else:

    sub_title = 'Invalid action!'
    output = 'Something wrong.. the action is neither add/edit nor delete'
    next_page = VIEW_EVENT




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
print 'Click <a href="%s">here</a> to continue...' % next_page
print "</body>"
print "</html>"


