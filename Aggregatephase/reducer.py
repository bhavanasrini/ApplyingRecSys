#!/usr/bin/python
"""
Aggregating distance and applying weighted approach
"""
import sys
import os
import ast
from time import time
from itertools import groupby
from operator import itemgetter

key_dict = {}
start = time()

def read_input(file):
    for line in file:
        yield ast.literal_eval(line.strip())

data = read_input(sys.stdin)
"""
for current_word, group in groupby(data, (itemgetter(0),itemgetter(1))):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print(current_word, total_count)
        except ValueError:
            pass
"""
for key_line  in data:
	if len(key_line) != 3:
		continue
	temp = (int(key_line[0]),int(key_line[1]))
	if(temp in key_dict):
		values = key_dict[temp]
		values.append(float(key_line[2]))
		key_dict[temp] = values
	else:
		key_dict[temp] = [float(key_line[2])]
sys.stderr.write('reduced in ' + str(time()-start)+' seconds'+ os.linesep)
sys.stderr.flush()
for i in key_dict.keys():
	val = key_dict[i]
	print(i[0],i[1],sum(val))
sys.stderr.write('total time : ' + str(time()-start) + ' seconds'+ os.linesep)
