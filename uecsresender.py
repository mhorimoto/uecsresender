#! /usr/bin/env python3
#code: utf-8
# Version 1.10

import sys
import time
import datetime
import socket
import netifaces

lcnt=0   # line counter
lbas=0   # line buffer TOD base
repoch=0 # Epoch time diff in record
cepoch=0 # Current epoch time
i     =0

IFACE='enp4s0'

ADDRESS = netifaces.ifaddresses(IFACE)[netifaces.AF_INET][0]['broadcast']
PORT = 16520
DEST_ADDR = (ADDRESS,PORT)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((ADDRESS,PORT))

lbuf = []
for l in sys.stdin:
    lbuf.append(l.rstrip())

lmax = len(lbuf)

i=0

while True:
    tm = lbuf[i][0:8]
    dt = lbuf[i][9:19]
    msg= lbuf[i][20:]
    tod= dt+" "+tm
    date = datetime.datetime.strptime(tod, '%Y-%m-%d %H:%M:%S').timestamp()
    if i==0:
        print("set base val")
        lbas = date
        bepoch = int(time.time())
    cepoch = int(time.time()) - bepoch
    repoch = (int)(date - lbas)
    if (repoch<=cepoch):
        s.sendto(msg.encode("utf-8"),DEST_ADDR)
        print("i={0}  Cepoch={1}  Repoch={2} {3} {4}".format(i,cepoch,repoch,tm,msg))
        time.sleep(0.01)
        i+=1
        if (i>=lmax):
            break

