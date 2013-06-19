
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

class InvalidIPaddress(Exception):
    def __init__(self, value='Invalid IP Address'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidPort(Exception):
    def __init__(self, value='Invalid Port'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidOADRURLPrefix(Exception):
    def __init__(self, value='Invalid OADR URL Prefix'):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidOADRMode(Exception):
    def __init__(self, value='Invalid OADR Mode'):
        self.value = value
    def __str__(self):
        return repr(self.value)


