from enum import Enum
from os.path import join, normpath

from openadr import config as oadrCfg

# pickle database to store all the EiEvents
# in the EiEventManager::__event_store dict
PICKLE_DB = normpath(join(oadrCfg.PERSISTENCE_ROOT, 'EiEventStore.pkl'))


oadrResponseRequired = Enum('always', 'never')




eventStatus = Enum('none', 'far', 'near', 'active', 'completed', 'cancelled')

optType = Enum('optIn', 'optOut')
