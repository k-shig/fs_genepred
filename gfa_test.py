#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import random
import time
from scipy.sparse import csr_matrix
import numba
from numba import jit

sys.setrecursionlimit(2000000)
sys.settrace 

from test_wiki import *
from genepred import *
from test_alb import viterbi_log, viterbi_log_g, seq2num

# return the list contains [[segment_list], [link_list]]
def readGFAfile(filename):

	gfa_file = open(filename)
	
	segment_list = [[0, ""]]
	link_list    = []

	for line in gfa_file:

		line_list = line.strip().split("\t")

		# segment lines [seqID, seq]
		if line_list[0] == 'S':
			line_list[2].replace("N", "") # N -> 4, emissi = 0 
			segment_list.append([int(line_list[1]), seq2num(line_list[2])])

		# link lines [srcID, +/-, dstID, +/-, cigar ]
		elif line_list[0] == 'L':
			link_list.append([int(line_list[1]), line_list[2], int(line_list[3]), line_list[4]])
		
		# other lines
		else:
			pass

	gfa_list = [sorted(segment_list, key = lambda x: x[0]), sorted(link_list, key = lambda x: x[0])]
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

# @profile
def topoSortGenePred2(gfa, start_segment_id):
	
	# print("\n")
	print("start_segment_id", start_segment_id, flush = True)
		
	# print("fol,", fol[start_segment_id])
	for i in fol[start_segment_id]:

		# print("startseg, i", start_segment_id, i)

		if len(pre[i]) == 0: 

			pass

		elif len(pre[i]) == 1:

			if pre[i] == [0]: # initial prediction
				print("initial prediction")

				# N - dimensional Markov Chain
				# s = gfa[allpath[start_segment_id][j][0]][1]
				# if len(s) < N:
				# 	s = np.append(s, gfa[allpath[start_segment_id][j][1][0]][1])
					
				# 	if len(s) < N:
				# 		s = np.append(s, gfa[allpath[start_segment_id][j][1][1][0]][1])
				# 		print(len(s))
				
				data[i].append(viterbi_log_g(start_probability, data_log, indices, indptr, emission_probability, gfa[i][1], True))
				allpath[i].append([i])
				# data[i] = np.append(data[i], viterbi_log_g(start_probability, transition_probability, emission_probability, gfa, i, True), axis = 0)
				# allpath[i] = np.append(allpath[i], [i], axis = 0)

				print("initial prediction has ended")
				pass
			
			else:
				
				# merging compare prediction results　

				# argmax way
				# print("length of data[pre[i][0]] before :", len(data[pre[i][0]]))

				# for j in range(1, len(data[pre[i][0]])):

				# 	print("base :", np.argmax(data[pre[i][0]][0]))

				# 	if np.argmax(data[pre[i][0]][0]) == np.argmax(data[pre[i][0]][j]):
						
				# 		print("j :", np.argmax(data[pre[i][0]][j]))
				# 		print("diff :", data[pre[i][0]][j] - data[pre[i][0]][0])

				# 		del data[pre[i][0]][j]
				# 		del allpath[start_segment_id][j]
				
				# print("length of data[pre[i][0]] after :", len(data[pre[i][0]]))


				# pre[i][0] == start_segment_id
				for j in range(len(data[pre[i][0]])):

					# N - dimensional Markov Chain
					s = gfa[allpath[start_segment_id][j][0]][1]
					if len(s) < N:
						s = np.append(s, gfa[allpath[start_segment_id][j][1][0]][1])
						
						if len(s) < N:
							s = np.append(s, gfa[allpath[start_segment_id][j][1][1][0]][1])

							if len(s) < N:
								s = np.append(s, gfa[allpath[start_segment_id][j][1][1][1][0]][1])
								print(len(s))
					
					print("k-mer integer :", k_mer_2_k_mer_integer(s[-N:]))


					data[i].append(viterbi_log_g(data[pre[i][0]][j], data_log, indices, indptr, emission_probability, gfa[i][1], False))
					# data[i] = np.append(data[i], viterbi_log_g(data[pre[i][0]][j], transition_probability, emission_probability, gfa, i, False), axis = 0)

				# for j in data[start_segment_id]:
				# 	data[i].append(viterbi_log_g(data[j][0], transition_probability, data_log, indices, indptr, emission_probability, gfa, i, False))

				for j in range(len(allpath[start_segment_id])):	

					allpath[i].append([i, allpath[start_segment_id][j]])
					# allpath[i] = np.append(allpath[i], [i, allpath[start_segment_id][j]], axis = 0)

				pass
		
		elif len(pre[i]) >= 2: # merging node

			# tmp[i] = tmp[i] - 1

			# argmax way
			# print(i, pre[i][0])
			# for j in range(1, len(data[pre[i][0]])):

			# 	print("base :", np.argmax(data[pre[i][0]][0]))

			# 	if np.argmax(data[pre[i][0]][0]) == np.argmax(data[pre[i][0]][j]):
					
			# 		# print("j :", np.argmax(data[pre[i][0]][j]))

			# 		del data[pre[i][0]][j]
			# 		del allpath[start_segment_id][j]


			if tmp[i] > 1:
				tmp[i] = tmp[i] - 1


				# experimentally comment out

				# for j in range(len(data[start_segment_id])):

				# 	# N - dimensional Markov Chain
				# 	s = gfa[allpath[start_segment_id][j][0]][1]
				# 	if len(s) < N:
				# 		s = np.append(s, gfa[allpath[start_segment_id][j][1][0]][1])
						
				# 		if len(s) < N:
				# 			s = np.append(s, gfa[allpath[start_segment_id][j][1][1][0]][1])
				# 			print(len(s))

				# 	data[i].append(viterbi_log_g(data[start_segment_id][j], data_log, indices, indptr, emission_probability, gfa[i][1], False))

				# for j in range(len(allpath[start_segment_id])):

				# 	allpath[i].append([i, allpath[start_segment_id][j]])
				# 	pass

				continue
				
			elif tmp[i] == 1:

				for j in range(len(data[start_segment_id])):

					# N - dimensional Markov Chain
					s = gfa[allpath[start_segment_id][j][0]][1]
					if len(s) < N:
						s = np.append(s, gfa[allpath[start_segment_id][j][1][0]][1])
						
						if len(s) < N:
							s = np.append(s, gfa[allpath[start_segment_id][j][1][1][0]][1])

							if len(s) < N:
								s = np.append(s, gfa[allpath[start_segment_id][j][1][1][1][0]][1])
								print(len(s))

					print("k-mer integer :", k_mer_2_k_mer_integer(s[-N:]))
					
					data[i].append(viterbi_log_g(data[start_segment_id][j], data_log, indices, indptr, emission_probability, gfa[i][1], False))
					# data[i] = np.append(data[i], viterbi_log_g(data[start_segment_id][j], transition_probability, emission_probability, gfa, i, False), axis = 0)

				for j in range(len(allpath[start_segment_id])):

					allpath[i].append([i, allpath[start_segment_id][j]])
					# allpath[i] = np.append(allpath[i], [i, allpath[start_segment_id][j]], axis = 0)

						
				if fol[i] == []:
					# break
					pass

		# print(len(data[pre[i][0]]))
		topoSortGenePred2(gfa, i)

	return 0

# @jit(nopython=True, fastmath=True)
def path2seq(path, segID_array):

	if len(path) == 1:
		segID_array.append(path[0])
		# print(path[0])

	else:
		path2seq(path[1], segID_array)
		# print(path[0])
		segID_array.append(path[0])

	num_seq = []

	for i in range(len(segID_array)):
		num_seq.extend(gfa[segID_array[i]][1])

	# print(len(seq))
	return np.array(num_seq)


def seq2traceback(num_seq):
	# print(num_seq)
	# print(type(num_seq))
	return viterbi_log(data_log, transition_probability, indices, indptr, start_probability, emission_probability, num_seq)

# @jit(nopython=True, fastmath=True)
def cosSimilarity(A, B):
	# print("cosSimilarity", flush = True)
	x = np.inner(A, B)
	s = np.linalg.norm(A)
	t = np.linalg.norm(B)
	print(A-B)
	# print(x / (s * t))
	return x / (s * t)

def diffSimilarity(A, B):
	print(np.linalg.norm(A-B))
	return np.linalg.norm(A-B)

@jit('i4(i4[:])', nopython = True, fastmath=True, cache=True)
def k_mer_2_k_mer_integer(k_mer_num_array):
	retval = 0
	for c in k_mer_num_array:
		retval *= 4
        # if c == 'A' or c == 'a':
		if c == 0:
			retval += 0
        # elif c == 'C' or c == 'c':
		elif c == 1:
			retval += 1
        # elif c == 'G' or c == 'g':
		elif c == 2:
			retval += 2
        # elif c == 'T' or c == 't':
		elif c == 3:
			retval += 3
	return retval

def numseq2string(numseq):

	stri = ""

	for n in numseq:

		if n == 0:
			stri += "A"
		elif n == 1:
			stri += "C"
		elif n == 2:
			stri += "G"
		elif n == 3:
			stri += "T"
	
	# print(stri)
	return stri


state_num = int(sys.argv[3])

# dimension of the HMM
N = 5

# start_probability = np.array([0.91, 0.0, 0.0, 0.0, 0.03, 0.03, 0.03])
start_probability = np.random.rand(state_num)
start_probability = start_probability / np.sum(start_probability)
# start_probability = np.array(start_probability, order='F')

# transition_probability = np.array(
# 	[[0.90, 0.10, 0.0, 0.0, 0.0, 0.0, 0.0],
# 	[0.0, 0.0, 0.95, 0.0, 0.05, 0.0, 0.0],
# 	[0.0, 0.0, 0.0, 0.95, 0.0, 0.05, 0.0],
# 	[0.01, 0.94, 0.0, 0.0, 0.0, 0.0, 0.05],
# 	[0.0, 0.0, 0.01, 0.0, 0.99, 0.0, 0.0],
# 	[0.0, 0.0, 0.0, 0.01, 0.0, 0.99, 0.0],
# 	[0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.99]]
# )
transition_probability = np.random.rand(state_num, state_num)

for i in range(state_num):
		for j in range(state_num):
			if transition_probability[i][j] <= float(sys.argv[2]):
				transition_probability[i][j] = 0

		transition_probability[i] = transition_probability[i] / np.sum(transition_probability[i])

transition_probability_CSR = csr_matrix(transition_probability.T)

data_log = np.array(np.log(transition_probability_CSR.data))
indices = np.array(transition_probability_CSR.indices)
indptr = np.array(transition_probability_CSR.indptr)

# print(type(data_log), type(indices), type(indptr))
# transition_probability = np.array(transition_probability, order='C')

# emission_probability = np.array(
# 	[[0.10, 0.10, 0.40, 0.40],
# 	[0.30, 0.30, 0.20, 0.20],
# 	[0.30, 0.30, 0.20, 0.20],
# 	[0.30, 0.30, 0.20, 0.20],
# 	[0.10, 0.10, 0.40, 0.40],
# 	[0.10, 0.10, 0.40, 0.40],
# 	[0.10, 0.10, 0.40, 0.40]]
# )

emission_probability = np.random.rand(state_num, 4)
for i in range(state_num):
	emission_probability[i] = emission_probability[i] / np.sum(emission_probability[i])

# emission_probability = np.array(emission_probability, order='F')

print("Data loading started.")

start = time.time()
gfa_file = readGFAfile(sys.argv[1])
end = time.time()

print("Data have loaded. Time taken:" + str(end - start) + " s")

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
	pre[link[2]].append(link[0])
	fol[link[0]].append(link[2])
for i in range(len(pre)):
	tmp.append(len(pre[i]))

# pre = np.array(pre)
# fol = np.array(fol)
# data = np.array(data)
# allpath = np.array(allpath)

# print(pre)
# print(fol)
# print(data)
# print(allpath)
end = time.time()

# print(pre[:1000])
# print(fol[:1000])
print("Lists have prepared. Time taken:" + str(end - start) + " s")

start = time.time()
print("Execution started.")

# transition_probability = np.array(
#         [[0.90, 0.10, 0.0, 0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.95, 0.0, 0.05, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.95, 0.0, 0.05, 0.0],
#         [0.01, 0.94, 0.0, 0.0, 0.0, 0.0, 0.05],
#         [0.0, 0.0, 0.01, 0.0, 0.99, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.01, 0.0, 0.99, 0.0],
#         [0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.99]]
#     )

# emission_probability = np.array(
#         [[0.10, 0.10, 0.40, 0.40, 0N],
#         [0.30, 0.30, 0.20, 0.20],
#         [0.30, 0.30, 0.20, 0.20],
#         [0.30, 0.30, 0.20, 0.20],
#         [0.10, 0.10, 0.40, 0.40],
#         [0.10, 0.10, 0.40, 0.40],
#         [0.10, 0.10, 0.40, 0.40]]
#     )

topoSortGenePred2(gfa, 0)
# topoSortGenePred2(gfa, 0) # 1st seg is NNNN...

end = time.time()

print("All nodes searched. Time taken : " + str(end - start) + " s")

# allpath = np.array(allpath)
# data = np.array(data)

# start = time.time()

print("Number of paths :", len(allpath[-1]))
gene_name = sys.argv[1].split('/')[1][:-4]
print("Gene name", gene_name)
f = open("SGFfasta/SGFout_" + gene_name + ".fa", "w")

for k in range(len(allpath[-1])):
	segID_array = []
	stri = ">" + gene_name + "　#" + str(k)
	f.write(stri + "\n")
	f.flush()
	f.write(numseq2string(path2seq(allpath[-1][k], segID_array)))
	f.flush()

f.close()
# end = time.time()

# print("Prediction time : " + str(end - start) + " s")
