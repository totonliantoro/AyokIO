#!/usr/bin/env python


import sys

def celcius_to_fahr (temp_c):
    converted = temp_c*(9.0/5.0) + 32
    return converted

cels = float (sys.argv[1])
print('celcius_fahr(cels))