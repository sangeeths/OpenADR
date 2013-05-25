from openadr.util import get_schema_ns

# well defined namespaces
# from openadr schema
ei   = get_schema_ns(prefix='ei')
emix = get_schema_ns(prefix='emix')
oadr = get_schema_ns(prefix='oadr')
pyld = get_schema_ns(prefix='pyld')
strm = get_schema_ns(prefix='strm')
xcal = get_schema_ns(prefix='xcal')

# namespace format
nsfmt = '{%s}%s'

#
# the following are the xml elements 
# for all oadr messages
#   -> with fully qualified oadr namespace
#   -> lxml etree compatible element names
#
# NOTE: sorted with element name
#
components           = nsfmt % (xcal, 'components')
createdDateTime      = nsfmt % (ei,   'createdDateTime')
currentValue         = nsfmt % (ei,   'currentValue')
date_time            = nsfmt % (xcal, 'date-time')
dtstart              = nsfmt % (xcal, 'dtstart')
duration             = nsfmt % (xcal, 'duration')
eiActivePeriod       = nsfmt % (ei,   'eiActivePeriod')
eiCreatedEvent       = nsfmt % (pyld, 'eiCreatedEvent')
eiEvent              = nsfmt % (ei,   'eiEvent')
eiEventSignal        = nsfmt % (ei,   'eiEventSignal')
eiEventSignals       = nsfmt % (ei,   'eiEventSignals')
eiMarketContext      = nsfmt % (ei,   'eiMarketContext')
eiRequestEvent       = nsfmt % (pyld, 'eiRequestEvent')
eiResponse           = nsfmt % (ei,   'eiResponse')
eiTarget             = nsfmt % (ei,   'eiTarget')
eventDescriptor      = nsfmt % (ei,   'eventDescriptor')
eventID              = nsfmt % (ei,   'eventID')
eventResponse        = nsfmt % (ei,   'eventResponse')
eventResponses       = nsfmt % (ei,   'eventResponses')
eventStatus          = nsfmt % (ei,   'eventStatus')
groupID              = nsfmt % (ei,   'groupID')
interval             = nsfmt % (ei,   'interval')
intervals            = nsfmt % (strm, 'intervals')
marketContext        = nsfmt % (emix, 'marketContext')
modificationNumber   = nsfmt % (ei,   'modificationNumber')
oadrCreatedEvent     = nsfmt % (oadr, 'oadrCreatedEvent')
oadrDistributeEvent  = nsfmt % (oadr, 'oadrDistributeEvent')
oadrEvent            = nsfmt % (oadr, 'oadrEvent')
oadrRequestEvent     = nsfmt % (oadr, 'oadrRequestEvent')
oadrResponse         = nsfmt % (oadr, 'oadrResponse')
oadrResponseRequired = nsfmt % (oadr, 'oadrResponseRequired')
optType              = nsfmt % (ei,   'optType')
partyID              = nsfmt % (ei,   'partyID')
payloadFloat         = nsfmt % (ei,   'payloadFloat')
priority             = nsfmt % (ei,   'priority')
properties           = nsfmt % (xcal, 'properties')
qualifiedEventID     = nsfmt % (ei,   'qualifiedEventID')
replyLimit           = nsfmt % (pyld, 'replyLimit')
requestID            = nsfmt % (pyld, 'requestID')
resourceID           = nsfmt % (ei,   'resourceID')
responseCode         = nsfmt % (ei,   'responseCode')
responseDescription  = nsfmt % (ei,   'responseDescription')
signalID             = nsfmt % (ei,   'signalID')
signalName           = nsfmt % (ei,   'signalName')
signalPayload        = nsfmt % (ei,   'signalPayload')
signalType           = nsfmt % (ei,   'signalType')
startafter           = nsfmt % (xcal, 'startafter')
testEvent            = nsfmt % (ei,   'testEvent')
text                 = nsfmt % (xcal, 'text')
tolerance            = nsfmt % (xcal, 'tolerance')
tolerate             = nsfmt % (xcal, 'tolerate')
uid                  = nsfmt % (xcal, 'uid')
value                = nsfmt % (ei,   'value')
venID                = nsfmt % (ei,   'venID')
vtnComment           = nsfmt % (ei,   'vtnComment')
vtnID                = nsfmt % (ei,   'vtnID')
x_eiNotification     = nsfmt % (ei,   'x-eiNotification')
x_eiRampUp           = nsfmt % (ei,   'x-eiRampUp')
x_eiRecovery         = nsfmt % (ei,   'x-eiRecovery')

