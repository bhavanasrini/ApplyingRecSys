#!/usr/bin/python
import gc
from  datetime import datetime
import itertools
from time import time
import ast
import sys
import os
import math
from scipy.stats import rankdata
import numpy
MAX_DISTANCE = 30
radius = 3000
sys.stderr.write('Started job '+os.linesep)

def read_input(file):
    for line in file:
        yield ast.literal_eval(line)

data = read_input(sys.stdin)

for key_line in data:
	sys.stderr.write(key_line[0]+os.linesep)
	if(key_line[0] == "startdate"):		
		sys.stderr.write("Running startdate "+os.linesep)
		sys.stderr.flush()
		list_date=list(key_line[1].keys())
		#convrank = rankdata([(i[0]) for i in list_date],method='ordinal')
		convrank = numpy.array(list_date).argsort().argsort()
		maxRank = max(convrank)-1
		comb = list(itertools.combinations_with_replacement(list_date,2))
		sys.stderr.write(str(int(sys.getsizeof(comb))/(1048576))+os.linesep)
		sys.stderr.write(str(len(comb))+os.linesep)
		sys.stderr.flush()
		count_startdate = 0
		start = time()
		start1 = time()
		for dates in comb:
			count_startdate+=1
			if not all(dates):
				continue
			ind1 = list_date.index(dates[0])
			ind2 = list_date.index(dates[1])
			if convrank[ind1] == convrank[ind2]:
				values = list(itertools.product(key_line[1][dates[0]],key_line[1][dates[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),0)
						print(int(val[1]),int(val[0]),0)
					else:
						print(int(val[0]),int(val[1]),0)
			elif convrank[ind1] > convrank[ind2]:
				temp = abs((convrank[ind1]-convrank[ind2])/(maxRank-1))
				values = list(itertools.product(key_line[1][dates[0]],key_line[1][dates[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),temp)
						print(int(val[1]),int(val[0]),temp)
					else:
						print(int(val[0]),int(val[1]),temp)
			else:
				temp = abs((convrank[ind2]-convrank[ind1])/(maxRank-1))
				values = list(itertools.product(key_line[1][dates[0]],key_line[1][dates[1]]))
				for al in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),temp)
						print(int(val[1]),int(val[0]),temp)
					else:
						print(int(val[0]),int(val[1]),temp)
			del values
			gc.collect()
			if count_startdate == 1000:
				sys.stdout.flush()
				count_startdate = 0
				sys.stderr.write(" Time taken for date to complete 1000 computations "+str(time()-start)+os.linesep)
				start = time()
				sys.stderr.flush()
		del comb
		gc.collect()
		sys.stderr.write(" Total time taken computations "+str(time()-start1)+os.linesep)
	elif(key_line[0]=="LatLong"):
		start = time()
		sys.stderr.write("Running Latlong "+os.linesep)
		list_zipcode = list(key_line[1].keys())
		comb = list(itertools.combinations_with_replacement(list_zipcode,2))
		sys.stderr.write(str(int(sys.getsizeof(comb))/(1048576))+os.linesep)
		sys.stderr.write(str(len(comb))+os.linesep)
		sys.stderr.flush()
		start = time()
		start1 = time()
		count_zip = 0
		for zipcode in comb:
			count_zip+=1
			if not all(zipcode[0]) or not all(zipcode[1]):
				continue
			list1 = []
			list1.append(float(zipcode[0][0]))
			list1.append(float(zipcode[0][1]))
			list2 = []
			list2.append(float(list_zipcode[1][0]))
			list2.append(float(list_zipcode[1][1]))
			dlat = math.radians(list2[0] - list1[0])
			dlon = math.radians(list2[1] - list2[1])
			a = (math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(list1[0])) * math.cos(math.radians(list2[0])) * math.sin(dlon / 2) * math.sin(dlon/2))
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
			distance = radius * c
			if distance == 0:
				values = list(itertools.product(key_line[1][zipcode[0]],key_line[1][zipcode[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),0)
						print(int(val[1]),int(val[0]),0)
					else:
						print(int(val[0]),int(val[1]),0)
			elif distance > MAX_DISTANCE :
				values = list(itertools.product(key_line[1][zipcode[0]],key_line[1][zipcode[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),1)
						print(int(val[1]),int(val[0]),1)
					else:
						print(int(val[0]),int(val[1]),1)
			else:
				values = list(itertools.product(key_line[1][zipcode[0]],key_line[1][zipcode[1]]))
				for val in values: 
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),distance/30)
						print(int(val[1]),int(val[0]),distance/30)
					else:
						print(int(val[0]),int(val[1]),distance/30)
			del values
			gc.collect()
			if count_zip == 1000:
				sys.stdout.flush()
				count_zip = 0
				sys.stderr.write(" Time taken for Latlong to complete 1000 computations "+str(time()-start)+os.linesep)
				start = time()
				sys.stderr.flush()
		del comb
		gc.collect()
		sys.stderr.write("LatLong "+ str(time()-start1) +os.linesep)	
	elif key_line[0]=="orgid":
		start = time()
		sys.stderr.write("Running orgId "+os.linesep)
		list_id=list(key_line[1].keys())
		comb = list(itertools.combinations_with_replacement(list_id,2))
		sys.stderr.write(str(int(sys.getsizeof(comb))/(1048576))+os.linesep)
		sys.stderr.write(str(len(comb))+os.linesep)
		sys.stderr.flush()
		start = time()
		start1 = time()
		count_id = 0
		for id in comb:
			count_id+=1
			if(id[0]==id[1]):
				values = list(itertools.product(key_line[1][id[0]],key_line[1][id[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),0)
						print(int(val[1]),int(val[0]),0)
					else:
						print(int(val[0]),int(val[1]),0)
			else:
				values = list(itertools.product(key_line[1][id[0]],key_line[1][id[1]]))
				for val in values:
					if(int(val[0]) != int(val[1])):
						print(int(val[0]),int(val[1]),1)
						print(int(val[1]),int(val[0]),1)
					else:
						print(int(val[0]),int(val[1]),1)
			if count_id == 1000:
				sys.stdout.flush()
				count_id = 0
				sys.stderr.write(" Time taken for id to complete 1000 computations "+str(time()-start)+os.linesep)
				start = time()
				sys.stderr.flush()
		del comb
		gc.collect()
		sys.stderr.write("Id "+str(time()-start1)+os.linesep)
	elif key_line[0] == "age":
		start = time()
		sys.stderr.write("Running age "+os.linesep)
		list_age = list(key_line[1].keys())
		comb = list(itertools.combinations_with_replacement(list_age,2))
		sys.stderr.write(str(int(sys.getsizeof(comb))/(1048576))+os.linesep)
		sys.stderr.write(str(len(comb))+os.linesep)
		sys.stderr.flush()
		start = time()
		start1 = time()
		count_age = 0
		for maxmin in comb:
			count_age+=1
			#print(maxmin)
			if((int(maxmin[0][0])==int(maxmin[1][0])) and (int(maxmin[0][1])==int(maxmin[1][1]))):
					values = list(itertools.product(key_line[1][maxmin[0]],key_line[1][maxmin[1]]))
					for val in values:
						if(int(val[0]) != int(val[1])):
							print(int(val[0]),int(val[1]),0)
							print(int(val[1]),int(val[0]),0)
						else:
							print(int(val[0]),int(val[1]),0)
			elif(int(maxmin[0][1]) <= int(maxmin[1][0]) or int(maxmin[1][1]) <= int(maxmin[0][0]) or (int(maxmin[0][1]) > int(maxmin[1][0]) and int(maxmin[0][0]) > int(maxmin[1][1]))):
					values = list(itertools.product(key_line[1][maxmin[0]],key_line[1][maxmin[1]]))
					for val in values:
						if(int(val[0]) != int(val[1])):
							print(int(val[0]),int(val[1]),1)
							print(int(val[1]),int(val[0]),1)
						else:
							print(int(val[0]),int(val[1]),1)
			else:
				if ((abs(int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0])))>1):
					values = list(itertools.product(key_line[1][maxmin[0]],key_line[1][maxmin[1]]))
					#print("greater than 1")
					for val in values:
						if(int(val[0]) != int(val[1])):
							print(int(val[0]),int(val[1]),1/abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
							print(int(val[1]),int(val[0]),1/abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
						else:
							print(int(val[0]),int(val[1]),1/abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
				else:
					values = list(itertools.product(key_line[1][maxmin[0]],key_line[1][maxmin[1]]))
					#print("Lesser than 1")
					for val in values:
						if(int(val[0]) != int(val[1])):
							print(int(val[0]),int(val[1]),abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
							print(int(val[1]),int(val[0]),abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
						else:
							print(int(val[0]),int(val[1]),abs((int(maxmin[0][1])-int(maxmin[1][0]))/(int(maxmin[1][1])-int(maxmin[0][0]))))
			del values
			gc.collect()
			if count_age == 1000:
				sys.stdout.flush()
				count_age = 0
				sys.stderr.write(" Time taken to age for 1000 computations "+str(time()-start)+os.linesep)
				start = time()
				sys.stderr.flush()
		del comb
		gc.collect()
		sys.stderr.write("age "+str(time()-start1)+os.linesep)
