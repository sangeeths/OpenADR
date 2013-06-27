
from openadr.util2 import str_to_enum

from openadr.exception import InvalidEiEventStatus, \
                              InvalidEiEventSignalType, \
                              InvalidEiEventResponseRequired

from openadr.services.EiEvent import EiEventConfig as evtCfg

def eievent_to_str(event_d):
    event_d['eventDescriptor']['eventStatus'] = str(event_d['eventDescriptor']['eventStatus'])
    for es in event_d['eiEventSignals']:
        es['signalType'] = str(es['signalType'])
    return event_d

def str_to_eievent(event_d):
    event_d['eventDescriptor']['eventStatus'] = \
        get_event_status_from_str(event_d['eventDescriptor']['eventStatus'])
    for es in event_d['eiEventSignals']:
        es['signalType'] = get_signal_type_from_str(es['signalType'])
    return event_d

def get_event_status_from_str(eventStatus):
    try:
        return str_to_enum(evtCfg.EVENT_STATUS, eventStatus)
    except Exception, e:
        msg = 'Invalid EiEvent Status [%s]; Reason: %s' % \
              (eventStatus, e)
        raise InvalidEiEventStatus(msg)

def get_signal_type_from_str(signalType):
    try:
        return str_to_enum(evtCfg.SIGNAL_TYPE, signalType)
    except Exception, e:
        msg = 'Invalid EiEvent Signal Type [%s]; Reason: %s' % \
              (signalType, e)
        raise InvalidEiEventSignalType(msg)

def get_response_required_from_str(RespRequired):
    try:
        return str_to_enum(evtCfg.RESPONSE_REQUIRED, RespRequired)
    except Exception, e:
        msg = 'Invalid EiEvent Response Required Value [%s]; ' \
              'Reason: %s' % (RespRequired, e)
        raise InvalidEiEventResponseRequired(msg)



