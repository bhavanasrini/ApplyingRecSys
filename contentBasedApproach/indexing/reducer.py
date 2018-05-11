#!/usr/bin/python
import sys
import os
import ast

key_dict = {}
for line  in sys.stdin:
	key_line = (ast.literal_eval(line))
	if key_line[0] in key_dict:
		temp = key_dict[key_line[0]]
		if key_line[1][1] in temp.keys():
			val = temp[key_line[1][1]]
			val.append(key_line[1][0])
			temp[key_line[1][1]] = val
		else:
			val = [key_line[1][0]]
			temp[key_line[1][1]] = val
	else:
		val  = {}
		val[key_line[1][1]] = [key_line[1][0]]
		key_dict[key_line[0]] = val
for i in key_dict.keys():
	print((str(i),key_dict[i]))
