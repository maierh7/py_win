#! c:/Python/312/python

import os
import xlwings as xw

fn = "c:/Users/maierha/OneDrive - MediaMarktSaturn/BMS-Storage-2311.xlsx"

if os.path.exists (fn) is False:
    print ("Error " + fn + " does not exist")
    exit (1)

ws = xw.Book (fn).sheets ("AMS")

res = ws.range ("A2:F34").value

for i in res:
    print (i)
