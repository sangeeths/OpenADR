
from string import ascii_lowercase as lower, \
                   ascii_uppercase as upper, \
                   digits as digits


# # # # # # # # # # # # # # # # # # # # # # # #
#
#       Input Validation for String
#     Parameters in Node/System Objects
#
VALID_NODE_STRING = {
'nodeId'    : {'allowed' : set(lower + \
                               digits + \
                               upper  + \
                               '_' + '-'),
               'min_len' : 5,
               'max_len' : 25,
              },
'prefix'    : {'allowed' : set(lower + \
                               digits + \
                               upper  + \
                               '_' + '-'),
               'min_len' : 3,
               'max_len' : 25,
              },
'summary'   : {'allowed' : set(lower + \
                               digits + \
                               upper  + \
                               '_' + '-' + ' ' + \
                               '(' + ')' + '&'),
               'min_len' : 15,
               'max_len' : 100,
              },
}
#
# # # # # # # # # # # # # # # # # # # # # # # #


