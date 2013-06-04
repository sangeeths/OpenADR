from openadr.exception import UnknownEiEventMessage

from openadr import config as oadrCfg
from openadr.util import *

from openadr.services.EiEvent import EiEvent as EiEvent
from openadr.services.EiEvent.message import *

# global variable for frequent reference
service = oadrCfg.OADR_SERVICE.EiEvent


def Response(request_h):
    #
    # TIP: 'incoming_msg' is a type (Enum)
    #      'outgoing_msg' is a string (xml data)
    #
    # TIP: any variable with suffix _h is a handle 
    #      to lxml; for example, 'request_h' is an
    #      lxml handle to the requset xml data
    #

    print "EiEventManager :: Response :: request = %s" % request_h
    incoming_msg = get_oadr_msg(service, request_h)

    # incoming : oadrDistributeEvent : vtn -> ven 
    # outgoing : oadrCreatedEvent    : vtn <- ven 
    if incoming_msg == oadrCfg.OADR_EIEVENT.oadrDistributeEvent:
        oadrDE       = read_oadrDistributeEvent_msg(request_h)
        events_out   = process_oadrDistributeEvent_msg(**oadrDE)
        outgoing_msg = compose_oadrCreatedEvent_msg(events_out)
        return outgoing_msg

    # incoming : oadrCreatedEvent : vtn <- ven 
    # outgoing : oadrResponse     : vtn -> ven 
    elif incoming_msg == oadrCfg.OADR_EIEVENT.oadrCreatedEvent:
        events_created   = read_oadrCreatedEvent_msg(request_h)
        events_processed = process_oadrCreatedEvent_msg(events_created)
        outgoing_msg     = compose_oadrResponse_msg(events_processed)
        return outgoing_msg

    # incoming : oadrRequestEvent    : vtn <- ven 
    # outgoing : oadrDistributeEvent : vtn -> ven 
    elif incoming_msg == oadrCfg.OADR_EIEVENT.oadrRequestEvent:
        events_requested = read_oadrRequestEvent_msg(request_h)
        events_created   = process_oadrRequestEvent_msg(events_requested)
        outgoing_msg     = compose_oadrDistributeEvent_msg(events_created)
        return outgoing_msg

    # incoming : oadrResponse : vtn -> ven (for oadrCreatedEvent)
    #                           vtn <- ven (for oadrDistributeEvent)
    # outgoing : ??
    elif incoming_msg == oadrCfg.OADR_EIEVENT.oadrResponse:
        response = read_oadrResponse_msg(request_h)
        process_oadrResponse_msg(response)
        return None

    else:
        raise UnknownEiEventMessage
        return None
        


