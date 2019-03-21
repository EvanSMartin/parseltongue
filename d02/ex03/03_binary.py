#!/usr/bin/env python3
import sys

base = int(sys.argv[1])
#print("Your binary is {0:b}".format(base))
print(bin(base)[2:])
print(oct(base)[2:])
print(hex(base)[2:])
