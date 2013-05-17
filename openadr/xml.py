from lxml import etree
from io import StringIO
from io import BytesIO

from openadr import config as oadrCfg


def valid_oadr_xml(xml_s):
    
    # get oadr schema handle
    #   oadr_schema_f = handle to the schema file
    #   oadr_schema_h = lxml handle to the schema xml
    #   oadr_schema   = this is the schema handle that 
    #                   should be used against all the 
    #                   incoming xml data
    #
    with open(oadrCfg.XSD[oadrCfg.PROFILE], 'r') as oadr_schema_f:
        oadr_schema_h = etree.parse(oadr_schema_f)
    oadr_schema = etree.XMLSchema(oadr_schema_h)
   
    # get lxml handle for the incoming xml data 
    xml_h = etree.parse(BytesIO(xml_s))

    compliance = oadr_schema.validate(xml_h)

    # if the incoming xml adhere to the 
    # OpenADR Profile Schema then return
    # the lxml handle, else return None
    #
    if compliance is True: return xml_h
    else: return None


def root_element(xml_h):
    return xml_h.xpath('local-name()')


def get_oadr_msg(service, xml_h):
    root = root_element(xml_h)
    for msg in oadrCfg.SERVICE_MESSAGE[service]:
        if root == msg.key:
            return msg
    return None      

 
