#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

sys.setrecursionlimit(2000)

from test_wiki import *
from genepred import *

# model : to be discussed
states = ("N", "E1", "E2", "E3", "I1", "I2", "I3")

# model : to be discussed
# log values!
start_probability = {"N" : math.log(0.91), "E1" : math.log(pow(10, -30)), "E2" : math.log(pow(10, -30)), "E3" : math.log(pow(10, -30)), "I1" : math.log(0.03), "I2" : math.log(0.03), "I3": math.log(0.03)}

transition_probability = {
    "N"  : {"N" : 0.90, "E1" : 0.10, "E2" : pow(10, -30), "E3" : pow(10, -30), "I1" : pow(10, -30), "I2" : pow(10, -30), "I3" : pow(10, -30)},
    "E1" : {"N" : pow(10, -30), "E1" : pow(10, -30), "E2" : 0.95, "E3" : pow(10, -30), "I1" : 0.05, "I2" : pow(10, -30), "I3" : pow(10, -30)},
    "E2" : {"N" : pow(10, -30), "E1" : pow(10, -30), "E2" : pow(10, -30), "E3" : 0.95, "I1" : pow(10, -30), "I2" : 0.05, "I3" : pow(10, -30)},
    "E3" : {"N" : 0.01, "E1" : 0.94, "E2" : pow(10, -30), "E3" : pow(10, -30), "I1" : pow(10, -30), "I2" : pow(10, -30), "I3" : 0.05},
    "I1" : {"N" : pow(10, -30), "E1" : pow(10, -30), "E2" : 0.01, "E3" : pow(10, -30), "I1" : 0.99, "I2" : pow(10, -30), "I3" : pow(10, -30)},
    "I2" : {"N" : pow(10, -30), "E1" : pow(10, -30), "E2" : pow(10, -30), "E3" : 0.01, "I1" : pow(10, -30), "I2" : 0.99, "I3" : pow(10, -30)},
    "I3" : {"N" : pow(10, -30), "E1" : 0.01, "E2" : pow(10, -30), "E3" : pow(10, -30), "I1" : pow(10, -30), "I2" : pow(10, -30), "I3" : 0.99}
}

# model : to be discussed
emission_probability = {
    "N"  : {"A" : 0.10, "T" : 0.10, "G" : 0.40, "C" : 0.40},
    "E1" : {"A" : 0.30, "T" : 0.30, "G" : 0.20, "C" : 0.20},
    "E2" : {"A" : 0.30, "T" : 0.30, "G" : 0.20, "C" : 0.20},
    "E3" : {"A" : 0.30, "T" : 0.30, "G" : 0.20, "C" : 0.20},
    "I1" : {"A" : 0.10, "T" : 0.10, "G" : 0.40, "C" : 0.40},
    "I2" : {"A" : 0.10, "T" : 0.10, "G" : 0.40, "C" : 0.40},
    "I3" : {"A" : 0.10, "T" : 0.10, "G" : 0.40, "C" : 0.40},
    }

# return the list contains [[segment_list], [link_list]]
def readGFAfile(filename):

	gfa_file = open(filename)
	
	segment_list = [['0', ""]]
	link_list    = []

	for line in gfa_file:

		line_list = line.strip().split("\t")

		# segment lines [seqID, seq]
		if line_list[0] == 'S':
			segment_list.append(line_list[1:])

		# link lines [srcID, +/-, dstID, +/-, cigar ]
		elif line_list[0] == 'L':
			link_list.append(line_list[1:])
		
		# other lines
		else:
			pass

		gfa_list = [sorted(segment_list, key = lambda x: int(x[0])), sorted(link_list, key = lambda x: int(x[0])), sorted(link_list, key = lambda x: int(x[2]))]

	return gfa_list

# return the list of preceding segment ID(s) of specified segment ID
def precedingSegmentIDof(gfa_file, segment_id):

	# preSeg(0) = []
	# preseg(1) = [0]
	pre_seg_list = [[], [0]]

	for i in range(len(gfa_file[0])):
		pre_seg_list.append([])

	dst_sorted_link_list = gfa_file[2]

	for link in dst_sorted_link_list:
		pre_seg_list[int(link[2])].append(int(link[0]))
	
	return pre_seg_list[segment_id]
		
# return the list of following segment ID(s) of specified segment ID
def followingSegmentIDof(gfa_file, segment_id):

	# folSeg(0) = [1]
	fol_seg_list = [[1]]

	for i in range(len(gfa_file[0])):
		fol_seg_list.append([])

	src_sorted_link_list = gfa_file[1]

	for link in src_sorted_link_list:
		fol_seg_list[int(link[0])].append(int(link[2]))

	return fol_seg_list[segment_id]

# gfa_file = readGFAfile("cactus-BRCA2.gfa")
gfa_file = readGFAfile("graph.gfa")
# print(gfa_file[2])
# print(precedingSegmentIDof(gfa_file, 0))
# print(followingSegmentIDof(gfa_file, 0))

# print(viterbi_w_g(states, start_probability, transition_probability, emission_probability, gfa_file, 17))

visited = []
def gfaSearch(gfa_file, start_segment_id, visited):

	for i in followingSegmentIDof(gfa_file, start_segment_id):
		pcnt = 0
		print(i)
		pcnt += 1
		visited.append(i)
		
		# should we consider node DP merging?
		# if preSeg(i) >= 2, we should. 
		if len(precedingSegmentIDof(gfa_file, i)) == 0 or len(precedingSegmentIDof(gfa_file, i)) == 1:
			pass
		else:
			if pcnt == len(precedingSegmentIDof(gfa_file, i)):
				break
			else:
				gfaSearch(gfa_file, i, visited)
			# print(visited)
			# print("merge?")
			# if followingSegmentIDof(gfa_file, i) != []:
			# 	gfaSearch(gfa_file, i, visited)
			
		if followingSegmentIDof(gfa_file, i) == []:
			print("end\n")

		gfaSearch(gfa_file, i, visited)

gfa = gfa_file[0]
pre = []
fol = []
tmp = []

for  i in range(len(gfa)):
	
	pre.append(precedingSegmentIDof(gfa_file, i))
	fol.append(followingSegmentIDof(gfa_file, i))
	tmp.append([])

def topologicalSort(gfa, start_segment_id, pre, fol, tmp):
	# gfa = gfa_file[0]
	# pre = []
	# fol = []
	# tmp = []

	# queue = []

	# for  i in range(len(gfa) + 1):
		
	# 	pre.append(precedingSegmentIDof(gfa_file, i))
	# 	fol.append(followingSegmentIDof(gfa_file, i))
	# 	tmp.append([])
	# print(fol[start_segment_id])
	for i in fol[start_segment_id]:
		
		if len(pre[i]) == 0 or len(pre[i]) == 1:
			tmp[i].append(start_segment_id)
			print(i)

		elif len(pre[i]) >= 2:
			# print(i)
			tmp[i].append(start_segment_id)
			# print(tmp)

			if (set(pre[i]) & set(tmp[i])) == set(pre[i]):
				print("Segment ID " + str(i) + " : all preceding segments are visited, go! ")
				print(i)
				# continue
				
				if fol[i] == []:
					print("end")	
				
				# continue

			else:
				print("Segment ID " + str(i) + " : not all preceding segments are visited, waiting!")
				continue
		
		topologicalSort(gfa, i, pre, fol, tmp)

topologicalSort(gfa_file, 0, pre, fol, tmp)
# gfaSearch(gfa_file, 0, visited)
# print(visited)