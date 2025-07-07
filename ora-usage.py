#! /cygdrive/c/Python/312/python

import re
import os
import xlwings as xw

fn = "c:/Users/maierha/OneDrive - MediaMarktSaturn/Dokumente/ora-usage.xlsx"

ws = xw.Book (fn).sheets ("Usage")

res = ws.range ("h2:h29").value

for i in res:
    print (i)
