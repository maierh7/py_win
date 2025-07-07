#! /cygdrive/c/Python/312/python

import os
import re
import subprocess as sub

res = dict ()
bname = "Benutzername"
lsetz = "Letztes Setzen des Kennworts"

def match_line (usr, search, line):
    m = re.match (r"^" + search + r"\s+(.*)", line)
    if m:
        if search == bname:
            res [m.group(1)] = ""
        else:
            res [usr] = m.group (1)

def get_user_stat (usr):
    cmd = "net user " + usr + " /domain"
    out = sub.check_output (cmd, shell=True).decode ("cp437")
    lin = out.splitlines ()
    for i in lin:
        match_line (usr, bname, i)
        match_line (usr, lsetz, i)
    
get_user_stat ("adm-maierha")
get_user_stat ("maierha")

for i in res:
    print ("%12s %s" % (i, res[i]))
