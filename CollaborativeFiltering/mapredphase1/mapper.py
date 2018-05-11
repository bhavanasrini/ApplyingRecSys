#!/usr/bin/python
from  datetime import datetime
import sys
import os
import math
arr = []
lines = sys.stdin
next(lines)
for l in lines:
	arr = l.split(",")
	print((arr[2].strip('\n'),(arr[1].strip('\n'),1)))	
