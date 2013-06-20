from openadr import userconfig as usrCfg
from openadr.system import IPADDR, GUI_PORT

GUI_BASE_URL = 'http://%s:%s%s/' % \
               (IPADDR, GUI_PORT, usrCfg.GUI_URL_PATH)

INDEX         = GUI_BASE_URL + 'index.py'
VIEW_SYSTEM   = GUI_BASE_URL + 'view_system_config.py'
UPDATE_SYSTEM = GUI_BASE_URL + 'update_system_config.py'
VIEW_NODE     = GUI_BASE_URL + 'view_node_config.py'
UPDATE_NODE   = GUI_BASE_URL + 'update_node_config.py'
VIEW_EVENTS   = GUI_BASE_URL + 'view_events.py'
UPDATE_EVENTS = GUI_BASE_URL + 'update_events.py'

