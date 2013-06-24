from enum import Enum

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


