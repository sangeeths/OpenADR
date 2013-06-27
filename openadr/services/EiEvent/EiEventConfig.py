from enum import Enum

from string import ascii_lowercase as lower, \
                   ascii_uppercase as upper, \
                   digits as digits

RESPONSE_REQUIRED = Enum('always',
                         'never')

EVENT_STATUS = Enum('none',
                    'far',
                    'near',
                    'active',
                    'completed',
                    'cancelled')

OPT_TYPE = Enum('optIn', 
                'optOut')

SIGNAL_TYPE = Enum( 'delta',
                    'level',
                    'multiplier',
                    'price',
                    'priceMultiplier',
                    'priceRelative',
                    'product',
                    'setpoint')


# # # # # # # # # # # # # # # # # # # # # # # #
#
#       Input Validation for String
#      Parameters in EiEvent Objects
#
VALID_EVENT_STRING = {
'eventId'    : {'allowed' : set(lower + \
                                digits + \
                                upper + \
                                '_' + '-'),
                'min_len' : 5,
                'max_len' : 25,
               },
'vtnComment' : {'allowed' : set(lower + \
                                digits + \
                                upper + \
                                '_' + '-' + ' ' + \
                                '(' + ')' + '&'),
                'min_len' : 0,
                'max_len' : 200,
               },
'signalName' : {'allowed' : set(lower + \
                                digits + \
                                upper + \
                                '_' + '-'),
                'min_len' : 5,
                'max_len' : 25,
               },
'signalID'   : {'allowed' : set(lower + \
                                digits + \
                                upper + \
                                '_' + '-'),
                'min_len' : 5,
                'max_len' : 25,
               },
'venID'      : {'allowed' : set(lower + \
                                digits + \
                                upper + \
                                '_' + '-'),
                'min_len' : 5,
                'max_len' : 25,
               },
}
#
# # # # # # # # # # # # # # # # # # # # # # # #



