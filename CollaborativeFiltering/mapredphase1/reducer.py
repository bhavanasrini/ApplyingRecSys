#!/usr/bin/python
from  datetime import datetime
import sys
import os
import math
import ast
list_enroll = {}
arr = []
for lines in sys.stdin:
	#print(lines)
	key_line = ast.literal_eval(lines)
	#arr = lines.split(",")
	key = key_line[0]
	value = key_line[1]
	if(key not in list_enroll):
		list_enroll[key] = [value]
	else:
		temp = list_enroll[key]
		temp.append(value)
		list_enroll[key] = temp
print(list_enroll)
