from enum import Enum
from os.path import join, normpath

from openadr import config as oadrCfg

oadrResponseRequired = Enum('always', 'never')

eventStatus = Enum('none', 'far', 'near', 'active', 'completed', 'cancelled')

optType = Enum('optIn', 'optOut')
