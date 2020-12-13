#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import random
import time
import warnings
# warnings.filterwarnings('ignore')

sys.setrecursionlimit(2000000)
sys.settrace 

from test_wiki import *
from genepred import *
from test_alb import *

start_probability = np.array([0.91, 0.0, 0.0, 0.0, 0.03, 0.03, 0.03])

transition_probability = np.array(
	[[0.90, 0.10, 0.0, 0.0, 0.0, 0.0, 0.0],
	[0.0, 0.0, 0.95, 0.0, 0.05, 0.0, 0.0],
	[0.0, 0.0, 0.0, 0.95, 0.0, 0.05, 0.0],
	[0.01, 0.94, 0.0, 0.0, 0.0, 0.0, 0.05],
	[0.0, 0.0, 0.01, 0.0, 0.99, 0.0, 0.0],
	[0.0, 0.0, 0.0, 0.01, 0.0, 0.99, 0.0],
	[0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.99]]
)

emission_probability = np.array(
	[[0.10, 0.10, 0.40, 0.40],
	[0.30, 0.30, 0.20, 0.20],
	[0.30, 0.30, 0.20, 0.20],
	[0.30, 0.30, 0.20, 0.20],
	[0.10, 0.10, 0.40, 0.40],
	[0.10, 0.10, 0.40, 0.40],
	[0.10, 0.10, 0.40, 0.40]]
)

# return the list contains [[segment_list], [link_list]]
def readGFAfile(filename):

	gfa_file = open(filename)
	
	segment_list = [['0', ""]]
	link_list    = []

	for line in gfa_file:

		line_list = line.strip().split("\t")

		# segment lines [seqID, seq]
		if line_list[0] == 'S':
			line_list[2].replace("N", "")
			segment_list.append(line_list[1:])

		# link lines [srcID, +/-, dstID, +/-, cigar ]
		elif line_list[0] == 'L':
			link_list.append(line_list[1:])
		
		# other lines
		else:
			pass

	# gfa_list = [sorted(segment_list, key = lambda x: int(x[0])), sorted(link_list, key = lambda x: int(x[0])), sorted(link_list, key = lambda x: int(x[2]))]
	gfa_list = [sorted(segment_list, key = lambda x: int(x[0])), sorted(link_list, key = lambda x: int(x[0]))]
	return gfa_list

# return the list of preceding segment ID(s) of specified segment ID
def precedingSegmentIDof(gfa_file, segment_id):

	# pre_seg_list = [[], [0]]

	# for i in range(len(gfa_file[0])):
	# 	pre_seg_list.append([])

	# sorted_link_list = gfa_file[1]

	# for link in sorted_link_list:
	# 	pre_seg_list[int(link[2])].append(int(link[0]))
	
	# return pre_seg_list[segment_id]
	pass
		
# return the list of following segment ID(s) of specified segment ID
def followingSegmentIDof(gfa_file, segment_id):

	# fol_seg_list = [[1]]

	# for i in range(len(gfa_file[0])):
	# 	fol_seg_list.append([])

	# sorted_link_list = gfa_file[1]

	# for link in sorted_link_list:
	# 	fol_seg_list[int(link[0])].append(int(link[2]))

	# return fol_seg_list[segment_id]
	pass

def topologicalSort(gfa, start_segment_id, pre, fol, tmp):

	for i in fol[start_segment_id]:
		
		if len(pre[i]) == 0 or len(pre[i]) == 1:
			tmp[i].append(start_segment_id)
			print(i)
			if fol[i] == []:
				# print("end")	
				pass

		elif len(pre[i]) >= 2:
			# print(i)
			tmp[i].append(start_segment_id)
			# print(tmp)

			if (set(pre[i]) & set(tmp[i])) == set(pre[i]):
				print("Segment ID " + str(i) + " : all preceding segments are visited, go! ")
				print(i)
				# continue
				
				if fol[i] == []:
					# print("end")	
					pass
				
				# continue

			else:
				print("Segment ID " + str(i) + " : not all preceding segments are visited, waiting!")
				continue
		
		topologicalSort(gfa, i, pre, fol, tmp)

def topoSortGenePred(gfa, start_segment_id, hitotsumae, hitotsumae_cnt):
	print("start : " + str(start_segment_id))
	for i in fol[start_segment_id]:
		# print(i)
		if len(pre[i]) == 0:
			tmp[i].append(start_segment_id)
			print("id : " + str(i))
			# print(type(data[i]))
			# print(gfa[i])

			# To do:

			# 1. using the last DP column of the preceding segment,
			#    calculate the first DP column of the segment.
			# 2. using the first DP column of the segment (calculated in 1),
			#    calculate the DP matrix of this segment.

			# Implement
			
			# 1. using the last DP column of the preceding segment,
			#    calculate the first DP column of the segment.


			if fol[i] == []:
				# print("end")	
				pass

		elif len(pre[i]) == 1:
			
			tmp[i].append(start_segment_id)
			print("id : " + str(i))
			print("pre : 1")
			# print(type(data[i]))
			# print(gfa[i])

			if pre[i] == [0]: # initial prediction
				# hitotsumae = 0
				data[i].append(viterbi_w_g(states, start_probability, transition_probability, emission_probability, gfa, i, True))
				# data[i] = viterbi_w_g(states, start_probability, transition_probability, emission_probability, gfa, i)
				
				# seq = seq + gfa[i][1]
				# viterbi_w_g(states, start_probability, transition_probability, emission_probability, gfa, i)
				pass
			
			else:
				# print(pre[i])
				# print(pre[i][0])
				# print(data[pre[i][0]])
				# hitotsumae = pre[i][0]
				print(pre[i])
				print(len(data[i]))
				print(pre[i][len(data[i])])
				print(len(data[pre[i][len(data[i])]]))
				for j in range(len(data[pre[i][0]])):
					print("j : " + str(j))
					data[i].append(viterbi_w_g(states, data[pre[i][0]][j], transition_probability, emission_probability, gfa, i, False))
					print(len(data[i]))
				# data = viterbi_w_g(states, data[pre[i][0]], transition_probability, emission_probability, gfa, i)
				
				# seq = seq + gfa[i][1]
				pass
			

		elif len(pre[i]) >= 2: # merging node
			print("merging node\n")
			print("id : " + str(i))
			print("pre : 2~")
			
			print("1tumae  : " + str(hitotsumae))
			tmp[i].append(start_segment_id)
			# print(tmp)

			if (set(pre[i]) & set(tmp[i])) != set(pre[i]): # totemo omoi
				hitotsumae = pre[i][hitotsumae_cnt]
				print("Segment ID " + str(i) + " : not all preceding segments are visited, waiting!")

				# To do:

				# 1. using the last DP column of the preceding segment,
				#    calculate the first DP column of the segment.
				# 2. using the first DP column of the segment (calculated in 1),
				#    calculate the DP matrix of this segment.
				
				# print(len(data[pre[i][0]]))
				print(pre[i])
				print(len(data[i]))
				print(pre[i][len(data[i])])
				print(len(data[pre[i][len(data[i])]]))
				
				for j in range(len(data[hitotsumae])):
					# pass
					print("j : " + str(j))
					print(pre[i][len(data[i])])
					# data[i].append(viterbi_w_g(states, data[pre[i][len(data[i])]][j], transition_probability, emission_probability, gfa, i, False))
					# data[i].append(viterbi_w_g(states, data[hitotsumae][j], transition_probability, emission_probability, gfa, i, False))
					print(len(data[i]))
				print(data)
				# data[i] = viterbi_w_g(states, data[pre[i][0]], transition_probability, emission_probability, gfa, i)
				# seq = seq + gfa[i][1]
				
				hitotsumae_cnt = hitotsumae_cnt + 1
				continue
				
			else:
				# hitotsumae = pre[i][hitotsumae_cnt]
				print("Segment ID " + str(i) + " : all preceding segments are visited, go! ")
				print("id : " + str(i))
				# print(type(data[i]))
				# print(data[pre[i][0]])
				print(pre[i])
				print(len(data[i]))
				# print(pre[i][len(data[i])])
				# print(len(data[pre[i][len(data[i])]]))
				# print("1tumae  : " + str(hitotsumae))
				
				# for j in range(len(data[hitotsumae])):
				# 	data[i].append(viterbi_w_g(states, data[hitotsumae][j], transition_probability, emission_probability, gfa, i, False))

				for j in pre[i]:
					for k in data[j]:
						data[i].append(viterbi_w_g(states, k, transition_probability, emission_probability, gfa, i, False))

				print(len(data[i]))
				print(data)
				# data[i] = viterbi_w_g(states, data[pre[i][0]], transition_probability, emission_probability, gfa, i)
				# seq = seq + gfa[i][1]
				# continue
				
				if fol[i] == []:
					# print("end")
					pass	
				
				# continue
		# print(data)
		topoSortGenePred(gfa, i, hitotsumae, hitotsumae_cnt)

def topoSortGenePred2(gfa, start_segment_id):
	
	if start_segment_id % 10000 == 0:
		print(start_segment_id)
		
	for i in fol[start_segment_id]:

		if len(pre[i]) == 0:

			allpath[i].append(np.array([i]))

			if fol[i] == []:

				pass

		elif len(pre[i]) == 1:

			if pre[i] == [0]: # initial prediction
				print("initial prediction")
				data[i].append(viterbi_log_g(start_probability, transition_probability, emission_probability, gfa, i, True))
				cp = allpath[start_segment_id].copy()
				allpath[i].append(np.append(cp, np.array([i])))
				print("initial prediction has ended")
				pass
			
			else:
				for j in range(len(data[pre[i][0]])):

					data[i].append(viterbi_log_g(data[pre[i][0]][j], transition_probability, emission_probability, gfa, i, False))
					cp = allpath[start_segment_id][j].copy()
					allpath[i].append(np.append(cp, np.array([i])))
				pass
		
		elif len(pre[i]) >= 2: # merging node

			if tmp[i] > 1:
				tmp[i] = tmp[i] - 1

				# for j in range(len(data[start_segment_id])):

				# 	# experimental

				# 	# data[i].append(viterbi_log_g(data[start_segment_id][j], transition_probability, emission_probability, gfa, i, False))
				# 	# cp = allpath[start_segment_id][j].copy()
				# 	# allpath[i].append(np.append(cp, np.array([i])))

				# 	pass
				continue
				
			elif tmp[i] == 1:

				for j in range(len(data[start_segment_id])):

					data[i].append(viterbi_log_g(data[start_segment_id][j], transition_probability, emission_probability, gfa, i, False))
					cp = allpath[start_segment_id][j].copy()
					allpath[i].append(np.append(cp, np.array([i])))
				
				if fol[i] == []:

					pass	
		
		# clear the memory
		if i > 1000 and i % 1000 == 0:
			data[:i].clear()
			allpath[:i].clear()
			pre[:i - 10].clear()
			fol[:i - 10].clear()

		topoSortGenePred2(gfa, i)

def path2seq(gfa, path):
	seq = ""
	for i in range(len(path)):
		seq = seq + gfa[int(path[i])][1]
	# print(seq)
	return seq

def seq2traceback(seq):
	return viterbi_log(transition_probability, start_probability, emission_probability, seq2num(seq)).astype(np.int32)

print("Data loading started.")

start = time.time()
gfa_file = readGFAfile(sys.argv[1])
end = time.time()

print("Data have loaded. Time taken:" + str(end - start) + " ms")

# preparing empty lists and a gfa file for running topological sort
gfa = gfa_file[0] # segment list
pre  = [] # The list of preceding segment(s)
fol  = [] # The list of following segment(s)
tmp  = [] # The list (will be used) to topologically sort the graph 
data = [] # The list containing data (which will be) used for backtracing
allpath = [] # The list of all paths

# random.shuffle(gfa)

print("Lists preparing started.")
start = time.time()

for i in range(len(gfa)):
	pre.append([])
	fol.append([])
	data.append([])
	allpath.append([])

pre[1] = [0]
fol[0] = [1]

for link in gfa_file[1]:
	pre[int(link[2])].append(int(link[0]))
	fol[int(link[0])].append(int(link[2]))

for i in range(len(pre)):
	tmp.append(len(pre[i]))

end = time.time()

# print(pre[:1000])
# print(fol[:1000])
print("Lists have prepared. Time taken:" + str(end - start) + " ms")

start = time.time()
print("Execution started.")

transition_probability = np.array(
        [[0.90, 0.10, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.95, 0.0, 0.05, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.95, 0.0, 0.05, 0.0],
        [0.01, 0.94, 0.0, 0.0, 0.0, 0.0, 0.05],
        [0.0, 0.0, 0.01, 0.0, 0.99, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.01, 0.0, 0.99, 0.0],
        [0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.99]]
    )

emission_probability = np.array(
        [[0.10, 0.10, 0.40, 0.40],
        [0.30, 0.30, 0.20, 0.20],
        [0.30, 0.30, 0.20, 0.20],
        [0.30, 0.30, 0.20, 0.20],
        [0.10, 0.10, 0.40, 0.40],
        [0.10, 0.10, 0.40, 0.40],
        [0.10, 0.10, 0.40, 0.40]]
    )

topoSortGenePred2(gfa, 0)
# topoSortGenePred2(gfa, 0) # 1st seg is NNNN...


for k in range(len(allpath[-1])):
	print("path : " + str(allpath[-1][k]))
	# print(path2seq(gfa, allpath[-1][k]))
	# print(data[-1][k])
	print(seq2traceback(path2seq(gfa, allpath[-1][k])))
	print("\n")

end = time.time()

print("Execution time : " + str(end - start) + " ms")

# print("\n segments yosoku \n")

# seq1 = gfa[1][1] + gfa[2][1] + gfa[3][1]
# seq2 = gfa[1][1] + gfa[3][1]

# print(viterbi_log(transition_probability, start_probability, emission_probability, seq2num(seq1)))
# print(viterbi_log(transition_probability, start_probability, emission_probability, seq2num(seq2)))
