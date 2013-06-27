from openadr.validation import valid_incoming_elements

from openadr.services.EiEvent.EiEventValidation import *


class EiEvent:
    # mandatory elements for EiEvent
    __elements = ('eventDescriptor', 'eiActivePeriod', 'eiEventSignals', 'eiTarget')

    class eventDescriptor:
        # mandatory elements for EiEvent.eventDescriptor
        __elements = ('eventID', 'modificationNumber', 'priority', \
                      'eiMarketContext', 'createdDateTime', 'eventStatus', \
                      'testEvent', 'vtnComment')
        # EiEvent.eventDescriptor
        def __init__(self, **kwargs):
            # validate the incoming eventDescriptor elements
            valid_incoming_elements(EiEvent.eventDescriptor.__elements, kwargs.keys()) 
            if valid_eventId(kwargs['eventID']):
                self.eventID = kwargs['eventID']
            if valid_modificationNumber(kwargs['modificationNumber']):
                self.modificationNumber = kwargs['modificationNumber']
            if valid_priority(kwargs['priority']):
                self.priority = kwargs['priority']
            if valid_eiMarketContext(kwargs['eiMarketContext']):
                self.eiMarketContext = kwargs['eiMarketContext']
            if valid_createdDateTime(kwargs['createdDateTime']):
                self.createdDateTime = kwargs['createdDateTime']
            if valid_eventStatus(kwargs['eventStatus']):
                self.eventStatus = kwargs['eventStatus']
            if valid_testEvent(kwargs['testEvent']):
                self.testEvent = kwargs['testEvent']
            if valid_vtnComment(kwargs['vtnComment']):
                self.vtnComment = kwargs['vtnComment']
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
        def getDict(self):
            return self.__dict__

    class eiActivePeriod:
        # mandatory elements for EiEvent.eiActivePeriod
        __elements = ('dtstart', 'duration', 'tolerance', 'x_eiNotification', \
                      'x_eiRampUp', 'x_eiRecovery', 'components')
        # EiEvent.eiActivePeriod
        def __init__(self, **kwargs):
            # validate the incoming eventDescriptor elements
            valid_incoming_elements(EiEvent.eiActivePeriod.__elements, kwargs.keys()) 
            if valid_dtstart(kwargs['dtstart']):
                self.dtstart = kwargs['dtstart']
            if valid_duration(kwargs['duration']):
                self.duration = kwargs['duration']
            if valid_tolerance(kwargs['tolerance']):
                self.tolerance = kwargs['tolerance']
            if valid_x_eiNotification(kwargs['x_eiNotification']):
                self.x_eiNotification = kwargs['x_eiNotification']
            if valid_x_eiRampUp(kwargs['x_eiRampUp']):
                self.x_eiRampUp = kwargs['x_eiRampUp']
            if valid_x_eiRecovery(kwargs['x_eiRecovery']):
                self.x_eiRecovery = kwargs['x_eiRecovery']
            if valid_components(kwargs['components']):
                self.components = kwargs['components']
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
        def getDict(self):
            return self.__dict__

    class eiEventSignals:
        # mandatory elements for EiEvent.eiEventSignals
        __elements = ('signalName', 'signalType', 'signalID', 'currentValue', 'intervals')
        class intervals:
            # mandatory elements for EiEvent.eiEventSignals.intervals
            __elements = ('duration', 'uid', 'signalPayload')
            # EiEvent.eiEventSignals.intervals
            def __init__(self, **kwargs):
                valid_incoming_elements(EiEvent.eiEventSignals.intervals.__elements, kwargs.keys()) 
                if valid_duration(kwargs['duration']):
                    self.duration = kwargs['duration']
                if valid_uid(kwargs['uid']):
                    self.uid = kwargs['uid']
                if valid_signalPayload(kwargs['signalPayload']):
                    self.signalPayload = kwargs['signalPayload']
            def __str__(self):
                intvl  = '\t\tinterval:\n'
                intvl += '\t\t\tduration      = %s\n' % self.duration
                intvl += '\t\t\tuid           = %s\n' % self.uid
                intvl += '\t\t\tsignalPayload = %s\n' % self.signalPayload
                return intvl
            def getDict(self):
                return self.__dict__
        # EiEvent.eiEventSignals
        def __init__(self, **kwargs):
            valid_incoming_elements(EiEvent.eiEventSignals.__elements, kwargs.keys()) 
            if valid_signalName(kwargs['signalName']):
                self.signalName = kwargs['signalName']
            if valid_signalType(kwargs['signalType']):
                self.signalType = kwargs['signalType']
            if valid_signalID(kwargs['signalID']):
                self.signalID = kwargs['signalID']
            if valid_currentValue(kwargs['currentValue']):
                self.currentValue = kwargs['currentValue']
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
        def getDict(self):
            ES_d = {
            'signalName'   : self.signalName,
            'signalType'   : self.signalType,
            'signalID'     : self.signalID,
            'currentValue' : self.currentValue
            }
            intervals = []
            for interval in self.intervals:
                intervals.append(interval.getDict())
            ES_d['intervals'] = intervals
            return ES_d

    class eiTarget:
        # mandatory elements for EiEvent.eiTarget
        __elements = ('groupID', 'resourceID', 'venID', 'partyID')
        # EiEvent.eiTarget
        def __init__(self, **kwargs):
            valid_incoming_elements(EiEvent.eiTarget.__elements, kwargs.keys()) 
            if valid_groupID(kwargs['groupID']):
                self.groupID = kwargs['groupID']
            if valid_resourceID(kwargs['resourceID']):
                self.resourceID = kwargs['resourceID']
            self.venID = []
            for venId in kwargs['venID']:
                if valid_venID(venId):
                    self.venID.append(venId)
            if valid_partyID(kwargs['partyID']):
                self.partyID = kwargs['partyID']
        def __str__(self):
            tgt  = '%s:\n'               % self.__class__.__name__
            tgt += '\tgroupID    = %s\n' % self.groupID
            tgt += '\tresourceID = %s\n' % self.resourceID
            tgt += '\tvenID      = %s\n' % self.venID
            tgt += '\tpartyID    = %s\n' % self.partyID
            return tgt
        def getDict(self):
            return self.__dict__

    # EiEvent
    def __init__(self, **kwargs):
        valid_incoming_elements(EiEvent.__elements, kwargs.keys()) 
        self.eventDescriptor = EiEvent.eventDescriptor(**kwargs['eventDescriptor'])
        self.eiActivePeriod  = EiEvent.eiActivePeriod(**kwargs['eiActivePeriod'])
        self.eiEventSignals  = []
        for eventSignal in kwargs['eiEventSignals']:
            es = EiEvent.eiEventSignals(**eventSignal)
            self.eiEventSignals.append(es)
        self.eiTarget = EiEvent.eiTarget(**kwargs['eiTarget'])

    def __str__(self):
        event_str  = 'EiEvent:\n'
        event_str += '--------\n'
        event_str += str(self.eventDescriptor)
        event_str += str(self.eiActivePeriod)
        event_str += 'eiEventSignals:\n'
        for eventSignal in self.eiEventSignals:
            event_str += str(eventSignal)
        event_str += str(self.eiTarget)
        return event_str

    def getDict(self):
        EiEvent_d = {
        'eventDescriptor' : self.eventDescriptor.getDict(),
        'eiActivePeriod'  : self.eiActivePeriod.getDict(),
        'eiTarget'        : self.eiTarget.getDict()
        }
        eiEventSignals = []
        for eventSignal in self.eiEventSignals:
            eiEventSignals.append(eventSignal.getDict())
        EiEvent_d['eiEventSignals'] = eiEventSignals
        return EiEvent_d

