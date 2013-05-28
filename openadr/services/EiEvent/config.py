from enum import Enum

oadrResponseRequired = Enum('always', 'never')




eventStatus = Enum('none', 'far', 'near', 'active', 'completed', 'cancelled')

optType = Enum('optIn', 'optOut')
