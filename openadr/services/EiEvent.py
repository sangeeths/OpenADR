from lxml import etree

from openadr.util import *
from openadr.services import elements as en     # en = element name


# OADR_EIEVENT.oadrDistributeEvent
# OADR_EIEVENT.oadrResponse

class EiEvent:
    _xml_prefix = '<?xml version="1.0" encoding="UTF-8"?>\n'

    def __init__(self, xml_h=None):
        print 'EiEvent.__init__()'
        #self.register_schema_ns()

    def configure(self):
        print 'EiEvent.configure()'

    def response(self):
        print 'EiEvent.response()'

    def poll(self):
        print 'EiEvent.poll()'

#    def register_schema_ns(self):
#        print "EiEvent.register_schema_ns"
#        ns = get_schema_ns()
#        for key, value in ns.iteritems():
#            etree.register_namespace(key, value)
        
    # def compose_oadrRequestEvent_msg(self, requestID, venID, replyLimit):
    def compose_oadrRequestEvent_msg(self):
        
        e_oadrRequestEvent = etree.Element(en.oadrRequestEvent)
        e_eiRequestEvent   = etree.SubElement(e_oadrRequestEvent, en.eiRequestEvent)
        e_requestID        = etree.SubElement(e_eiRequestEvent, en.requestID)
        e_requestID.text   = 'rioVEN-request-1'
        e_venID            = etree.SubElement(e_eiRequestEvent, en.venID)
        e_venID.text       = 'rioVEN-1'
        e_replyLimit       = etree.SubElement(e_eiRequestEvent, en.replyLimit)
        e_replyLimit.text  = '0'
        
        # convert the xml msg to string
        oadrRequestEventMsg = etree.tostring(e_oadrRequestEvent, 
                                             pretty_print=True, 
                                             xml_declaration=True, 
                                             encoding='UTF-8')
        return oadrRequestEventMsg

    def compose_oadrDistributeEvent_msg(self):
        pass

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
        e_responseCode             = etree.SubElement(e_eiResponse, en.responseCode)
        e_responseCode.text        = 'ei:responseCode'
        e_responseDescription      = etree.SubElement(e_eiResponse, en.responseDescription)
        e_responseDescription.text = 'ei:responseDescription'
        e_requestID                = etree.SubElement(e_eiResponse, en.requestID)
        e_requestID.text           = 'pyld:requestID'

        # eventResponses element and its sub elements with value
        #events = get_created_event()
        events = [14]
        for event in events:
            e_eventResponses = etree.SubElement(e_eiCreatedEvent, en.eventResponses)
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
        pass

