from enum import Enum
from os.path import join, normpath

oadrResponseRequired = Enum('always', 'never')

eventStatus = Enum('none', 'far', 'near', 'active', 'completed', 'cancelled')

optType = Enum('optIn', 'optOut')
