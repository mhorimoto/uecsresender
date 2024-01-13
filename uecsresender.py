#! /usr/bin/env python3
#code: utf-8

import sys
import datetime

lcnt=0   # line counter
lmax=100 # default line max limit
lbas=0   # line buffer TOD base
dift=0   #

lbuf = [ input() for i in range(lmax) ]

for i in range(lmax):
    tm = lbuf[i][0:8]
    dt = lbuf[i][9:19]
    msg= lbuf[i][20:]
    tod= dt+" "+tm
    date = datetime.datetime.strptime(tod, '%Y-%m-%d %H:%M:%S').timestamp()
    if i==0:
        lbas = date
    dift = (int)(date - lbas)
    print("{0} {1}".format(dift,msg))
