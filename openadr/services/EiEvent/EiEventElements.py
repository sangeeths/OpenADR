from openadr.util import get_schema_ns as __get_schema_ns

# well defined namespaces
# from openadr schema
__ei   = __get_schema_ns(prefix='ei')
__emix = __get_schema_ns(prefix='emix')
__oadr = __get_schema_ns(prefix='oadr')
__pyld = __get_schema_ns(prefix='pyld')
__strm = __get_schema_ns(prefix='strm')
__xcal = __get_schema_ns(prefix='xcal')

# namespace format
__nsfmt = '{%s}%s'

#
# the following are the xml elements 
# for all oadr messages
#   -> with fully qualified oadr namespace
#   -> lxml etree compatible element names
#
# NOTE: sorted with element name
#
components           = __nsfmt % (__xcal, 'components')
createdDateTime      = __nsfmt % (__ei,   'createdDateTime')
currentValue         = __nsfmt % (__ei,   'currentValue')
date_time            = __nsfmt % (__xcal, 'date-time')
dtstart              = __nsfmt % (__xcal, 'dtstart')
duration             = __nsfmt % (__xcal, 'duration')
eiActivePeriod       = __nsfmt % (__ei,   'eiActivePeriod')
eiCreatedEvent       = __nsfmt % (__pyld, 'eiCreatedEvent')
eiEvent              = __nsfmt % (__ei,   'eiEvent')
eiEventSignal        = __nsfmt % (__ei,   'eiEventSignal')
eiEventSignals       = __nsfmt % (__ei,   'eiEventSignals')
eiMarketContext      = __nsfmt % (__ei,   'eiMarketContext')
eiRequestEvent       = __nsfmt % (__pyld, 'eiRequestEvent')
eiResponse           = __nsfmt % (__ei,   'eiResponse')
eiTarget             = __nsfmt % (__ei,   'eiTarget')
eventDescriptor      = __nsfmt % (__ei,   'eventDescriptor')
eventID              = __nsfmt % (__ei,   'eventID')
eventResponse        = __nsfmt % (__ei,   'eventResponse')
eventResponses       = __nsfmt % (__ei,   'eventResponses')
eventStatus          = __nsfmt % (__ei,   'eventStatus')
groupID              = __nsfmt % (__ei,   'groupID')
interval             = __nsfmt % (__ei,   'interval')
intervals            = __nsfmt % (__strm, 'intervals')
marketContext        = __nsfmt % (__emix, 'marketContext')
modificationNumber   = __nsfmt % (__ei,   'modificationNumber')
oadrCreatedEvent     = __nsfmt % (__oadr, 'oadrCreatedEvent')
oadrDistributeEvent  = __nsfmt % (__oadr, 'oadrDistributeEvent')
oadrEvent            = __nsfmt % (__oadr, 'oadrEvent')
oadrRequestEvent     = __nsfmt % (__oadr, 'oadrRequestEvent')
oadrResponse         = __nsfmt % (__oadr, 'oadrResponse')
oadrResponseRequired = __nsfmt % (__oadr, 'oadrResponseRequired')
optType              = __nsfmt % (__ei,   'optType')
partyID              = __nsfmt % (__ei,   'partyID')
payloadFloat         = __nsfmt % (__ei,   'payloadFloat')
priority             = __nsfmt % (__ei,   'priority')
properties           = __nsfmt % (__xcal, 'properties')
qualifiedEventID     = __nsfmt % (__ei,   'qualifiedEventID')
replyLimit           = __nsfmt % (__pyld, 'replyLimit')
requestID            = __nsfmt % (__pyld, 'requestID')
resourceID           = __nsfmt % (__ei,   'resourceID')
responseCode         = __nsfmt % (__ei,   'responseCode')
responseDescription  = __nsfmt % (__ei,   'responseDescription')
signalID             = __nsfmt % (__ei,   'signalID')
signalName           = __nsfmt % (__ei,   'signalName')
signalPayload        = __nsfmt % (__ei,   'signalPayload')
signalType           = __nsfmt % (__ei,   'signalType')
startafter           = __nsfmt % (__xcal, 'startafter')
testEvent            = __nsfmt % (__ei,   'testEvent')
text                 = __nsfmt % (__xcal, 'text')
tolerance            = __nsfmt % (__xcal, 'tolerance')
tolerate             = __nsfmt % (__xcal, 'tolerate')
uid                  = __nsfmt % (__xcal, 'uid')
value                = __nsfmt % (__ei,   'value')
venID                = __nsfmt % (__ei,   'venID')
vtnComment           = __nsfmt % (__ei,   'vtnComment')
vtnID                = __nsfmt % (__ei,   'vtnID')
x_eiNotification     = __nsfmt % (__ei,   'x-eiNotification')
x_eiRampUp           = __nsfmt % (__ei,   'x-eiRampUp')
x_eiRecovery         = __nsfmt % (__ei,   'x-eiRecovery')

