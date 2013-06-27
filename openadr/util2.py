from openadr.exception import ValueNotFound


def str_to_enum(eNum, strItem):
    for element in eNum:
        if element.key == strItem:
            return element 
    msg = 'Value [%s] not found in [%s]' % \
          (strItem, eNum._keys)
    raise ValueNotFound(msg)

