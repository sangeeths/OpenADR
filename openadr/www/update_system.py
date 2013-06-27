#!/usr/bin/env python

import cgitb; cgitb.enable()
import logging
import cgi

from openadr.www import *
from openadr import sysconfig as sysCfg

from openadr.system import NODE, MODE, PROFILE, ID, IPADDR, \
                           PORT, PREFIX, GUI_PORT, SUMMARY

from openadr.system.SystemManager import SystemManager
from openadr.node import Node

from openadr.node.NodeUtil import node_str_to_enum


sub_title = 'Update System Configuration'
logging.info(sub_title)


form = cgi.FieldStorage()

nodeType =  form.getvalue('node')
mode     =  form.getvalue('mode')
profile  =  form.getvalue('profile')
nodeid   =  form.getvalue('id')
ipaddr   =  form.getvalue('ip')
port     =  form.getvalue('port')
prefix   =  form.getvalue('prefix')
summary  =  form.getvalue('summary')
gui_port =  form.getvalue('gui_port')

node_dict = {
'nodeType' : nodeType,
'profile'  : profile,
'mode'     : mode,
'nodeId'   : nodeid,
'ipaddr'   : ipaddr,
'port'     : int(port),
'prefix'   : prefix,
'gui_port' : int(gui_port),
'summary'  : summary,
}

sysNode_d = node_str_to_enum(node_dict, sysNode=True)

try:
    node = Node(sysNode=True, **sysNode_d)
    SystemManager().setSysInfo(node)   
    #logging.info(str(node))
    output = "System configuration updated successfully!!"
except Exception, e:
    output = e


print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print h1()
print h2(sub_title)
print "Output : "
print '<b> %s </b> <br><br>' % output
print 'NOTE : you must restart the GUI and OpenADR process for the changes to reflect.' 
print '<br><br>' 
print 'Click <a href="%s">here</a> to continue...' % INDEX
print "</body>"
print "</html>"


