from openadr.services.EiEvent import elements as en


class oadrNSP:
    def __init__(self, ns):
        self._ns = ns
        self._elements = {}
        self.configure()
    def configure(self):
        from openadr.services.EiEvent import elements as EiEventElement
        for k, v in vars(EiEventElement).iteritems():
            if not k.startswith('__'):
                url = v.strip('{').rsplit('}')[0]
                ele = v.strip('{').rsplit('}')[1]
                self._elements[v] = self._ns[url] + ':' + ele
    def getAllElements(self):
        return self._elements
    def printAllElements(self):
        for key, value in self._elements.iteritems():
            print "%s       : %s" % (key, value)



def get_oadrDistributeEvent_xpath(ns):
    oadr_nsp = oadrNSP(ns)
    oadr_nsp.printAllElements()
    nsp = oadr_nsp.getAllElements()
    
    xpath_d = {
    'responseCode' : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                    nsp[en.eiResponse], 
                                    nsp[en.responseCode]),
    'responseDescription' : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                           nsp[en.eiResponse], 
                                           nsp[en.responseDescription]),
    'requestID' : '/%s/%s/%s' % (nsp[en.oadrDistributeEvent], 
                                 nsp[en.eiResponse], 
                                 nsp[en.requestID]),
    'oadr_requestID' : '/%s/%s' % (nsp[en.oadrDistributeEvent], nsp[en.requestID]),
    'vtnID'          : '/%s/%s' % (nsp[en.oadrDistributeEvent], nsp[en.vtnID]),
    'oadrEvent'      : '/%s/%s' % (nsp[en.oadrDistributeEvent], nsp[en.oadrEvent]),
    'eventID' : '%s/%s/%s' % (nsp[en.eiEvent],
                              nsp[en.eventDescriptor], 
                              nsp[en.eventID]),
    'modificationNumber' : '%s/%s/%s' % (nsp[en.eiEvent], 
                                         nsp[en.eventDescriptor], 
                                         nsp[en.modificationNumber]),
    'priority' : '%s/%s/%s' % (nsp[en.eiEvent],
                               nsp[en.eventDescriptor], 
                               nsp[en.priority]),
    'marketContext' : '%s/%s/%s/%s' % (nsp[en.eiEvent],
                                       nsp[en.eventDescriptor],
                                       nsp[en.eiMarketContext],
                                       nsp[en.marketContext]),
    'createdDateTime' : '%s/%s/%s' % (nsp[en.eiEvent],
                                      nsp[en.eventDescriptor],
                                      nsp[en.createdDateTime]),
    'eventStatus' : '%s/%s/%s' % (nsp[en.eiEvent],
                                  nsp[en.eventDescriptor],
                                  nsp[en.eventStatus]),
    'testEvent' : '%s/%s/%s' % (nsp[en.eiEvent],
                                nsp[en.eventDescriptor],
                                nsp[en.testEvent]),
    'vtnComment' : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eventDescriptor],
                                 nsp[en.vtnComment]),
    'dtstart' : '%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                    nsp[en.eiActivePeriod],
                                    nsp[en.properties],
                                    nsp[en.dtstart],
                                    nsp[en.date_time]),
    'duration' : '%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                     nsp[en.eiActivePeriod],
                                     nsp[en.properties],
                                     nsp[en.duration],
                                     nsp[en.duration]),
    'tolerance' : '%s/%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                         nsp[en.eiActivePeriod],
                                         nsp[en.properties],
                                         nsp[en.tolerance],
                                         nsp[en.tolerate],
                                         nsp[en.startafter]),
    'x_eiNotification' : '%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                             nsp[en.eiActivePeriod],
                                             nsp[en.properties],
                                             nsp[en.x_eiNotification],
                                             nsp[en.duration]),
    'x_eiRampUp' : '%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                       nsp[en.eiActivePeriod],
                                       nsp[en.properties],
                                       nsp[en.x_eiRampUp],
                                       nsp[en.duration]),
    'x_eiRecovery' : '%s/%s/%s/%s/%s' % (nsp[en.eiEvent],
                                         nsp[en.eiActivePeriod],
                                         nsp[en.properties],
                                         nsp[en.x_eiRecovery],
                                         nsp[en.duration]),
    'components' : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiActivePeriod],
                                 nsp[en.components]),
    #eiEventSignal->oneormore
    'eiEventSignal' : '/%s/%s/%s/%s/%s' % (nsp[en.oadrDistributeEvent],
                                           nsp[en.oadrEvent],
                                           nsp[en.eiEvent],
                                           nsp[en.eiEventSignals],
                                           nsp[en.eiEventSignal]),
    'signalName' : '%s' % (nsp[en.signalName]),
    'signalType' : '%s' % (nsp[en.signalType]),
    'signalID'   : '%s' % (nsp[en.signalID]),
    'currentValue' : '%s/%s/%s' % (nsp[en.currentValue],
                                   nsp[en.payloadFloat],
                                   nsp[en.value]),
    #interval->oneormore
    'interval'          : '%s/%s' % (nsp[en.intervals], nsp[en.interval]),
    'i_duration' : '%s/%s' % (nsp[en.duration], nsp[en.duration]),
    'i_uid'      : '%s/%s' % (nsp[en.uid], nsp[en.text]),
    'i_payload'  : '%s/%s/%s' % (nsp[en.signalPayload],
                                 nsp[en.payloadFloat],
                                 nsp[en.value]),
    # eiTarget
    'groupID' : '%s/%s/%s' % (nsp[en.eiEvent],
                              nsp[en.eiTarget],
                              nsp[en.groupID]),
    'resourceID' : '%s/%s/%s' % (nsp[en.eiEvent],
                                 nsp[en.eiTarget],
                                 nsp[en.resourceID]),
    'venID' : '%s/%s/%s' % (nsp[en.eiEvent],
                            nsp[en.eiTarget],
                            nsp[en.venID]),
    'partyID' : '%s/%s/%s' % (nsp[en.eiEvent],
                              nsp[en.eiTarget],
                              nsp[en.partyID]),
    'ResponseRequired' : '%s' % (nsp[en.oadrResponseRequired])
    }
    
    print '========================================='
    print xpath_d
    print '========================================='
    return xpath_d


