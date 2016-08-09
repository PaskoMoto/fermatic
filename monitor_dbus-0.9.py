#!/usr/bin/python3
from gi.repository import GLib
import os
import sys
import dbus
import dbus.glib
OBJ_PATH = '/ril_0'
INTERFACE = 'org.ofono.NetworkRegistration'
SERVICE = 'org.ofono'
LOG = open('/home/nemo/fermatic/log.txt','a')
CellIds = [line.rstrip('\n') for line in open('cellid.txt')]
HOMENETWORK = True
def handler(member=None,sender=None,path=None):
   global HOMENETWORK
   if member == 'CellId':
     print("CellId:"+str(sender)+"\n")
     try:
       index = CellIds.index(str(sender))
       if HOMENETWORK:
          pass
       else:
          print ("Tenemos que cambiar a indoors"+"\n")
          os.system("dbus-send --system --print-reply --dest=net.connman /net/connman/service/cellular_YOUR_IMSI_NUMBER_HERE_context1 net.connman.Service.SetProperty string:\"AutoConnect\" variant:boolean:false")
          os.system("dbus-send --system --print-reply --dest=net.connman /net/connman/technology/wifi net.connman.Technology.SetProperty string:\"Powered\" variant:boolean:true")
#          os.system("killall openvpn")
          HOMENETWORK = True 
     except ValueError:
       if not HOMENETWORK:
          pass
       else:
          print ("Tenemos que cambiar a outdoors"+"\n")
#          os.system("killall openvpn")
          os.system("dbus-send --system --print-reply --dest=net.connman /net/connman/service/cellular_YOUR_IMSI_NUMBER_HERE_context1 net.connman.Service.SetProperty string:\"AutoConnect\" variant:boolean:true")
          os.system("dbus-send --system --print-reply --dest=net.connman /net/connman/technology/wifi net.connman.Technology.SetProperty string:\"Powered\" variant:boolean:false")
#         os.system("/usr/sbin/openvpn --user nobody --group nobody --config /etc/openvpn/Jolla.conf --dev p2p5 --dev-type tap --verb 4")
          LOG.write("CellID:"+str(sender)+"\n")
          HOMENETWORK = False

bus = dbus.SystemBus()
proxy_obj = bus.get_object(SERVICE, OBJ_PATH)
dbus_iface = dbus.Interface(proxy_obj, INTERFACE)
dbus_iface.connect_to_signal('PropertyChanged', handler, path_keyword='path')

mainloop = GLib.MainLoop()
mainloop.run()
