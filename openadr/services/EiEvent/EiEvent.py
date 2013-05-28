from lxml import etree

from openadr.util import *
from openadr.services.EiEvent import elements as en     # en = element name
from openadr.services.EiEvent import config as EiEventCfg


# <ei:eiEvent>
#     <ei:eventDescriptor>
#         <ei:eventID>ei:eventID</ei:eventID>
#         <ei:modificationNumber>0</ei:modificationNumber>
#         <ei:priority>0</ei:priority>
#         <ei:eiMarketContext>
#             <emix:marketContext>http://tempuri.org</emix:marketContext>
#         </ei:eiMarketContext>
#         <ei:createdDateTime>2001-12-31T12:00:00</ei:createdDateTime>
#         <ei:eventStatus>none</ei:eventStatus>
#         <ei:testEvent>ei:testEvent</ei:testEvent>
#         <ei:vtnComment>ei:vtnComment</ei:vtnComment>
#     </ei:eventDescriptor>
#     <ei:eiActivePeriod>
#         <xcal:properties>
#             <xcal:dtstart>
#                 <xcal:date-time>2001-12-31T12:00:00</xcal:date-time>
#             </xcal:dtstart>
#             <xcal:duration>
#                 <xcal:duration>PT1H</xcal:duration>
#             </xcal:duration>
#             <xcal:tolerance>
#                 <xcal:tolerate>
#                     <xcal:startafter>PT2H</xcal:startafter>
#                 </xcal:tolerate>
#             </xcal:tolerance>
#             <ei:x-eiNotification>
#                 <xcal:duration>PT3H</xcal:duration>
#             </ei:x-eiNotification>
#             <ei:x-eiRampUp>
#                 <xcal:duration>PT5H</xcal:duration>
#             </ei:x-eiRampUp>
#             <ei:x-eiRecovery>
#                 <xcal:duration>PT10H</xcal:duration>
#             </ei:x-eiRecovery>
#         </xcal:properties>
#         <xcal:components/>
#     </ei:eiActivePeriod>
#     <ei:eiEventSignals>
#         <ei:eiEventSignal>
#             <strm:intervals>
#                 <ei:interval>
#                     <xcal:duration>
#                         <xcal:duration>PT12H</xcal:duration>
#                     </xcal:duration>
#                     <xcal:uid>
#                         <xcal:text>xcal:text</xcal:text>
#                     </xcal:uid>
#                     <ei:signalPayload>
#                         <ei:payloadFloat>
#                             <ei:value>0.0</ei:value>
#                         </ei:payloadFloat>
#                     </ei:signalPayload>
#                 </ei:interval>
#             </strm:intervals>
#             <ei:signalName>ei:signalName</ei:signalName>
#             <ei:signalType>delta</ei:signalType>
#             <ei:signalID>ei:signalID</ei:signalID>
#             <ei:currentValue>
#                 <ei:payloadFloat>
#                     <ei:value>0.0</ei:value>
#                 </ei:payloadFloat>
#             </ei:currentValue>
#         </ei:eiEventSignal>
#     </ei:eiEventSignals>
#     <ei:eiTarget>
#         <ei:groupID>ei:groupID</ei:groupID>
#         <ei:resourceID>ei:resourceID</ei:resourceID>
#         <ei:venID>ei:venID</ei:venID>
#         <ei:partyID>ei:partyID</ei:partyID>
#     </ei:eiTarget>
# </ei:eiEvent>




class EiEvent:
    __eventDescriptor = ('eventID', 'modificationNumber', 'priority', \
                         'eiMarketContext', 'createdDateTime', 'eventStatus', \
                         'testEvent', 'vtnComment')
    __eiActivePeriod = ('properties', 'components')
    class eventDescriptor:
        def __init__(self, eventID, modificationNumber, priority, 
                     eiMarketContext, createdDateTime, eventStatus, 
                     testEvent, vtnComment):
            self.eventID = eventID
            self.modificationNumber = modificationNumber
            self.priority = priority
            self.eiMarketContext = eiMarketContext
            self.createdDateTime = createdDateTime
            self.eventStatus = eventStatus
            self.testEvent = testEvent
            self.vtnComment = vtnComment
        def __str__(self):
            return '%s(eventID=%s, modificationNumber=%d, priority=%d, \
                       eiMarketContext=%s, createdDateTime=%s, \
                       eventStatus=%s, testEvent=%s, vtnComment=%s)' % \
                    (self.__class__.__name__, self.eventID, self.modificationNumber, \
                    self.priority, self.eiMarketContext, self.createdDateTime, \
                    self.eventStatus.key, self.testEvent, self.vtnComment)
            

    class eiActivePeriod:
        def __init__(self, properties, components):
            self.properties = properties
            self.components = components


#     <ei:eiActivePeriod>
#         <xcal:properties>
#             <xcal:dtstart>
#                 <xcal:date-time>2001-12-31T12:00:00</xcal:date-time>
#             </xcal:dtstart>
#             <xcal:duration>
#                 <xcal:duration>PT1H</xcal:duration>
#             </xcal:duration>
#             <xcal:tolerance>
#                 <xcal:tolerate>
#                     <xcal:startafter>PT2H</xcal:startafter>
#                 </xcal:tolerate>
#             </xcal:tolerance>
#             <ei:x-eiNotification>
#                 <xcal:duration>PT3H</xcal:duration>
#             </ei:x-eiNotification>
#             <ei:x-eiRampUp>
#                 <xcal:duration>PT5H</xcal:duration>
#             </ei:x-eiRampUp>
#             <ei:x-eiRecovery>
#                 <xcal:duration>PT10H</xcal:duration>
#             </ei:x-eiRecovery>
#         </xcal:properties>
#         <xcal:components/>
#     </ei:eiActivePeriod>





    class eiEventSignals:
        def __init__(self):
            pass

    class eiTarget:
        def __init__(self):
            pass


    def __init__(self):
        pass



