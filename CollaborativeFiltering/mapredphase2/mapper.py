#!/usr/bin/python
import sys
import os
import numpy as np
import ast
"""
Computing Cosine Similarity for non-zero vectors
"""
item_dict = {}
for lines in sys.stdin:
	item_dict = ast.literal_eval(lines)

items = list(item_dict.keys())
for i in range(len(items)):
	item1 = items[i]
	list1 = item_dict[item1]
	for j in range(i,len(items)):
		item2 = items[j]
		list2 = item_dict[item2]
		intersectLen = len(np.intersect1d(list1,list2))
		unionLen = len(np.union1d(list1,list2))
		print(((item1,item2),float(intersectLen/unionLen)))
		print(((item2,item1),float(intersectLen/unionLen)))

