import logging

from openadr.exception import InvalidEiEventId, \
                              InvalidEiEventModificationNumber, \
                              InvalidEiEventPriority, \
                              InvalidEiEventStatus, \
                              InvalidEiEventVTNComment, \
                              InvalidEiEventSignalName, \
                              InvalidEiEventSignalType, \
                              InvalidEiEventSignalId, \
                              InvalidEiEventVENId 

from openadr.validation import valid_positive_integer, \
                               valid_string

from openadr.services.EiEvent import EiEventConfig as evtCfg


def valid_eventId(eventId):
    s = evtCfg.VALID_EVENT_STRING['eventId']
    try:
        valid_string(eventId, s['allowed'], s['min_len'], s['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid EiEvent Id [%s]; Reason: %s ' % (eventId, e)
        raise InvalidEiEventId(msg)


def valid_modificationNumber(modicationNumber):
    try:
        valid_positive_integer(modicationNumber)
        return True
    except Exception, e:
        msg = 'Invalid EiEvent Modification Number [%s]; Reason: %s' % \
              (modicationNumber, e)
        raise InvalidEiEventModificationNumber(msg)


def valid_priority(priority):
    try:
        valid_positive_integer(priority)
        return True
    except Exception, e:
        msg = 'Invalid EiEvent Priority [%s]; Reason: %s' % (priority, e)
        raise InvalidEiEventPriority(msg)


def valid_eiMarketContext(eiMarketContext):
    return True


def valid_createdDateTime(createdDateTime):
    return True


def valid_eventStatus(eventStatus):
    if eventStatus in evtCfg.EVENT_STATUS._values:
        return True
    msg = 'Invalid EiEvent Status [%s]' % eventStatus
    raise InvalidEiEventStatus(msg)


def valid_testEvent(testEvent):
    return True


def valid_vtnComment(vtnComment):
    s = evtCfg.VALID_EVENT_STRING['vtnComment']
    try:
        valid_string(vtnComment, s['allowed'], s['min_len'], s['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid EiEvent VTN Comment [%s]; Reason: %s' % (vtnComment, e)
        raise InvalidEiEventVTNComment(msg)


def valid_dtstart(dtstart):
    return True


def valid_duration(duration):
    return True


def valid_tolerance(tolerance):
    return True


def valid_x_eiNotification(x_eiNotication):
    return True


def valid_x_eiRampUp(x_eiRampUp):
    return True


def valid_x_eiRecovery(x_eiRecovery):
    return True


def valid_components(components):
    return True


def valid_uid(uid):
    return True


def valid_signalPayload(signalPayload):
    return True


def valid_signalName(signalName):
    s = evtCfg.VALID_EVENT_STRING['signalName']
    try:
        valid_string(signalName, s['allowed'], s['min_len'], s['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid EiEvent Signal Name [%s]; Reason: %s' % (signalName, e)
        raise InvalidEiEventSignalName(msg)


def valid_signalType(signalType):
    if signalType in evtCfg.SIGNAL_TYPE._values:
        return True
    msg = 'Invalid EiEvent Signal Type [%s]' % signalType
    raise InvalidEiEventSignalType(msg)


def valid_signalID(signalID):
    s = evtCfg.VALID_EVENT_STRING['signalID']
    try:
        valid_string(signalID, s['allowed'], s['min_len'], s['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid EiEvent Signal Id [%s]; Reason: %s' % (signalID, e)
        raise InvalidEiEventSignalId(msg)


def valid_currentValue(currentValue):
    return True


def valid_groupID(groupID):
    return True


def valid_resourceID(resourceID):
    return True


def valid_venID(venID):
    s = evtCfg.VALID_EVENT_STRING['venID']
    try:
        valid_string(venID, s['allowed'], s['min_len'], s['max_len'])
        return True
    except Exception, e:
        msg = 'Invalid VEN Id [%s]; Reason: %s' % (venID, e)
        raise InvalidEiEventVENId(msg)
    return True


def valid_partyID(partyID):
    return True


