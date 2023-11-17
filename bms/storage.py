#! /cygdrive/c/Python/312/python

import os
import xlwings as xw

import argparse as arg

par = arg.ArgumentParser ()
par.add_argument ("--pct", default=0, type=int)
args = par.parse_args ()

lst = dict ()

fn = "c:/Users/maierha/OneDrive - MediaMarktSaturn/BMS-Storage-2311.xlsx"

if os.path.exists (fn) is False:
    print ("Error " + fn + " does not exist")
    exit (1)

ws = xw.Book (fn).sheets ("AMS")

res = ws.range ("A2:F34").value

for i in res:
    vd = i[0]
    lst [vd] = i

s_pct = sorted (lst.items (), key = lambda kv: kv[1][5])


print ("%16s %5s %8s %8s" % ("", "PCT", "Apparent", "Size"))
for i in s_pct:
    vd  = i[0]
    sz  = i[1][3]
    ap  = i[1][4]
    pct = i[1][5]

    if pct < args.pct:
        continue
    
    print ("%s %5.2f %8.3f %8.3f" % (vd, pct, ap, sz))


