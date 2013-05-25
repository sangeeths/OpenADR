from lxml import etree

from openadr.util import *
from openadr.services import elements as en     # en = element name


# OADR_EIEVENT.oadrDistributeEvent
# OADR_EIEVENT.oadrResponse

class EiEvent:
    _xml_prefix = '<?xml version="1.0" encoding="UTF-8"?>\n'

    def __init__(self, xml_h=None):
        print 'EiEvent.__init__()'
        self.register_schema_ns()

    def configure(self):
        print 'EiEvent.configure()'

    def response(self):
        print 'EiEvent.response()'

    def poll(self):
        print 'EiEvent.poll()'

    def register_schema_ns(self):
        print "EiEvent.register_schema_ns"
        ns = get_schema_ns()
        for key, value in ns.iteritems():
            etree.register_namespace(key, value)
        
    # def compose_oadrRequestEvent_msg(self, requestID, venID, replyLimit):
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
        # root element
        e_oadrDistributeEvent = etree.Element(en.oadrDistributeEvent)

        # eiResponse element and its sub elements with values
        e_eiResponse = etree.SubElement(e_oadrDistributeEvent, en.eiResponse)
        etree.SubElement(e_eiResponse, en.responseCode).text = 'ei:responseCode'
        etree.SubElement(e_eiResponse, en.responseDescription).text = 'ei:responseDescription'
        etree.SubElement(e_eiResponse, en.requestID).text = 'pyld:requestID'
    
        # requestID and vtnID elements and its values
        etree.SubElement(e_oadrDistributeEvent, en.requestID).text = 'pyld:requestID'
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
        # root element
        e_oadrCreatedEvent = etree.Element(en.oadrCreatedEvent)

        # sub elements of oadrCreatedEvent (root)
        e_eiCreatedEvent = etree.SubElement(e_oadrCreatedEvent, en.eiCreatedEvent)

        # eiResponse element and its sub element with values
        e_eiResponse               = etree.SubElement(e_eiCreatedEvent, en.eiResponse)
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



