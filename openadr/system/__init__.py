from openadr.system.SystemManager import SystemManager

sysInfo = SystemManager().getSysInfo()

NODE     = sysInfo.get_nodeType()
MODE     = sysInfo.get_mode()
PROFILE  = sysInfo.get_profile()
ID       = sysInfo.get_nodeId()
IPADDR   = sysInfo.get_ipaddr()
PORT     = sysInfo.get_port()
PREFIX   = sysInfo.get_prefix()
GUI_PORT = sysInfo.get_gui_port()
SUMMARY  = sysInfo.get_summary()

