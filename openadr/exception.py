
class InvalidOADRNodeType(Exception):
    def __init__(self, value='Invalid OADR Node Type'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidOADRProfile(Exception):
    def __init__(self, value='Invalid OADR Profile'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidServiceURL(Exception):
    def __init__(self, value='Invalid Service URL'):
        self.value = value
    def __str__(self):
        return repr(self.value)
 
class UnknownEiEventMessage(Exception):
    def __init__(self, value='Unknown EiEvent Message'):
        self.value = value
    def __str__(self):
        return repr(self.value)
 
class InvalidOADRNodeID(Exception):
    def __init__(self, value='Invalid OADR Node ID'):
        self.value = value
    def __str__(self):
        return repr(self.value)
