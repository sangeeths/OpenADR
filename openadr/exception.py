

class OADRException(Exception):
    def __init__(self, value='OADR Exception'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidOADRNodeType(OADRException):
    def __init__(self, value='Invalid OADR Node Type'):
        self.value = value

class InvalidOADRProfile(OADRException):
    def __init__(self, value='Invalid OADR Profile'):
        self.value = value

class InvalidServiceURL(OADRException):
    def __init__(self, value='Invalid Service URL'):
        self.value = value
 
class UnknownEiEventMessage(OADRException):
    def __init__(self, value='Unknown EiEvent Message'):
        self.value = value
 
class InvalidOADRNodeId(OADRException):
    def __init__(self, value='Invalid OADR Node Id'):
        self.value = value

class InvalidIPaddress(OADRException):
    def __init__(self, value='Invalid IP Address'):
        self.value = value

class InvalidPort(OADRException):
    def __init__(self, value='Invalid Port'):
        self.value = value

class InvalidOADRURLPrefix(OADRException):
    def __init__(self, value='Invalid OADR URL Prefix'):
        self.value = value

class InvalidOADRMode(OADRException):
    def __init__(self, value='Invalid OADR Mode'):
        self.value = value

class ValueNotFound(OADRException):
    def __init__(self, value='Invalid value'):
        self.value = value

class InvalidIncomingElements(OADRException):
    def __init__(self, value='Mismatch between Expected and Incoming Elements'):
        self.value = value

class InvalidOADRSummary(OADRException):
    def __init__(self, value='Invalid OADR Summary'):
        self.value = value

class InvalidValue(OADRException):
    def __init__(self, value='Invalid Value'):
        self.value = value

class InvalidLength(OADRException):
    def __init__(self, value='Invalid Length'):
        self.value = value

class InvalidInteger(OADRException):
    def __init__(self, value='Invalid Integer Value'):
        self.value = value

class InvalidFloatingPoint(OADRException):
    def __init__(self, value='Invalid Floating Point Value'):
        self.value = value

class InvalidEiEventId(OADRException):
    def __init__(self, value='Invalid EiEvent Id'):
        self.value = value

class InvalidEiEventModificationNumber(OADRException):
    def __init__(self, value='Invalid EiEvent Modification Number'):
        self.value = value

class InvalidEiEventPriority(OADRException):
    def __init__(self, value='Invalid EiEvent Priority'):
        self.value = value

class InvalidEiEventStatus(OADRException):
    def __init__(self, value='Invalid EiEvent Status'):
        self.value = value

class InvalidEiEventVTNComment(OADRException):
    def __init__(self, value='Invalid EiEvent VTN Comment'):
        self.value = value

class InvalidEiEventSignalName(OADRException):
    def __init__(self, value='Invalid EiEvent Signal Name'):
        self.value = value

class InvalidEiEventSignalId(OADRException):
    def __init__(self, value='Invalid EiEvent Signal Id'):
        self.value = value

class InvalidEiEventSignalType(OADRException):
    def __init__(self, value='Invalid EiEvent Signal Type'):
        self.value = value

class InvalidPositiveInteger(OADRException):
    def __init__(self, value='Invalid Positive Integer'):
        self.value = value

class InvalidEiEventResponseRequired(OADRException):
    def __init__(self, value='Invalid EiEvent Response Required'):
        self.value = value

class InvalidEiEventVENId(OADRException):
    def __init__(self, value='Invalid EiEvent VEN Id'):
        self.value = value



