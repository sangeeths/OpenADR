import logging
import json
import os
from threading import Lock as Lock 

from openadr.util import *
from openadr.exception import UnknownEiEventMessage
from openadr.services.EiEvent import EiEvent
from openadr.services.EiEvent.EiEventMessages import *


# global variable for frequent reference
service = sysCfg.OADR_SERVICE.EiEvent

         
def Load_EiEventStore(event_store_lock, 
                      filename=sysCfg.EIEVENT_STORE):
    event_store_lock.acquire()
    try:
        event_store = {}
        logging.info('Loading EiEvents..')
        if not os.path.exists(filename):
            logging.debug('EiEvent Information not present in %s' % filename)
            event_dict = {}
        else:
            with open(filename, 'r') as file_h:
                event_dict = json.load(file_h)
        # key = EventId
        # value = object of type EiEvent()
        for k, v in event_dict.iteritems():
            event_store[k] = EiEvent(**v)
        logging.debug('Loaded %d EiEvent(s) from %s' % \
                     (len(event_store), filename))
    except Exception, e:
        print e
    finally:
        event_store_lock.release()
    return event_store



def Save_EiEventStore(event_store, 
                      event_store_lock, 
                      filename=sysCfg.EIEVENT_STORE):
    event_store_lock.acquire()
    try:
        logging.info('Saving EiEvents..')
        event_dict = {}
        # key = eventId
        # value = dict(object of type EiEvent())
        for k, v in event_store.iteritems():
            event_dict[k] = v.getDict()
        with open(filename, 'w') as file_h:
            json.dump(event_dict, file_h)
        logging.debug('Saved %d EiEvent(s) to %s' % \
                     (len(event_dict), filename))
    except Exception, e:
        print e
    finally:
        event_store_lock.release()
    return None



class EiEventManager:
    __event_store_lock = Lock()
    __event_store = Load_EiEventStore(__event_store_lock)
    
    def __init__(self): 
        print "EiEventManager:: __init__()"
        #self.__load_from_pickle_db()
        
    def getEiEvents(self):
        print "EiEventManager:: getEiEvents()"
        return EiEventManager.__event_store.values()

    def addEiEvent(self, eiEvent):
        print "EiEventManager:: addEiEvent() :: enter"
        EiEventManager.__event_store_lock.acquire()
        EiEventManager.__event_store[eiEvent.eventDescriptor.eventID] = eiEvent
        EiEventManager.__event_store_lock.release()
        Save_EiEventStore(EiEventManager.__event_store, EiEventManager.__event_store_lock)
        print "EiEventManager:: addEiEvent() :: done"
 
    def process_oadrDistributeEvent_msg(self, **kwargs):
        print 'process_oadrDistributeEvent_msg'
        for event in kwargs['EiEvents']:
            self.addEiEvent(event)   

        print 'process_oadrDistributeEvent_msg'




       

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
        


