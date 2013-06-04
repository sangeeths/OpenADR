from lxml import etree

from openadr.util import *
from openadr.services.EiEvent import elements as en     # en = element name
from openadr.services.EiEvent import config as EiEventCfg

class EiEvent:
    __elements = ('eventDescriptor', 'eiActivePeriod', 'eiEventSignals', 'eiTarget')

    class eventDescriptor:
        __elements = ('eventID', 'modificationNumber', 'priority', \
                      'eiMarketContext', 'createdDateTime', 'eventStatus', \
                      'testEvent', 'vtnComment')
        def __init__(self, **kwargs):
            missing_elements = elements_exist(EiEvent.eventDescriptor.__elements, 
                                              kwargs.keys()) 
            if missing_elements:
                print missing_elements, " are expected but missing" 
                return None
            for k, v in kwargs.iteritems():
                setattr(self, k, v)
        def __str__(self):
            ed  = '%s:\n'                       % self.__class__.__name__
            ed += '\teventID            = %s\n' % self.eventID 
            ed += '\tmodificationNumber = %s\n' % self.modificationNumber
            ed += '\tpriority           = %s\n' % self.priority
            ed += '\teiMarketContext    = %s\n' % self.eiMarketContext
            ed += '\tcreatedDateTime    = %s\n' % self.createdDateTime
            ed += '\teventStatus        = %s\n' % self.eventStatus
            ed += '\ttestEvent          = %s\n' % self.testEvent
            ed += '\tvtnComment         = %s\n' % self.vtnComment
            return ed
 
    class eiActivePeriod:
        __elements = ('dtstart', 'duration', 'tolerance', 'x_eiNotification', \
                      'x_eiRampUp', 'x_eiRecovery', 'components')
        def __init__(self, **kwargs):
            missing_elements = elements_exist(EiEvent.eiActivePeriod.__elements, 
                                              kwargs.keys()) 
            if missing_elements:
                print missing_elements, " are expected but missing" 
                return None
            for k, v in kwargs.iteritems():
                setattr(self, k, v)
        def __str__(self):
            ap  = '%s:\n'                       % self.__class__.__name__
            ap += '\tproperties\n'
            ap += '\t\tdtstart          = %s\n' % self.dtstart
            ap += '\t\tduration         = %s\n' % self.duration
            ap += '\t\ttolerance        = %s\n' % self.tolerance
            ap += '\t\tx-eiNotification = %s\n' % self.x_eiNotification
            ap += '\t\tx-eiRampUp       = %s\n' % self.x_eiRampUp
            ap += '\t\tx-eiRecovery     = %s\n' % self.x_eiRecovery
            ap += '\tcomponents = %s\n' % self.components
            return ap

    class eiEventSignals:
        __elements = ('signalName', 'signalType', 'signalID', 'currentValue', 'intervals')
        class intervals:
            __elements = ('duration', 'uid', 'signalPayload')
            def __init__(self, **kwargs):
                missing_elements = elements_exist(EiEvent.eiEventSignals.intervals.__elements, 
                                                  kwargs.keys()) 
                if missing_elements:
                    print missing_elements, " are expected but missing" 
                    return None
                for k, v in kwargs.iteritems():
                    setattr(self, k, v)
            def __str__(self):
                intvl  = '\t\tinterval:\n'
                intvl += '\t\t\tduration      = %s\n' % self.duration
                intvl += '\t\t\tuid           = %s\n' % self.uid
                intvl += '\t\t\tsignalPayload = %s\n' % self.signalPayload
                return intvl
                
        def __init__(self, **kwargs):
            missing_elements = elements_exist(EiEvent.eiEventSignals.__elements, 
                                              kwargs.keys()) 
            if missing_elements:
                print missing_elements, " are expected but missing" 
                return None
            for k, v in kwargs.iteritems():
                if k != 'intervals':
                    setattr(self, k, v)
            self.intervals = []
            for interval in kwargs['intervals']:
                intvl = EiEvent.eiEventSignals.intervals(**interval)
                self.intervals.append(intvl) 
        def __str__(self):
            es  = '\teiEventSignal:\n'
            es += '\t\tsignalName   = %s\n' % self.signalName
            es += '\t\tsignalType   = %s\n' % self.signalType
            es += '\t\tsignalID     = %s\n' % self.signalID
            es += '\t\tcurrentValue = %s\n' % self.currentValue
            for interval in self.intervals:
                es += str(interval)
            return es

    class eiTarget:
        __elements = ('groupID', 'resourceID', 'venID', 'partyID')
        def __init__(self, **kwargs):
            missing_elements = elements_exist(EiEvent.eiTarget.__elements, 
                                              kwargs.keys()) 
            if missing_elements:
                print missing_elements, " are expected but missing" 
                return None
            for k, v in kwargs.iteritems():
                setattr(self, k, v)
        def __str__(self):
            tgt  = '%s:\n'               % self.__class__.__name__
            tgt += '\tgroupID    = %s\n' % self.groupID
            tgt += '\tresourceID = %s\n' % self.resourceID
            tgt += '\tvenID      = %s\n' % self.venID
            tgt += '\tpartyID    = %s\n' % self.partyID
            return tgt


    def __init__(self, **kwargs):
        missing_elements = elements_exist(EiEvent.__elements, kwargs.keys()) 
        if missing_elements:
            print missing_elements, " are expected but missing" 
            return None

        self._eventDescriptor = EiEvent.eventDescriptor(**kwargs['eventDescriptor'])
        self._eiActivePeriod  = EiEvent.eiActivePeriod(**kwargs['eiActivePeriod'])
        self._eiEventSignals  = []
        for eventSignal in kwargs['eiEventSignals']:
            es = EiEvent.eiEventSignals(**eventSignal)
            self._eiEventSignals.append(es)
        self._eiTarget = EiEvent.eiTarget(**kwargs['eiTarget'])

    def __str__(self):
        event_str  = "EiEvent:\n"
        event_str += "--------\n"
        event_str += str(self._eventDescriptor)
        event_str += str(self._eiActivePeriod)
        event_str += 'eiEventSignals:\n'
        for eventSignal in self._eiEventSignals:
            event_str += str(eventSignal)
        event_str += str(self._eiTarget)
        return event_str
