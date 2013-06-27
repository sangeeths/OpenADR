import logging
import json
import os
from threading import Lock as Lock 

from openadr.util import *
from openadr.exception import UnknownEiEventMessage
from openadr.services.EiEvent import EiEvent
from openadr.services.EiEvent.EiEventMessages import *

from openadr.services.EiEvent.EiEventUtil import str_to_eievent, \
                                                 eievent_to_str


# global variable for frequent reference
service = sysCfg.OADR_SERVICE.EiEvent

         
def Load_EiEventStore(filename=sysCfg.EIEVENT_STORE):
    # if the EiEvent configuration file does not exist
    # then simple return {}
    if not os.path.exists(filename):
        logging.debug('Unable to load EiEvent(s) Information; ' \
                      '%s not present' % filename)
        return {}
    with open(filename, 'r') as file_h:
        EiEventCfg = json.load(file_h)
    event_store = {}
    for eventId, event in EiEventCfg.iteritems():
        event_d = str_to_eievent(event)
        event_store[eventId] = EiEvent(**event_d)
    logging.debug('Loaded %d EiEvents(s) from %s' % \
                 (len(EiEventCfg), filename))
    return event_store


def Save_EiEventStore(event_store, event_store_lock, 
                      filename=sysCfg.EIEVENT_STORE):
    event_store_lock.acquire()
    try:
        event_dict = {}
        # key = eventId
        # value = dict(object of type EiEvent())
        for eventId, event in event_store.iteritems():
            event_dict[eventId] = eievent_to_str(event.getDict())
        with open(filename, 'w') as file_h:
            json.dump(event_dict, file_h)
        logging.debug('Saved %d EiEvent(s) to %s' % \
                     (len(event_dict), filename))
    finally:
        event_store_lock.release()



class EiEventManager:
    __event_store_lock = Lock()
    __event_store = Load_EiEventStore()
    
    def __init__(self): 
        pass
 
    def getAllEiEvents(self):
        return EiEventManager.__event_store.values()

    def getEiEvent(self, eventId):
        if eventId not in EiEventManager.__event_store:
            return False     
        return EiEventManager.__event_store[eventId]

    def removeEiEvent(self, eventId):
        if eventId not in EiEventManager.__event_store:
            return False     
        EiEventManager.__event_store_lock.acquire()
        del EiEventManager.__event_store[eventId]
        EiEventManager.__event_store_lock.release()
        Save_EiEventStore(EiEventManager.__event_store, EiEventManager.__event_store_lock)
        return True

    def addEiEvent(self, eiEvent):
        EiEventManager.__event_store_lock.acquire()
        EiEventManager.__event_store[eiEvent.eventDescriptor.eventID] = eiEvent
        EiEventManager.__event_store_lock.release()
        Save_EiEventStore(EiEventManager.__event_store, EiEventManager.__event_store_lock)
        logging.info('EiEventManager::addEiEvent() successful for the following event:')
        logging.info(str(eiEvent))
 
    def process_oadrDistributeEvent_msg(self, **kwargs):
        for event in kwargs['EiEvents']:
            self.addEiEvent(event)   




       

def Response(request_h):
    #
    # TIP: 'incoming_msg' is a type (Enum)
    #      'outgoing_msg' is a string (xml data)
    #
    # TIP: any variable with suffix _h is a handle 
    #      to lxml; for example, 'request_h' is an
    #      lxml handle to the requset xml data
    #
    
    # create an instance of EiEventManager
    # to perform process_XXX_msg() functions
    em = EiEventManager()

    incoming_msg = get_oadr_msg(service, request_h)

    # incoming : oadrDistributeEvent : vtn -> ven 
    # outgoing : oadrCreatedEvent    : vtn <- ven 
    if incoming_msg == sysCfg.OADR_EIEVENT.oadrDistributeEvent:
        oadrDE         = read_oadrDistributeEvent_msg(request_h)
        events_created = em.process_oadrDistributeEvent_msg(**oadrDE)
        outgoing_msg   = compose_oadrCreatedEvent_msg(events_created)
        return outgoing_msg

    # incoming : oadrCreatedEvent : vtn <- ven 
    # outgoing : oadrResponse     : vtn -> ven 
    elif incoming_msg == sysCfg.OADR_EIEVENT.oadrCreatedEvent:
        events_created   = read_oadrCreatedEvent_msg(request_h)
        events_processed = process_oadrCreatedEvent_msg(events_created)
        outgoing_msg     = compose_oadrResponse_msg(events_processed)
        return outgoing_msg

    # incoming : oadrRequestEvent    : vtn <- ven 
    # outgoing : oadrDistributeEvent : vtn -> ven 
    elif incoming_msg == sysCfg.OADR_EIEVENT.oadrRequestEvent:
        events_requested = read_oadrRequestEvent_msg(request_h)
        events_created   = process_oadrRequestEvent_msg(events_requested)
        outgoing_msg     = compose_oadrDistributeEvent_msg(events_created)
        return outgoing_msg

    # incoming : oadrResponse : vtn -> ven (for oadrCreatedEvent)
    #                           vtn <- ven (for oadrDistributeEvent)
    # outgoing : ??
    elif incoming_msg == sysCfg.OADR_EIEVENT.oadrResponse:
        response = read_oadrResponse_msg(request_h)
        process_oadrResponse_msg(response)
        return None

    else:
        raise UnknownEiEventMessage
        return None
        


