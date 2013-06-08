
from lxml import etree 

from openadr.util import *

from openadr.services.EiEvent import elements as en     # en = element name
from openadr.services.EiEvent.EiEvent import EiEvent 

from openadr.services.EiEvent.xpath import *


def register_schema_ns():
    ns = get_schema_ns()
    for key, value in ns.iteritems():
        etree.register_namespace(key, value)

#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#

def read_oadrRequestEvent_msg(req_h):
    print 'read_oadrRequestEvent_msg'

    xml_rns = get_ns(req_h, reverse=True)   # dict{url:ns}
    xml_ns  = get_ns(req_h)                 # dict{ns:url}

    xp = get_oadrRequestEvent_xpath(xml_rns)

    oadrRE = {
    'requestID'  : req_h.xpath(xp['requestID'],  namespaces=xml_ns)[0].text,
    'venID'      : req_h.xpath(xp['venID'],      namespaces=xml_ns)[0].text,
    'replyLimit' : req_h.xpath(xp['replyLimit'], namespaces=xml_ns)[0].text
    }
    
    print oadrRE
    return oadrRE


def process_oadrRequestEvent_msg(events_requested):
    print 'process_oadrRequestEvent_msg'

def compose_oadrRequestEvent_msg(self):
#    
# <oadr:oadrRequestEvent> 
#     <pyld:eiRequestEvent>
#         <pyld:requestID>pyld:requestID</pyld:requestID>
#         <ei:venID>ei:venID</ei:venID>
#         <pyld:replyLimit>0</pyld:replyLimit>
#     </pyld:eiRequestEvent>
# </oadr:oadrRequestEvent>
#
    register_schema_ns()

    e_oadrRequestEvent = etree.Element(en.oadrRequestEvent)
    e_eiRequestEvent   = etree.SubElement(e_oadrRequestEvent, en.eiRequestEvent)
    etree.SubElement(e_eiRequestEvent, en.requestID).text  = 'rioVEN-request-1'
    etree.SubElement(e_eiRequestEvent, en.venID).text      = 'rioVEN-1'
    etree.SubElement(e_eiRequestEvent, en.replyLimit).text = '0'
    
    # convert the xml msg to string
    oadrRequestEventMsg = etree.tostring(e_oadrRequestEvent, 
                                         pretty_print=True, 
                                         xml_declaration=True, 
                                         encoding='UTF-8')
    return oadrRequestEventMsg

#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#


def read_oadrDistributeEvent_msg(req_h):
    print 'read_oadrDistributeEvent_msg'

    xml_rns = get_ns(req_h, reverse=True)   # dict{url:ns}
    xml_ns  = get_ns(req_h)                 # dict{ns:url}

    xp = get_oadrDistributeEvent_xpath(xml_rns)

    # return dictionary which contains the following info:
    #   1. eiResponse
    #   2. requestID
    #   3. vtnID
    #   4. EiEvents -> list of EiEvent()'s
    #   5. RespReqd -> list of event ids
    oadrDE = {}

    oadrDE['eiResponse'] = {
    'responseCode'        : req_h.xpath(xp['responseCode'],        namespaces=xml_ns)[0].text,
    'responseDescription' : req_h.xpath(xp['responseDescription'], namespaces=xml_ns)[0].text,
    'requestID'           : req_h.xpath(xp['requestID'],           namespaces=xml_ns)[0].text
    }

    oadrDE['requestID'] = req_h.xpath(xp['oadr_requestID'], namespaces=xml_ns)[0].text
    oadrDE['vtnID']     = req_h.xpath(xp['vtnID'],          namespaces=xml_ns)[0].text

    ResponseRequired = {}
    newEvents = []

    oadrEvents = req_h.xpath(xp['oadrEvent'], namespaces=xml_ns)
    for oadrEvent in oadrEvents:
        eiEvent = {}
        # eventDescriptor
        eiEvent['eventDescriptor'] = {
        'eventID'            : oadrEvent.xpath(xp['eventID'],            namespaces=xml_ns)[0].text,
        'modificationNumber' : oadrEvent.xpath(xp['modificationNumber'], namespaces=xml_ns)[0].text,
        'priority'           : oadrEvent.xpath(xp['priority'],           namespaces=xml_ns)[0].text,
        'eiMarketContext'    : oadrEvent.xpath(xp['eiMarketContext'],    namespaces=xml_ns)[0].text,
        'createdDateTime'    : oadrEvent.xpath(xp['createdDateTime'],    namespaces=xml_ns)[0].text,
        'eventStatus'        : oadrEvent.xpath(xp['eventStatus'],        namespaces=xml_ns)[0].text,
        'testEvent'          : oadrEvent.xpath(xp['testEvent'],          namespaces=xml_ns)[0].text,
        'vtnComment'         : oadrEvent.xpath(xp['vtnComment'],         namespaces=xml_ns)[0].text
        }
        # eiActivePeriod
        eiEvent['eiActivePeriod'] = {
        'dtstart'          : oadrEvent.xpath(xp['dtstart'],          namespaces=xml_ns)[0].text,
        'duration'         : oadrEvent.xpath(xp['duration'],         namespaces=xml_ns)[0].text,
        'tolerance'        : oadrEvent.xpath(xp['tolerance'],        namespaces=xml_ns)[0].text,
        'x_eiNotification' : oadrEvent.xpath(xp['x_eiNotification'], namespaces=xml_ns)[0].text,
        'x_eiRampUp'       : oadrEvent.xpath(xp['x_eiRampUp'],       namespaces=xml_ns)[0].text,
        'x_eiRecovery'     : oadrEvent.xpath(xp['x_eiRecovery'],     namespaces=xml_ns)[0].text,
        'components'       : oadrEvent.xpath(xp['components'],       namespaces=xml_ns)[0].text
        }
        # eiEventSignals
        eiEventSignals = []
        eiEventSignals_e = oadrEvent.xpath(xp['eiEventSignal'], namespaces=xml_ns)
        for eiEventSignal in eiEventSignals_e:
            eventSignal = {
            'signalName'   : eiEventSignal.xpath(xp['signalName'],   namespaces=xml_ns)[0].text,
            'signalType'   : eiEventSignal.xpath(xp['signalType'],   namespaces=xml_ns)[0].text,
            'signalID'     : eiEventSignal.xpath(xp['signalID'],     namespaces=xml_ns)[0].text,
            'currentValue' : eiEventSignal.xpath(xp['currentValue'], namespaces=xml_ns)[0].text
            }
            # intervals
            intervals = []
            intervals_e = eiEventSignal.xpath(xp['interval'], namespaces=xml_ns) 
            for interval in intervals_e:
                interval_d = {
                'duration'      : interval.xpath(xp['i_duration'], namespaces=xml_ns)[0].text,
                'uid'           : interval.xpath(xp['i_uid'],      namespaces=xml_ns)[0].text,
                'signalPayload' : interval.xpath(xp['i_payload'],  namespaces=xml_ns)[0].text
                }
                intervals.append(interval_d)
            eventSignal['intervals'] = intervals
            eiEventSignals.append(eventSignal)
        eiEvent['eiEventSignals'] = eiEventSignals
        # eiTarget
        eiEvent['eiTarget'] = {
        'groupID'    : oadrEvent.xpath(xp['groupID'],    namespaces=xml_ns)[0].text,
        'resourceID' : oadrEvent.xpath(xp['resourceID'], namespaces=xml_ns)[0].text,
        'venID'      : oadrEvent.xpath(xp['venID'],      namespaces=xml_ns)[0].text,
        'partyID'    : oadrEvent.xpath(xp['partyID'],    namespaces=xml_ns)[0].text
        }

        newEvents.append(EiEvent(**eiEvent))
        
        # check oadrResponseRequired for the current event
        ResponseReq = oadrEvent.xpath(xp['ResponseRequired'], namespaces=xml_ns)[0].text
        ResponseRequired[eiEvent['eventDescriptor']['eventID']] = ResponseReq

    oadrDE['RespReqd'] = ResponseRequired
    oadrDE['EiEvents'] = newEvents

    print oadrDE
    return oadrDE



#def process_oadrDistributeEvent_msg(**kwargs):
#    em = EiEventManager()
#    print 'process_oadrDistributeEvent_msg'
#    for k, v in kwargs.iteritems():
#        print "key   = ", k
#        print "value = ", v
#    for event in kwargs['EiEvents']:
#        print "Adding the following EiEvent"
#        print str(event)
#        em.addEiEvent(event)
        


def compose_oadrDistributeEvent_msg(self):
#
# <oadr:oadrDistributeEvent> 
#     <ei:eiResponse>
#         <ei:responseCode>111</ei:responseCode>
#         <ei:responseDescription>ei:responseDescription</ei:responseDescription>
#         <pyld:requestID>pyld:requestID</pyld:requestID>
#     </ei:eiResponse>
#     <pyld:requestID>pyld:requestID</pyld:requestID>
#     <ei:vtnID>ei:vtnID</ei:vtnID>
#     <oadr:oadrEvent>
#         <ei:eiEvent>
#             <ei:eventDescriptor>
#                 <ei:eventID>ei:eventID</ei:eventID>
#                 <ei:modificationNumber>0</ei:modificationNumber>
#                 <ei:priority>0</ei:priority>
#                 <ei:eiMarketContext>
#                     <emix:marketContext>http://tempuri.org</emix:marketContext>
#                 </ei:eiMarketContext>
#                 <ei:createdDateTime>2001-12-31T12:00:00</ei:createdDateTime>
#                 <ei:eventStatus>none</ei:eventStatus>
#                 <ei:testEvent>ei:testEvent</ei:testEvent>
#                 <ei:vtnComment>ei:vtnComment</ei:vtnComment>
#             </ei:eventDescriptor>
#             <ei:eiActivePeriod>
#                 <xcal:properties>
#                     <xcal:dtstart>
#                         <xcal:date-time>2001-12-31T12:00:00</xcal:date-time>
#                     </xcal:dtstart>
#                     <xcal:duration>
#                         <xcal:duration>PT1H</xcal:duration>
#                     </xcal:duration>
#                     <xcal:tolerance>
#                         <xcal:tolerate>
#                             <xcal:startafter>PT2H</xcal:startafter>
#                         </xcal:tolerate>
#                     </xcal:tolerance>
#                     <ei:x-eiNotification>
#                         <xcal:duration>PT3H</xcal:duration>
#                     </ei:x-eiNotification>
#                     <ei:x-eiRampUp>
#                         <xcal:duration>PT5H</xcal:duration>
#                     </ei:x-eiRampUp>
#                     <ei:x-eiRecovery>
#                         <xcal:duration>PT10H</xcal:duration>
#                     </ei:x-eiRecovery>
#                 </xcal:properties>
#                 <xcal:components/>
#             </ei:eiActivePeriod>
#             <ei:eiEventSignals>
#                 <ei:eiEventSignal>
#                     <strm:intervals>
#                         <ei:interval>
#                             <xcal:duration>
#                                 <xcal:duration>PT12H</xcal:duration>
#                             </xcal:duration>
#                             <xcal:uid>
#                                 <xcal:text>xcal:text</xcal:text>
#                             </xcal:uid>
#                             <ei:signalPayload>
#                                 <ei:payloadFloat>
#                                     <ei:value>0.0</ei:value>
#                                 </ei:payloadFloat>
#                             </ei:signalPayload>
#                         </ei:interval>
#                     </strm:intervals>
#                     <ei:signalName>ei:signalName</ei:signalName>
#                     <ei:signalType>delta</ei:signalType>
#                     <ei:signalID>ei:signalID</ei:signalID>
#                     <ei:currentValue>
#                         <ei:payloadFloat>
#                             <ei:value>0.0</ei:value>
#                         </ei:payloadFloat>
#                     </ei:currentValue>
#                 </ei:eiEventSignal>
#             </ei:eiEventSignals>
#             <ei:eiTarget>
#                 <ei:groupID>ei:groupID</ei:groupID>
#                 <ei:resourceID>ei:resourceID</ei:resourceID>
#                 <ei:venID>ei:venID</ei:venID>
#                 <ei:partyID>ei:partyID</ei:partyID>
#             </ei:eiTarget>
#         </ei:eiEvent>
#         <oadr:oadrResponseRequired>always</oadr:oadrResponseRequired>
#     </oadr:oadrEvent>
# </oadr:oadrDistributeEvent>
#
    register_schema_ns()

    # root element
    e_oadrDistributeEvent = etree.Element(en.oadrDistributeEvent)

    # eiResponse element and its sub elements with values
    e_eiResponse = etree.SubElement(e_oadrDistributeEvent, en.eiResponse)
    etree.SubElement(e_eiResponse, en.responseCode).text = 'ei:responseCode'
    etree.SubElement(e_eiResponse, en.responseDescription).text = 'ei:responseDescription'
    etree.SubElement(e_eiResponse, en.requestID).text = 'pyld:requestID'

    # requestID and vtnID elements and its values
    e_requestID = etree.SubElement(e_oadrDistributeEvent, en.requestID)
    e_requestID.text = 'pyld:requestID'
    etree.SubElement(e_oadrDistributeEvent, en.vtnID).text = 'ei:vtnID'

    # oadrEvent element and its sub elements with values
    events = [1]
    for event in events:
        e_oadrEvent = etree.SubElement(e_oadrDistributeEvent, en.oadrEvent)
    

        # eiEvent and its sub elements with values
        e_eiEvent = etree.SubElement(e_oadrEvent, en.eiEvent)
        e_eventDescriptor = etree.SubElement(e_eiEvent, en.eventDescriptor)

        # eventDescriptor and its sub elements with values
        etree.SubElement(e_eventDescriptor, en.eventID).text = 'ei:eventID'
        etree.SubElement(e_eventDescriptor, en.modificationNumber).text = '0'
        etree.SubElement(e_eventDescriptor, en.priority).text = '0'
        e_eiMarketContext = etree.SubElement(e_eventDescriptor, en.eiMarketContext)
        etree.SubElement(e_eiMarketContext, en.marketContext).text = 'http://tempuri.org'
        etree.SubElement(e_eventDescriptor, en.createdDateTime).text = '2001-12-31T12:00:00'
        etree.SubElement(e_eventDescriptor, en.eventStatus).text = 'none'
        etree.SubElement(e_eventDescriptor, en.testEvent).text = 'ei:testEvent'
        etree.SubElement(e_eventDescriptor, en.vtnComment).text = 'ei:vtnComment'

        # eiActivePeriod and its sub elements with values
        e_eiActivePeriod = etree.SubElement(e_eiEvent, en.eiActivePeriod)
        e_properties = etree.SubElement(e_eiActivePeriod, en.properties)
        #   dtstart date and time
        e_dtstart = etree.SubElement(e_properties, en.dtstart)
        etree.SubElement(e_dtstart, en.date_time).text = '2001-12-31T12:00:00'
        #   duration
        e_duration = etree.SubElement(e_properties, en.duration)
        etree.SubElement(e_duration, en.duration).text = 'PT1H'
        #   tolerance
        e_tolerance = etree.SubElement(e_properties, en.tolerance)
        e_tolerate = etree.SubElement(e_tolerance, en.tolerate)
        etree.SubElement(e_tolerate, en.startafter).text = 'PT2H'
        #   notification
        e_x_eiNotification = etree.SubElement(e_properties, en.x_eiNotification)
        etree.SubElement(e_x_eiNotification, en.duration).text = 'PT3H'
        #   rampup
        e_x_eiRampUp = etree.SubElement(e_properties, en.x_eiRampUp)
        etree.SubElement(e_x_eiRampUp, en.duration).text = 'PT4H'
        #   recovery
        e_x_eiRecovery = etree.SubElement(e_properties, en.x_eiRecovery)
        etree.SubElement(e_x_eiRecovery, en.duration).text = 'PT5H'
        #   components
        etree.SubElement(e_eiActivePeriod, en.components)

        # eiEventSignals and its sub elements with values
        e_eiEventSignals = etree.SubElement(e_eiEvent, en.eiEventSignals)
        e_eiEventSignal = etree.SubElement(e_eiEventSignals, en.eiEventSignal)
        e_intervals = etree.SubElement(e_eiEventSignal, en.intervals)
        e_interval = etree.SubElement(e_intervals, en.interval)
        e_duration = etree.SubElement(e_interval, en.duration)
        etree.SubElement(e_duration, en.duration).text = 'PT1H'
        e_uid = etree.SubElement(e_interval, en.uid)
        etree.SubElement(e_uid, en.text).text = 'xcal:text'
        e_signalPayload = etree.SubElement(e_interval, en.signalPayload)
        e_payloadFloat = etree.SubElement(e_signalPayload, en.payloadFloat)
        etree.SubElement(e_payloadFloat, en.value).text = '0.0'

        etree.SubElement(e_eiEventSignal, en.signalName).text = 'ei:signalName'
        etree.SubElement(e_eiEventSignal, en.signalType).text = 'delta'
        etree.SubElement(e_eiEventSignal, en.signalID).text = 'ei:signalID'

        e_currentValue = etree.SubElement(e_eiEventSignal, en.currentValue)
        e_payloadFloat = etree.SubElement(e_currentValue, en.payloadFloat)
        etree.SubElement(e_payloadFloat, en.value).text = '0.0'

        # eiTarget and its sub elements with values
        e_eiTarget = etree.SubElement(e_eiEvent, en.eiTarget)
        etree.SubElement(e_eiTarget, en.groupID).text = 'ei:groupID'
        etree.SubElement(e_eiTarget, en.resourceID).text = 'ei:resourceID'
        etree.SubElement(e_eiTarget, en.venID).text = 'ei:venID'
        etree.SubElement(e_eiTarget, en.partyID).text = 'ei:partyID'
        
        # oadrResponseRequired element and its value
        etree.SubElement(e_oadrEvent, en.oadrResponseRequired).text = 'always'

    oadrDistributeEventMsg = etree.tostring(e_oadrDistributeEvent, 
                                            pretty_print=True, 
                                            xml_declaration=True, 
                                            encoding='UTF-8')
    return oadrDistributeEventMsg

#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#

def read_oadrCreatedEvent_msg(req_h):
    print 'read_oadrCreatedEvent_msg'
    xml_rns = get_ns(req_h, reverse=True)   # dict{url:ns}
    xml_ns  = get_ns(req_h)                 # dict{ns:url}

    xp = get_oadrCreatedEvent_xpath(xml_rns)

    oadrCE = {}

    # eiResponse
    # NOTE: there will be only one eiResponse element in 
    #       oadrCreatedEvent. So we can do eiResponse_e[0]
    #       without any issues.
    eiResponse_e = req_h.xpath(xp['eiResponse'], namespaces=xml_ns)
    oadrCE['eiResponse'] = {
    'responseCode'        : eiResponse_e[0].xpath(xp['responseCode'],        namespaces=xml_ns)[0].text,
    'responseDescription' : eiResponse_e[0].xpath(xp['responseDescription'], namespaces=xml_ns)[0].text,
    'requestID'           : eiResponse_e[0].xpath(xp['requestID'],           namespaces=xml_ns)[0].text
    }

    # venID
    oadrCE['venID'] = req_h.xpath(xp['venID'], namespaces=xml_ns)[0].text

    # eventResponses
    eventResponses = []
    eventResponse_e = req_h.xpath(xp['eventResponse'], namespaces=xml_ns)
    for er in eventResponse_e:
        er_d = {
        'responseCode'        : er.xpath(xp['responseCode'],        namespaces=xml_ns)[0].text,
        'responseDescription' : er.xpath(xp['responseDescription'], namespaces=xml_ns)[0].text,
        'requestID'           : er.xpath(xp['requestID'],           namespaces=xml_ns)[0].text,
        'eventID'             : er.xpath(xp['eventID'],             namespaces=xml_ns)[0].text,
        'modificationNumber'  : er.xpath(xp['modificationNumber'],  namespaces=xml_ns)[0].text,
        'optType'             : er.xpath(xp['optType'],             namespaces=xml_ns)[0].text
        }
        eventResponses.append(er_d)
    oadrCE['eventResponses'] = eventResponses

    print oadrCE
    return oadrCE


def process_oadrCreatedEvent_msg(events_created):
    print 'process_oadrCreatedEvent_msg'

def compose_oadrCreatedEvent_msg(self):
#
# <oadr:oadrCreatedEvent>
#     <pyld:eiCreatedEvent>
#         <ei:eiResponse>
#             <ei:responseCode>ei:responseCode</ei:responseCode>
#             <ei:responseDescription>ei:responseDescription</ei:responseDescription>
#             <pyld:requestID>pyld:requestID</pyld:requestID>
#         </ei:eiResponse>
#         <ei:eventResponses>
#             <ei:eventResponse>
#                 <ei:responseCode>ei:responseCode</ei:responseCode>
#                 <ei:responseDescription>ei:responseDescription</ei:responseDescription>
#                 <pyld:requestID>pyld:requestID</pyld:requestID>
#                 <ei:qualifiedEventID>
#                     <ei:eventID>ei:eventID</ei:eventID>
#                     <ei:modificationNumber>0</ei:modificationNumber>
#                 </ei:qualifiedEventID>
#                 <ei:optType>optIn</ei:optType>
#             </ei:eventResponse>
#         </ei:eventResponses>
#         <ei:venID>ei:venID</ei:venID>
#     </pyld:eiCreatedEvent>
# </oadr:oadrCreatedEvent>
#
    register_schema_ns()

    # root element
    e_oadrCreatedEvent = etree.Element(en.oadrCreatedEvent)

    # sub elements of oadrCreatedEvent (root)
    e_eiCreatedEvent = etree.SubElement(e_oadrCreatedEvent, en.eiCreatedEvent)

    # eiResponse element and its sub element with values
    e_eiResponse = etree.SubElement(e_eiCreatedEvent, en.eiResponse)
    etree.SubElement(e_eiResponse, en.responseCode).text = 'ei:responseCode'
    etree.SubElement(e_eiResponse, en.responseDescription).text = 'ei:responseDescription'
    etree.SubElement(e_eiResponse, en.requestID).text = 'pyld:requestID'

    # eventResponses element and its sub elements with value
    #events = get_created_event()
    events = [14]
    if events:
        e_eventResponses = etree.SubElement(e_eiCreatedEvent, en.eventResponses)
        for event in events:
            e_eventResponse  = etree.SubElement(e_eventResponses, en.eventResponse)
            etree.SubElement(e_eventResponse, en.responseCode).text = 'ei:responseCode'
            etree.SubElement(e_eventResponse, en.responseDescription).text = 'ei:responseDescription'
            etree.SubElement(e_eventResponse, en.requestID).text = 'pyld:requestID'
            e_qualifiedEventID = etree.SubElement(e_eventResponse, en.qualifiedEventID)
            etree.SubElement(e_qualifiedEventID, en.eventID).text = 'ei:eventID'
            etree.SubElement(e_qualifiedEventID, en.modificationNumber).text = '0'
            etree.SubElement(e_eventResponse, en.optType).text = 'optIn'

    # venID element 
    e_venID      = etree.SubElement(e_eiCreatedEvent, en.venID)
    e_venID.text = 'ei:venID'

    oadrCreatedEventMsg = etree.tostring(e_oadrCreatedEvent, 
                                         pretty_print=True, 
                                         xml_declaration=True, 
                                         encoding='UTF-8')
    return oadrCreatedEventMsg
    
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#

def read_oadrResponse_msg(req_h):
    print 'read_oadrResponse_msg'
    xml_rns = get_ns(req_h, reverse=True)   # dict{url:ns}
    xml_ns  = get_ns(req_h)                 # dict{ns:url}

    xp = get_oadrResponse_xpath(xml_rns)

    oadrResponse = {
    'responseCode'        : req_h.xpath(xp['responseCode'],        namespaces=xml_ns)[0].text,
    'responseDescription' : req_h.xpath(xp['responseDescription'], namespaces=xml_ns)[0].text,
    'requestID'           : req_h.xpath(xp['requestID'],           namespaces=xml_ns)[0].text
    }

    print oadrResponse
    return oadrResponse
    

def process_oadrResponse_msg(response):
    print 'process_oadrResponse_msg'

def compose_oadrResponse_msg(self):
#
# <oadr:oadrResponse>
#     <ei:eiResponse>
#         <ei:responseCode>123</ei:responseCode>
#         <ei:responseDescription>ei:responseDescription</ei:responseDescription>
#         <pyld:requestID>pyld:requestID</pyld:requestID>
#     </ei:eiResponse>
# </oadr:oadrResponse>
#
    register_schema_ns()

    e_oadrResponse = etree.Element(en.oadrResponse)
    e_eiResponse = etree.SubElement(e_oadrResponse, en.eiResponse)
    etree.SubElement(e_eiResponse, en.responseCode).text = 'ei:responseCode'
    etree.SubElement(e_eiResponse, en.responseDescription).text = 'ei:responseDescription'
    etree.SubElement(e_eiResponse, en.requestID).text = 'pyld:requestID'

    oadrResponseMsg = etree.tostring(e_oadrResponse, 
                                     pretty_print=True, 
                                     xml_declaration=True, 
                                     encoding='UTF-8')
    return oadrResponseMsg

#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#

# __END__ 
