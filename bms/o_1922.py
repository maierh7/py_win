#! /cygdrive/c/Python/312/python

import re
import os
import xlwings as xw

import argparse as arg

par = arg.ArgumentParser ()
par.add_argument ("--pct", default=0, type=int)
args = par.parse_args ()

lst = dict ()

fn = "c:/Users/maierha/OneDrive - MediaMarktSaturn/py_win/Oracle_19_22.xlsx"

if os.path.exists (fn) is False:
    print ("Error " + fn + " does not exist")
    exit (1)

ws = xw.Book (fn).sheets ("Usage")

res = ws.range ("H2:H29").value

for i in res:
    print (i)
