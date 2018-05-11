#!/usr/bin/python
# Converting CSV format to Inverted Index structure
import sys
import os
count = 0
for line  in sys.stdin.readlines():
	#next(line)
	arr = line.strip().split(",")
	if(count == 0):
		count = 1 
		continue
	print(("LatLong",(arr[1],(arr[9],arr[10]))))
	print(("orgid",(arr[1],arr[4])))
	print(("age",(arr[1],(arr[5],arr[6]))))
	print(("startdate",(arr[1],arr[8])))
