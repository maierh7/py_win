#! /cygdrive/c/Python/312/python

import os
import re
import subprocess as sub
import argparse as arg

par = arg.ArgumentParser ()
par.add_argument( "--pro",  default="mms-cif-database-qa-1000")
par.add_argument( "--hour", default="24")
args = par.parse_args ()

def show_path ():
    path = os.environ ["PATH"]
    lst = path.split (";")
    for i in lst:
        print (i)

# show_path ()

cmd = "gcloud auth login"
sub.run (cmd, shell = True)


cmd = "cloudctl permissions assign-temp --project " + args.pro +  " --duration " + args.hour + "h roles/compute.admin"
sub.run (cmd)
