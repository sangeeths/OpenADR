#!/usr/bin/env python

import logging

logging.info('__init__.py file for www dir')

from enum import Enum
from netifaces import interfaces, ifaddresses, AF_INET

from openadr import sysconfig as sysCfg
from openadr.system import IPADDR, GUI_PORT, PROFILE, SUMMARY

GUI_BASE_URL = 'http://%s:%s%s/' % \
               (IPADDR, GUI_PORT, sysCfg.GUI_URL_PATH)


INDEX        = 'index.py'
VIEW_SYSTEM  = 'view_system.py'
EDIT_SYSTEM   = 'edit_system.py'
UPDATE_SYSTEM = 'update_system.py'
VIEW_NODE    = 'view_node.py'
ADD_NODE     = 'add_node.py'
EDIT_NODE    = 'edit_node.py'
DELETE_NODE  = 'delete_node.py'
VIEW_EVENT   = 'view_event.py'
ADD_EVENT    = 'add_event.py'
EDIT_EVENT   = 'edit_event.py'
DELETE_EVENT = 'delete_event.py'

URL_INDEX        = GUI_BASE_URL + INDEX
URL_VIEW_SYSTEM  = GUI_BASE_URL + VIEW_SYSTEM
URL_EDIT_SYSTEM  = GUI_BASE_URL + EDIT_SYSTEM
URL_UPDATE_SYSTEM = GUI_BASE_URL + UPDATE_SYSTEM
URL_VIEW_NODE    = GUI_BASE_URL + VIEW_NODE
URL_ADD_NODE     = GUI_BASE_URL + ADD_NODE
URL_EDIT_NODE    = GUI_BASE_URL + EDIT_NODE
URL_DELETE_NODE  = GUI_BASE_URL + DELETE_NODE
URL_VIEW_EVENT   = GUI_BASE_URL + VIEW_EVENT
URL_ADD_EVENT    = GUI_BASE_URL + ADD_EVENT
URL_EDIT_EVENT   = GUI_BASE_URL + EDIT_EVENT
URL_DELETE_EVENT = GUI_BASE_URL + DELETE_EVENT

PAGE = Enum('system', 'node', 'event')
ACTION = Enum('view', 'add', 'edit', 'delete')

def get_title(title=None):
    base_title  = 'RiptideIO\'s OpenADR'
    base_title += ' %s ' % sysCfg.OADR_VERSION
    base_title += '[\'%s\' Profile] - ' % PROFILE 
    base_title += SUMMARY
    if title is not None:
        base_title += ' - ' + title
    return base_title

def h1(header=None):
    if header is None: 
        header = get_title()
    return '<h1>' + header + '</h1>'

def h2(header=None):
    if header is None: 
        header = get_title()
    return '<h2>' + header + '</h2>'

def get_hyperlink(text=None, url=None):
    if text is None: return ''
    if url  is None:
        link = '<a>%s</a>' % (url)
    else:
        link = '<a href="%s">%s</a>' % (url, text)
    return link

def header(sub_title, page=PAGE.system, action=ACTION.view):
    # the page matrix contains the mapping of page and action
    # to the url which points to a cgi (.py) file
    page_matrix = {
        PAGE.system : { 
            ACTION.view : get_hyperlink('view', URL_VIEW_SYSTEM),
            ACTION.edit : get_hyperlink('edit', URL_EDIT_SYSTEM),
        }, 
        PAGE.node   : {
            ACTION.view   : get_hyperlink('view',   URL_VIEW_NODE),
            ACTION.add    : get_hyperlink('add',    URL_ADD_NODE),
            ACTION.edit   : get_hyperlink('edit',   URL_EDIT_NODE),
            ACTION.delete : get_hyperlink('delete', URL_DELETE_NODE),
        },
        PAGE.event  : {
            ACTION.view   : get_hyperlink('view',   URL_VIEW_EVENT),
            ACTION.add    : get_hyperlink('add',    URL_ADD_EVENT),
            ACTION.edit   : get_hyperlink('edit',   URL_EDIT_EVENT),
            ACTION.delete : get_hyperlink('delete', URL_DELETE_EVENT),
        },    
    }

    # mute the current page!
    del page_matrix[page][action]
    
    hdr = h1()
    hdr += '<ol>'
    for page, actions in page_matrix.iteritems():
        hdr += '<li>'
        hdr += '%s > ' % page.key
        for action, link in actions.iteritems():
            hdr += '%s ' % link
        hdr += '</li>'
    hdr += '</ol>'
    hdr += h2(sub_title)
    return hdr

def get_ip_address():
    ipaddr = {}
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        ipaddr[ifaceName] = ', '.join(addresses)
    return ipaddr


