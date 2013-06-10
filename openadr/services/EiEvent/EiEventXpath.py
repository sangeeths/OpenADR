from openadr.services.EiEvent import EiEventElements as en


class oadrNSP:
    def __init__(self, ns):
        self._ns = ns
        self._elements = {}
        self.configure()
    def configure(self):
        from openadr.services.EiEvent import EiEventElements 
        for k, v in vars(EiEventElements).iteritems():
            if not k.startswith('__'):
                url = v.strip('{').rsplit('}')[0]
                ele = v.strip('{').rsplit('}')[1]
                if url in self._ns.keys():
                    self._elements[v] = self._ns[url] + ':' + ele
    def getAllElements(self):
        return self._elements
    def printAllElements(self):
        for key, value in self._elements.iteritems():
            print "%s       : %s" % (key, value)



def get_oadrDistributeEvent_xpath(ns):
    nsp = oadrNSP(ns).getAllElements()   

    xpath_d = {
    # absolute path for eiResponse elements
    'responseCode'        : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                           nsp[en.eiResponse], 
                                           nsp[en.responseCode]),
    'responseDescription' : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                           nsp[en.eiResponse], 
                                           nsp[en.responseDescription]),
    'requestID'           : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                           nsp[en.eiResponse], 
                                           nsp[en.requestID]),

    # absolute path for requestID element
    'oadr_requestID' : '/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                   nsp[en.requestID]),

    # absolute path for vtnID element
    'vtnID' : '/%s/%s' % (nsp[en.oadrDistributeEvent], 
                          nsp[en.vtnID]),


    # absolute path for oadrEvent element -> one or more
    'oadrEvent' : '/%s/%s' % (nsp[en.oadrDistributeEvent], 
                              nsp[en.oadrEvent]),

    # relative paths to oadrEvent element
    # /oadrDistributeEvent/oadrEvent/eiEvent/eventDescriptor
    'eventID'            : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor], 
                                            nsp[en.eventID]),
    'modificationNumber' : '%s/%s/%s'    % (nsp[en.eiEvent], 
                                            nsp[en.eventDescriptor], 
                                            nsp[en.modificationNumber]),
    'priority'           : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor], 
                                            nsp[en.priority]),
    'eiMarketContext'    : '%s/%s/%s/%s' % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor],
                                            nsp[en.eiMarketContext],
                                            nsp[en.marketContext]),
    'createdDateTime'    : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor],
                                            nsp[en.createdDateTime]),
    'eventStatus'        : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor],
                                            nsp[en.eventStatus]),
    'testEvent'          : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor],
                                            nsp[en.testEvent]),
    'vtnComment'         : '%s/%s/%s'    % (nsp[en.eiEvent],
                                            nsp[en.eventDescriptor],
                                            nsp[en.vtnComment]),

    # relative paths to oadrEvent element
    # /oadrDistributeEvent/oadrEvent/eiEvent/eiActivePeriod
    'dtstart'          : '%s/%s/%s/%s/%s'    % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.dtstart],
                                                nsp[en.date_time]),
    'duration'         : '%s/%s/%s/%s/%s'    % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.duration],
                                                nsp[en.duration]),
    'tolerance'        : '%s/%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.tolerance],
                                                nsp[en.tolerate],
                                                nsp[en.startafter]),
    'x_eiNotification' : '%s/%s/%s/%s/%s'    % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.x_eiNotification],
                                                nsp[en.duration]),
    'x_eiRampUp'       : '%s/%s/%s/%s/%s'    % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.x_eiRampUp],
                                                nsp[en.duration]),
    'x_eiRecovery'     : '%s/%s/%s/%s/%s'    % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.properties],
                                                nsp[en.x_eiRecovery],
                                                nsp[en.duration]),
    'components'       : '%s/%s/%s'          % (nsp[en.eiEvent],
                                                nsp[en.eiActivePeriod],
                                                nsp[en.components]),

    # /oadrDistributeEvent/oadrEvent/eiEvent/eiEventSignals/eiEventSignal
    # NOTE: one or more instance of eiEventSignal element
    'eiEventSignal' : '/%s/%s/%s/%s/%s' % (nsp[en.oadrDistributeEvent],
                                           nsp[en.oadrEvent],
                                           nsp[en.eiEvent],
                                           nsp[en.eiEventSignals],
                                           nsp[en.eiEventSignal]),
    'signalName'   : '%s'       % (nsp[en.signalName]),
    'signalType'   : '%s'       % (nsp[en.signalType]),
    'signalID'     : '%s'       % (nsp[en.signalID]),
    'currentValue' : '%s/%s/%s' % (nsp[en.currentValue],
                                   nsp[en.payloadFloat],
                                   nsp[en.value]),

    # /oadrDistributeEvent/oadrEvent/eiEvent/eiEventSignals/eiEventSignal/intervals/interval
    # NOTE: one or more instance of interval element
    'interval'   : '%s/%s'    % (nsp[en.intervals], 
                                 nsp[en.interval]),
    'i_duration' : '%s/%s'    % (nsp[en.duration], 
                                 nsp[en.duration]),
    'i_uid'      : '%s/%s'    % (nsp[en.uid], 
                                 nsp[en.text]),
    'i_payload'  : '%s/%s/%s' % (nsp[en.signalPayload],
                                 nsp[en.payloadFloat],
                                 nsp[en.value]),

    # /oadrDistributeEvent/oadrEvent/eiEvent/eiTarget
    'groupID'    : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiTarget],
                                 nsp[en.groupID]),
    'resourceID' : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiTarget],
                                 nsp[en.resourceID]),
    'venID'      : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiTarget],
                                 nsp[en.venID]),
    'partyID'    : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiTarget],
                                 nsp[en.partyID]),

    # /oadrDistributeEvent/oadrEvent/ResponseRequired
    'ResponseRequired' : '%s' % (nsp[en.oadrResponseRequired])
    }
    
    return xpath_d



def get_oadrRequestEvent_xpath(ns):
    nsp = oadrNSP(ns).getAllElements()
    
    print "-----------------------"
    print nsp
    print "-----------------------"

    xpath_d = {
    # absolute path for eiResponse element
    'requestID'  : '/%s/%s/%s' % (nsp[en.oadrRequestEvent], 
                                  nsp[en.eiRequestEvent], 
                                  nsp[en.requestID]),
    'venID'      : '/%s/%s/%s' % (nsp[en.oadrRequestEvent], 
                                  nsp[en.eiRequestEvent], 
                                  nsp[en.venID]),
    'replyLimit' : '/%s/%s/%s' % (nsp[en.oadrRequestEvent], 
                                  nsp[en.eiRequestEvent], 
                                  nsp[en.replyLimit])
    }

    return xpath_d


def get_oadrCreatedEvent_xpath(ns):
    nsp = oadrNSP(ns).getAllElements()

    xpath_d = {
    # absolute path for eiResponse element
    'eiResponse' : '/%s/%s/%s' % (nsp[en.oadrCreatedEvent],
                                  nsp[en.eiCreatedEvent],
                                  nsp[en.eiResponse]),

    # absolute path for eventResponse elements
    'eventResponse' : '/%s/%s/%s/%s' % (nsp[en.oadrCreatedEvent], 
                                        nsp[en.eiCreatedEvent],
                                        nsp[en.eventResponses], 
                                        nsp[en.eventResponse]),

    # absolute path for venID element
    'venID' : '/%s/%s/%s' % (nsp[en.oadrCreatedEvent], 
                             nsp[en.eiCreatedEvent], 
                             nsp[en.venID]),

    # relative path for eiResponse 
    # and eventResponse elements
    'responseCode'        : '%s'    % (nsp[en.responseCode]),
    'responseDescription' : '%s'    % (nsp[en.responseDescription]),
    'requestID'           : '%s'    % (nsp[en.requestID]),
    'eventID'             : '%s/%s' % (nsp[en.qualifiedEventID], 
                                       nsp[en.eventID]),
    'modificationNumber'  : '%s/%s' % (nsp[en.qualifiedEventID], 
                                       nsp[en.modificationNumber]),
    'optType'             : '%s'    % (nsp[en.optType])

    }

    return xpath_d


def get_oadrResponse_xpath(ns):
    nsp = oadrNSP(ns).getAllElements()

    xpath_d = {
    # absolute path for eiResponse element
    'responseCode'        : '/%s/%s/%s' % (nsp[en.oadrResponse],
                                           nsp[en.eiResponse],
                                           nsp[en.responseCode]),
    'responseDescription' : '/%s/%s/%s' % (nsp[en.oadrResponse],
                                           nsp[en.eiResponse],
                                           nsp[en.responseDescription]),
    'requestID'           : '/%s/%s/%s' % (nsp[en.oadrResponse],
                                           nsp[en.eiResponse],
                                           nsp[en.requestID])
    }

    return xpath_d

