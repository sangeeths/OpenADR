from openadr.system.SystemManager import SystemManager

sysInfo = SystemManager().getSysInfo()

NODE     = sysInfo.nodeType
MODE     = sysInfo.mode
PROFILE  = sysInfo.profile
ID       = sysInfo.nodeId
IPADDR   = sysInfo.ipaddr
PORT     = sysInfo.port
PREFIX   = sysInfo.prefix
GUI_PORT = sysInfo.gui_port
SUMMARY  = sysInfo.summary

