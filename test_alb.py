# -*- coding:utf-8 -*-

import math
import numpy as np
import sys
import time
from scipy.sparse import csr_matrix, csc_matrix
from notify import *
import numba
from numba import jit


# def main():
#     # inf = math.inf

#     # state_num = 

#     start_probability = np.random.rand(state_num)
#     start_probability = start_probability / np.sum(start_probability)
#     start_probability = np.array(start_probability, order='F')

#     # make it SPARSE !
#     transition_probability = np.random.rand(state_num, state_num)

#     for i in range(state_num):
#         for j in range(state_num):
#             if transition_probability[i][j] <= float(sys.argv[1]):
#                 transition_probability[i][j] = 0

#         transition_probability[i] = transition_probability[i] / np.sum(transition_probability[i])

#     transition_probability = np.array(transition_probability)

#     transition_probability_CSR = csr_matrix(transition_probability.T)

#     data_log = np.array(np.log(transition_probability_CSR.data))
#     indices = np.array(transition_probability_CSR.indices)
#     indptr = np.array(transition_probability_CSR.indptr)


#     emission_probability = np.random.rand(state_num, 4)
#     for i in range(state_num):
#         emission_probability[i] = emission_probability[i] / np.sum(emission_probability[i])

#     emission_probability = np.array(emission_probability, order='F')

#     # observation_list
#     # seq = "ATTAGGTCTATGGAAGCCTAAGTTAAAACGCCAGCCTG"

#     seq = "CAG"
#     O = seq2num(seq).astype(np.int32)
#     O = np.array(O)

#     # Apply Viterbi algorithm
#     # S_opt, D, E = viterbi_log(transition_probability, start_probability, emission_probability, O)
#     start = time.time()
#     print("U", transition_probability.shape)
#     S_opt = viterbi_log(data_log, transition_probability, indices, indptr, start_probability, emission_probability, O)
#     # print('Observation sequence:   O = ', O)
#     # print('Optimal state sequence: S = ', S_opt)
#     end = time.time()
#     # print("Execution time: ", end - start, " s")
#     # np.set_printoptions(formatter={'float': "{: 7.4f}".format})
#     # print('D =', D, sep='\n')
#     # np.set_printoptions(formatter={'float': "{: 7.0f}".format})
#     # print('E =', E, sep='\n')

#     # prac_CSR(transition_probability)

#     return(end - start)

# convert DNA sequence to the list of numbers 0, 1, 2, 3
def seq2num(seq):
    seq_u = seq.upper()
    num_list = np.empty(len(seq_u)) 
    for i in range(len(seq_u)):
        if seq_u[i] == "A" or seq_u[i] == "a":
            num_list[i] = 0
        elif seq_u[i] == "C" or seq_u[i] == "c":
            num_list[i] = 1
        elif seq_u[i] == "G" or seq_u[i] == "g":
            num_list[i] = 2
        elif seq_u[i] == "T" or seq_u[i] == "t":
            num_list[i] = 3
        elif seq_u[i] == "N" or seq_u[i] == "n":
            num_list[i] = -1
            
    return num_list.astype(np.int32)

def viterbi(A, C, B, O):

    I = A.shape[0]    # Number of states
    N = len(O)  # Length of observation sequence

    # Initialize D and E matrices
    D = np.zeros((I, N))
    E = np.zeros((I, N-1)).astype(np.int32)
    D[:, 0] = np.multiply(C, B[:, 0])

    # Compute D and E in a nested loop
    for n in range(1, N):
        for i in range(I):
            temp_product = np.multiply(A[:, i], D[:, n-1])
            D[i, n] = np.max(temp_product) * B[i, O[n]]
            E[i, n-1] = np.argmax(temp_product)

    # Backtracking
    S_opt = np.zeros(N).astype(np.int32)
    S_opt[-1] = np.argmax(D[:, -1])
    for n in range(N-2, 0, -1):
        S_opt[n] = E[int(S_opt[n+1]), n]

    return S_opt, D, E

# @jit('i4[:](f8[:], f8[:,:], i4[:], i4[:], f8[:], f8[:,:], i4[:])', fastmath=True)
def viterbi_log(data_log ,transition_probability, indices, indptr, start_probability, emission_probability, O):

    # I = transition_probability.shape[0]    # Number of states
    I = len(indptr) - 1
    N = len(O)  # Length of observation sequence
    # tiny = np.finfo(0.).tiny
    print(type(transition_probability), transition_probability.shape)
    transition_probability_log = np.log(transition_probability)
    print("t, ",transition_probability.shape)
    transition_probability_log = np.array(transition_probability_log, order='F')
    print(transition_probability.shape)
    start_probability_log = np.log(start_probability)
    emission_probability_log = np.log(emission_probability)
    emission_probability_log = np.array(emission_probability_log, order='F')

    # print(transition_probability)

    # transition_probability_CSR = csr_matrix(transition_probability.T)

    # data_log = np.log(transition_probability_CSR.data)
    # indices = transition_probability_CSR.indices
    # indptr = transition_probability_CSR.indptr

    # print(A_log)

    # Initialize D and E matrices
    D_log_csr = np.zeros((I, N))
    D_log_m   = np.zeros((I, N))
    E_csr  = np.zeros((I, N-1)).astype(np.int32)
    E_m    = np.zeros((I, N-1)).astype(np.int32)
    D_log_csr[:, 0]   = start_probability_log + emission_probability_log[:, 0]
    D_log_m[:, 0]     = start_probability_log + emission_probability_log[:, 0]

    # Compute D and E in a nested loop
    # print("start computing D and E")
    # print(N)
    for n in range(1, N):

        # too slow
        # for i in range(I):
        #     temp_sum = transition_probability_log[:, i] + D_log[:, n-1]
        #     # print(temp_sum)
        #     D_log[i, n] = np.max(temp_sum) + emission_probability_log[i, O[n]]
        #     E[i, n-1] = np.argmax(temp_sum)

        ## 1216 kasahara
        # print(n)
        # 1行ずつ関数にして　関数呼び出し　cProfileで時間を見る
        
        print(transition_probability_log)

        Dlog_plus_trans_log_sqm = np.add(transition_probability_log.T, D_log_m[:, n-1]) # ここが本当に遅い？　遅いならCython使うとか。
        temp_sum_m = np.max(Dlog_plus_trans_log_sqm, axis = 1)
        E_m[:, n-1] = np.argmax(Dlog_plus_trans_log_sqm, axis = 1)
        D_log_m[:, n] = np.add(emission_probability_log[:, O[n]] , temp_sum_m)

        # 1222
        # print(data_log)
        # print(indices)
        # print(indptr)

        # for j in range(len(indptr) - 1):

        #     D_log_n_max = 0 - math.inf
        #     D_log_n_argmax = 0

        #     for i in indices[ indptr[j] : indptr[j + 1] ]:

        #         if transition_probability_log[i][j] + D_log_csr[i, n-1] >= D_log_n_max:
        #             D_log_n_max = transition_probability_log[i][j] + D_log_csr[i, n-1]
        #             D_log_n_argmax = i
            
        #     # print("D_log_n_max", D_log_n_max)

        #     E_csr[j, n - 1] = D_log_n_argmax
        #     D_log_csr[j, n] = np.add(emission_probability_log[j, O[n]], D_log_n_max)

    DP_calc_func(N, data_log, indices, indptr, transition_probability_log, D_log_csr, E_csr, emission_probability_log, O)

    # Backtracking
    # print("Backtracking start")
    S_opt = np.zeros(N).astype(np.int32)
    S_opt[-1] = np.argmax(D_log_csr[:, -1])

    for n in range(N-2, 0, -1):

        S_opt[n] = E_csr[int(S_opt[n+1]), n]

    # return S_opt, D_log, E
    # return D_log[:, -1]

    print("D_log_diff", D_log_csr - D_log_m, sep = '\n')
    print("E_diff", E_csr - E_m, sep = '\n')
    return S_opt

# @jit('i4(i8, f8[:], i4[:], i4[:], f8[:,:], f8[:,:], i4[:,:], f8[:,:], i4[:])', fastmath=True)
def DP_calc_func(N, data_log, indices, indptr, transition_probability_log, D_log_csr, E_csr, emission_probability_log, O):

    for n in range(1, N):

        for j in range(len(indptr) - 1):

            D_log_n_max = 0 - math.inf
            D_log_n_argmax = 0

            # for i in indices[ indptr[j] : indptr[j + 1] ]:
            for i in range(indptr[j],  indptr[j + 1]):

                if data_log[i] + D_log_csr[indices[i], n-1] > D_log_n_max:
                    D_log_n_max = data_log[i] + D_log_csr[indices[i], n-1]
                    D_log_n_argmax = indices[i]

                # if transition_probability_log[i][j] + D_log_csr[i, n-1] >= D_log_n_max:
                #     D_log_n_max = D_log_csr[i, n-1] + transition_probability_log[i][j]
                #     D_log_n_argmax = i
            
            # print("D_log_n_max", D_log_n_max)

            E_csr[j, n - 1] = D_log_n_argmax
            D_log_csr[j, n] = np.add(emission_probability_log[j, O[n]], D_log_n_max)


    return 0

# @profile
# @jit('f8[:](f8[:], f8[:], i4[:], i4[:], f8[:,:], i4[:], i4, i4, i4, f8[:], f8[:,:])', nopython = True, fastmath = True, cache = True)
def viterbi_log_g_first_seg(start_probability, data_log, indices, indptr, emission_probability_log, num_seq, state_num, len_seq, len_indptr, start_probability_log, D_log_csr):

    D_log_csr[:, 0] = start_probability_log + emission_probability_log[:, 0]
    # if is_first == True:

    #     D_log_csr[:, 0] = start_probability_log + emission_probability_log[:, 0]
        
    # else:

    DP_1st_column_func_g(len_indptr, indptr, data_log, start_probability, indices, D_log_csr, emission_probability_log, num_seq)

    # D_log_csr = DP_calc_func_g(len_seq, data_log, indices, indptr, D_log_csr, emission_probability_log, num_seq, len(indptr))

    # print("first", D_log_csr[:, -1])
    return D_log_csr[:, -1]

# @jit('f8[:](f8[:], f8[:], i4[:], i4[:], f8[:,:], i4[:], i4, i4, i4, f8[:], f8[:,:])', nopython = True, fastmath = True, cache = True)
def viterbi_log_g_not_first_seg(start_probability, data_log, indices, indptr, emission_probability_log, num_seq, state_num, len_seq, len_indptr, start_probability_log, D_log_csr):

    D_log_csr = DP_1st_column_func_g(len_indptr, indptr, data_log, start_probability, indices, D_log_csr, emission_probability_log, num_seq)

    # print("start_prob", start_probability)
    D_log_csr = DP_calc_func_g(len_seq, data_log, indices, indptr, D_log_csr, emission_probability_log, num_seq, len_indptr)
    # print(D_log_csr)
    
    # print("no_first", D_log_csr[:, -1])
    return D_log_csr[:, -1]


@jit('f8[:,:](i8, f8[:], i4[:], i4[:], f8[:,:], f8[:,:], i4[:], i4)', nopython = True, fastmath = True, cache = True)
def DP_calc_func_g(len_seq, data_log, indices, indptr, D_log_csr, emission_probability_log, num_seq, len_indptr):

    for n in range(1, len_seq):

        for j in range(len_indptr - 1):

            D_log_n_max = 0 - math.inf

            for i in range(indptr[j],  indptr[j + 1]):

                if data_log[i] + D_log_csr[indices[i], n-1] > D_log_n_max:
                    D_log_n_max = data_log[i] + D_log_csr[indices[i], n-1]
                    

            D_log_csr[j, n] = np.add(emission_probability_log[j, num_seq[n]], D_log_n_max)
    # print("all, ", D_log_csr)
    # print(D_log_csr)
    return D_log_csr

@jit('f8[:, :](i4, i4[:], f8[:], f8[:], i4[:], f8[:,:], f8[:,:], i4[:])', nopython = True, fastmath = True, cache = True)
def DP_1st_column_func_g(len_indptr, indptr, data_log, start_probability, indices, D_log_csr, emission_probability_log, num_seq):
    
    for j in range(len_indptr - 1):

        D_log_0_max = 0 - math.inf

        for i in range(indptr[j],  indptr[j + 1]):

            if data_log[i] + start_probability[indices[i]] > D_log_0_max:
                D_log_0_max = data_log[i] + start_probability[indices[i]]

        D_log_csr[j, 0] = np.add(emission_probability_log[j, num_seq[0]], D_log_0_max)
    # print("1st, ", D_log_csr)
    return D_log_csr

# for time plotting
def time_plot(notify = False):

    state_num_list = [10, 50, 100, 500, 1000, 2000,3000, 4000, 5000, 8000, 10000]

    state_num_list = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    state_num_list = [10]
    print(state_num_list)



    ave_time_list = []
    for state_num in state_num_list:
        sum_time = 0.0
        for i in range(1):
            sum_time += main(state_num)

    ave_time = sum_time / 1
    ave_time_list.append(ave_time)
    print(state_num, "states :", ave_time, "s")
    # print(ave_time)

    msg = str(state_num) + " states : " + str(ave_time) + " s\n"

    if notify == True:
        send_line_notify(msg)

    print(ave_time_list)

# time_plot()

# main(3)