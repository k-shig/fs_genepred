#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
	
# model : to be discussed
states = ("N", "E1", "E2", "E3", "I1", "I2", "I3")

# sequence : read files?
sequence = "TATTAGGTCTATGGAAGCCTAAGTTAAAACGCCAGCCTGGCCTTAAAATTACCTCCGCCTGCCTTTCGCCTCAATCGATGCCTTATGCAAATTTTTTTTTATTTCTAAATTTTTCTCATCAAATTAATAAAAATGAGAAAATTGAATATTTGCAAGTTCTCGCGGGCAGGTTTCAAGCAGGCGTTAGTTTTTGGCTCCCCCAATTTTTTTTTGAATTTTTATTCCAAAAGTTACAGAACTAAAAGCTCTTTTTTGAAATTTTTAGACTGAAAATCAAAAATTTTAATTTAAAATTTTTTTTTTAATTTAAGAACTCAAAAAATGAAAGTTTGGTCGTTTTCCGAATATTTAAACAAAATCTACTGGGAATCTATTTGGATTTTAAAATATTATAAAGAACTGTTTTTGTTGTAAATGTAGATTTGAAAAGTTCAACAAAATAAATTTCTTACAATTTTTTTTTCAGTATTTGTTTTTTTTTGTTGCAAGAATCGTGAAAAAATATTTTTTGAAACATTTTCGGAAGCCTGATCTTATTTATACTCTTTTAGCGAACAATTTTTCAAACAAAAGTTATTTTCAAAAAAATGTTCCTAAAAAATAATTTAAAATTAAAAAAAAATTACAGAAAAAATCCCCAGTTTTTAGAAAATTAAATTTTAGAAATTAGGAAAATTCCAAAACTCTGTGATTGTCACATTCCAAGCAGGGTGTGCGGCTGATTGATTTTTTTGGTTGTCGGCTGGTAGCACTAAAATGGGTAGAGCCGGTTTTAAATTTTCTTCCTGTACCGTTCCAATTTGTTACTATCAGTAAACTCCCCCTTAGTCACCGTATTATTGGAAAAAAGTGTTCCTGTAAATATTTGTTATCAATTTTGAAATGTTGCGTATGTATAAATAACATCTTTTTTGACCGTTTTAATCATTGCGTTTCAAAATTTCAATTTCTAAATATTCAAATATTTTCAGGTCAACTAAAACTCTAAGGCGCACGAGCAATGCGCTCAAAACATGTGCTGTACATAGCTATACTGTTCAGTTCAATTTTTGGAGGGAAAGGTGAGTGGAATTACGTGGCCTAGAAAACCTCCTGACCTAGAATTTATTCCACATAGCTAAGACTAGGCAAAAAAATATTTAAAAATGGGTGGCCTAGAAATATCGTTTTTTATAAGCAGGCAAATTGCATGATCGGTGCCGTCATGGTCTAGGTTGTTGGATGACCAAAAAAATTCCTTTCGGAGGACCGGGTGGAAAATTTGTCAACAGAGCGGACCTGCTATCTTAAATGTTTAAGAGGCTTTTGATCTTGAGCCGATCTTTGAAAATGTGTTCAAGATCTGTTCAAATAGTAGCTGATTTCTTGTAAAGAGAGACTAATTGCAAACAGTTAAGGAAGATGGACACCAAGTGCGCTATATTGATAATTTTTGGAATAGCTCAATTGAACGTGTCTGTACTATTTTCTGTGCTAGATTTTCAAAATGTTAGGTTAAAAATGAATGGGATAAAAATTACAAAAAAATGTTCAAAAATTCTCAAATTGCGTATTTCAAAACTTCAAATTCCAAACAAAAATTTTCCTTGTCCGCAACATTTCTGCCCCTCCAAAATTTCAAAATCACTGATAGCTGTTTACTGATAAGCTCTGTGTGCCACCCGGTGTCTGTGTTCTTTTTCATAAAAATCACATAGTTTACCTAAGAAAGTGTTCATGTTTACACCTAAATAACAAAATGTGTATCTTTCGAATTTCAACAAAGTGGTGGTTTCCCAACCAATTTTGGAAAAATTCCTGAAATTCCCGAGTTATCAGGAACAATTTCCTGTTTTACTGACCTTGCCATCGTCGCCCAATACAAGAAAAAGGATAAAATGTACAAAAAATAGGCAAACAAACAGAATAAATATAGGTGCGAAAATGATACGAAAATAATTGTTTCGGGTGGCGGGGCAAATGTTTGCTCTGCTCCGCTACTGACCGGAAATTTGCGCGTTCAGTGAGAAAATGCACGAATCGGTGTGAAAATGTAGTGAAGGGAGCATGTGTGACCTAGAAATTTCAATAAGGAACCTAGGCCATCATATAGATTTTGGTGGCCTGGAAATCAAAAACTCGTAACATTTATCTTTTCAGGAATCCAACAAAATGAGGAATTTCAAAGATACGACGGATGGTACAACAATCTGGCGAATAGTGAATGGGGTTCTGCTGGTAGGTTTTTTCGGAAGAGAAATGACGTTACATTGACCTACTCCTTCAGGAAGTCGGCTGCATAGAGATGCACGTTCCTACTACTCAGACGGTGTATATTCAGTGAATAACTCACTTCCGTCCGCCCGTGAACTCTCCGATATACTATTCAAAGGAGAGTCCGGTATACCTAATACAAGAGGATGCACGACTTTATTGGCATTTTTCAGTTCGTTTTTATTGCCCTCTACCTCAAAAATTAGTAATAATAATTATAGGTCAAGTAGTTGCTTATGAAATAATGCAATCAAATGGAGTATCCTGTCCACTAGAGACACTTAAAATTCAAGTACCCCTATGTGATAATGTATTTGATAAAGAATGTGAGGGAAAGACAGAAATCCCATTTACACGTGCCAAATACGATAAAGCAACTGGAAATGGGCTCAACTCACCTCGAGAACAAATCAATGAACGGACTTCATGGATTGATGGATCATTCATCTATGGTACCACCCAGCCATGGGTGTCCTCATTAAGATCTTTCAAACAAGGGCGGTTGGCTGAAGGTGTACCTGGATATCCACCACTTAACAACCCACATATTCCATTGAATAACCCCGCTCCGCCACAAGTACATCGATTGATGAGTCCAGATAGATTATTTAGTGAGTTCATAGTTTTATAGAAAAGTATAAATATTTAAACTTGAAGTGTTGGGAGACTCGCGTGTGAATGAGAATCCAGGTCTTCTCTCATTTGGTCTGATCCTCTTCCGTTGGCATAACTACAATGCAAATCAAATCCATCGAGAACATCCTGACTGGACAGACGAACAAATCTTCCAGGCAGCACGTCGTTTGGTGATTGCATCTATGCAGAAGATTATTGCATATGACTTTGTTCCAGGGCTGTTAGGTTAATCAACTATATTATAATACCTTAAACTCAGTGTTTCTTTTAAGGTGAAGACGTTCGTTTGTCAAACTACACCAAATACATGCCACATGTTCCACCTGGAATCTCGCATGCTTTTGGAGCAGCCGCCTTCAGGTTCCCTCACTCAATTGTGCCACCAGCAATGCTTCTGAGAAAACGAGGAAATAAATGTGAATTCCGGACGGAAGTTGGTGGATATCCTGCATTGAGATTGTGCCAGAATTGGTGGAATGCGCAGGATATTGTAAAGGAGTACAGTGTGGATGAGATTATTCTTGGTTAGTTCATGCTTGAGTGGTTATATAATAAAGGTTGTAATTTCAGGAATGGCAAGCCAGATAGCTGAACGAGATGATAACATAGTAGTTGAAGATCTTCGTGATTACATCTTCGGACCAATGCATTTCTCTCGTTTGGATGTTGTTGCTTCATCAATAATGAGAGGAAGGGACAATGGAGTACCACCGTATAATGAATTGAGAAGAACATTCGGACTTGCGCCAAAGACATGGGAGACAATGAATGAAGACTTTTACAAGAAGCATACTGCAAAGGTGGAGAAGTTGAAAGAGTTGTATGGAGGCAATATTTTATATTTGGATGCTTATGTAGGAGGGTTAGTTTTGGGTTTAAAGTGGAATGCTTAACTTAAAATGCGGTGAATTCGAAGAGTTTCAAGCAAAAACAATGAAAATCAATTCGTTTTAACATAACTGATTGGTTTAAGAAGTGTGGAATTTTGAATATTCACTAAATCTTCTCAAGGGTTAAAAAGTTCTCACGAGTAAACTTCTAACGGCTTCTTTTGGTCAAACTCTAAAATTTGTAGCAGGCATAAACTCTGGAAGTTGTATGTCACCTCAGTTTTATAGTGCAATTCCTTCGGTATTTCAAACGTTACCCATGCAAGGTAGTTTTTTTTGCAAATCTAGGCAGAATAAATTACGCATACTTGTTTCTTTCTCAGTGCACATATATTGGATTACGTTAATCAAACGTTATTATTTTAGAATGCTGGAAGGAGGTGAAAATGGGCCTGGAGAGTTGTTCAAAGAAATCATAAAGGATCAATTCACCCGTATTCGTGATGGAGATAGATTCTGGTTTGAGAATAAATTGAATGGATTATTCACTGATGAAGAAGTTCAAATGATTCATAGTATTACACTTCGAGATATTATCAAAGCAACCACCGATATCGATGAGACAATGCTTCAGAAGGATGTAAGTTACTTTCCAAATTTAATGGTTTATTATTATGTTCTTTTGAATTCCGCATTGCAATGTATTTATCACTCCAGGTATTCTTCTTCAAGGAAGGTGACCCGTGCCCGCAACCATTCCAAGTGAACACAACTGGACTTGAACCATGTGTTCCATTTATGCAATCAACTTATTGGACTGATAATGACACCACTTATGTTTTCACCCTAATTGGATTAGCATGTGTGCCATTAAGTGAGCTATTGCATCTAGTTCCATACAAACCAAAATGCTTTCAGTTTGCTATGGAATTGGCCGATACTTGGTTAATCGTCGCATTGCTATTGGCCACAACAGTGCTTGTGACAGCCTAACTACTGACTTTGCAAATGATGATTGTGGCGCGAAGGGAGATATTTATGGTGTAAATGCTTTGGAATGGCTTCAAGAAGAGTACATACGACAGGTCAGGATAGAAATAGAAAACACCACGTTGGCAGTAAAGAAGCCACGCGGTGGAATCCTTCGAAAAATTCGTTTTGAAACTGGACAGAAGATTGAGTTATTCCACTCTATGCCGAATCCATCAGCAATGCACGGACCATTTGTACTTCTGTCTCAAAAGAATAATCATCATTTGGTGATAAGATTGTCGTCTGATAGAGATTTATCTAAATTTTTGGATCAAATTAGACAGGCGGCTAGTGGAATCAATGCAGAGGTTATCATAAAGGATGAGGAGAATTCTGTGAGTTTACTTCAAGAAATACGTTGAATCTGGAAATTATTTCAGATTCTCTTATCCCAAGCAATCACAAAAGAACGCCGTCAAGACCGACTGGACCTGTTCTTCCGTGAAGCCTACGCAAAAGCATTCAATGATAGTGAACTTCAAGATTCGGAAACTTCATTTGACTCATCAAATGATGATATATTAAATGAGACAATATCTCGTGAGGAACTGGCAAGTGCAATGGGAATGAAAGCGAATAATGAGTTTGTGAAGAGAATGTTCGCGATGACTGCAAAACATAATGAGGATTCGCTCAGTTTCAATGAGTTTTTGACAGTCTTGAGAGAGTTTGTTAATGGTGAGTATTTCAGCATAAATTTGTTGTGATACAAAGACTACGTTCTAGAATGTTCCGGCGTGTTTCCCATTAACATAAGTTCTAATTGAATAAATATAATTTCTTAATGCAGCTTAATTACGTGTAACAGCAGTAGCGGTAAAGTTGTTTTGAACTGTCTTTGATTTTGTACGTACAAAACTACATATAAAAGGTTTTGGTTCAAGAGAGCCGAAGTCTCCTGCGAAAAGAAATTTATTTCTTCTGATCTGAATTTAAACTAGGCCGGGATTAGCGACCGATTAACATTTTGTAGGTTCATTAGCCGTGAGGTGAAACTCGGTGTCCTATGGTCGGCAATATTTCGAGATAGTAAAAGTTCTAAAGGTTATTTATTCTGAATCTGAATTTATTCGGGGGAGTCCTATAGAATTTGCGAGCACTGTAGAAAGTTCTCGTGTGACAGGGAGGTCACAACTAATATGGCATCAAAGTATTGAGAATTTAGTCAATTGTAGATTTTCTTTTACTGAACAGTAGAAAAACCAACACTGCCTTTAAAAAATGTTATGCACCACCTACTTTAATTTCCAGCTCCTCAAAAGCAAAAACTGCAAACTCTATTCAAAATGTGTGATTTGGAGGGAAAGAACAAGGTACTCCGAAAGGATCTCGCGGAACTCGTCAAGTCCCTCAATCAAACCGCTGGAGTTCACATTACTGAAAGTGTGCAGCTTCGATTATTCAATGAAGTGTTGCACTATGCAGGAGTGAGCAATGATGCCAAGTACCTGACTTACGACGATTTCAATGCTCTGTTCTCGGATATACCTGACAAGCAACCAGTTGGACTGCCGTTCAATCGAAAGAACTATCAGCCAAGTATTGGAGAGTGAGTATTCAGGAGGACTCTGACTGTATAACAATTATAACTTTTAGAACATCTTCTCTGAACTCATTTGCCGTCGTGGATCGATCCATCAACAGTTCAGCACCGCTAACTTTGATCCACAAAGTTTCAGCGTTCTTGGAGACCTATCGCCAACACGTTTTCATTGTCTTCTGCTTTGTTGCCATCAATCTTGTTCTTTTCTTCGAACGGTTTTGGCGTAAGTTCATATAATTGGGAGCTCATGTTAATTTAGTTTTCAGATTATCGTTACATGGCGGAAAACAGGGATCTCCGACGAGTAATGGGAGCTGGAATCGCTATTACTCGTGGTGCCGCGGGAGCCTTGTCATTTTGCATGGCGTTGATATTGCTGACAGTTTGTAGAAACATAATCACACTTCTTCGAGAGACAGTCATTGCGCAGTATATTCCATTTGACTCGGCTATTGCGTTCCACAAGGTGAGAAACGTTAGGGCAGCGTGTAACACATTTTTTAAATATTATTATTGCATTAGTAAATTTTGTCAAATCAGTTGTTTTTAAAAATATTTAGCATGTTCAGATATAAGGGAAAACTTGTTATTTTATTATCTGTACAGTAATGCGGAGGTTTAATGCAAGTAGGATAACTGTACTGTGCATACCCAATGTTTTGAAAAGATTTTTTAAAATAGAATACAAGCATGAAAGGAAAGATCTTTGCATCGAACATGGTGTTTCTCAGCCAGATGTGAACTTATGATATAGCGATGTTATCCTAAACTTGTAAGTGTTTAATTTTTTTAAATTTATTACGATAGTAAGATATCGTGAGGTAGAAAAAAAACACACATTAATAGATACAAACCATCACAAGTGGTTACATAAATAAAAATGGAACAAAAATAAAAAGAGATGAGAAAAAAAATAATGGCTACATTGGAGAAGAAGCAAAAAACACAAATATCGATGTATAAAAGGCAAGAATAAATGATGAATAGAAGTGAGGATAAGGTAACATTAGATCAGTGTTGCTTCATTGTGTGTAGTGTTCTGTTGACAAAAAAGTGTCTCCTAAGTTTAGATTTTCCTGTGCTCCAGATATATTTCTTTTTAGAACGAGTGTGGGTCTCTTGTTGCTCAAAAAACTCAGATGTTTTTAAGTCTACTTTACATATAAGTGTTCTGTAGAGAGGGCAGATTTTTGAATAAAAAAATAAACTATGATAAACAATGGGAAAACTAATATTTCGGACAAAGTATTGTTTATTATGACCGCCAGTATCAAAAACTCTATAATAACTGAACATTTCTAGATCGTTGCGCTCTTTGCGGCTTTCTGGGCCACTCTTCACACCGTTGGACATTGTGTCAATTTCTATCACGTTGGAACTCAAAGTCAAGAAGGTCTTGCTTGTCTCTTTCAGGAAGCATTCTTTGGGTAATACTTTACTTGAATTCATTTTTGCATTCAATCTTACTAGAATACGCACCATTAACAAACTCCCTCAAGACTGTCAACAACTTTCATCAAATAACTTTCAGATCCAACTTCCTTCCTTCAATCAGTTACTGGTTCTTCAGCACAATTACAGGTCTGACAGGAATTGCATTGGTCGCTGTCATGTGCATCATTTATGTTTTCGCGTTACCATGTTTCATTAAGAGAGCTTATCACGCATTCCGGCTCACACATCTTCTCAATATTGCCTTTTACGCACTTACTCTTCTTCATGGGCTTCCAAAGTTGTTGGATGTGAGTTTTTGCCACTGTTCGGTTCAAGAAGTTTCTTCAATATTTGTTACAGTCTCCCAAATTTGGCTACTACGTTGTTGGTCCCATCGTGTTATTTGTAATTGATCGCATAATTGGTTTGATGCAATATTACAAAAAATTAGAAATTGTAAACGCAGAAATCCTTCCATCAGATATTATATACATCGAGTACCGTCGTCCAAGAGAGTTTAAATATAAATCAGGACAATGGGTTACTGTATCATCACCATCAATATCATGTACCTTTAATGAATCTCACGCATTCTCGATTGCCTCAAGTCCACAGGATGAGAATATGAAGTTGTATATAAAAGCAGTTGGACCATGGACATGGAAGTTGAGAAGCGAATTGATAAGATCATTGAATACAGGATCGCCATTTCCATTAATCCATATGAAAGGACCATATGGTGATGGTAACCAAGAATGGATGGATTATGAAGTTGCAATAATGGTTGGAGCAGGAATCGGAGTGACTCCATATGCATCGACACTTGTTGATCTTGTACAACGAACATCAAGTGACTCATTTCACAGAGTTCGTTGCCGTAAAGTATATTTCCTATGGGTGTGCTCAACTCACAAGAACTATGAATGGTTTGTGGATGTGCTCAAGAACGTGGAAGACCAAGCAAGGTCGGGAATTTTGGAGACACATATCTTTGTCACTCAGACGTTCCACAAGTTTGATTTGAGAACTACTATGCTTGTGAGTTTATTGAAGATAATTTTCAAAATCAAACGTCAGGTTTGGTTATAAACTGATTAAAGCGGACGCATTTAAACGCAGTGGCATCTTAAGGTCTGAAGCTTTTAAACTTTAACATCTTATTTGCAGTACATTTGCGAGAAGCACTTCCGTGCCACCAACTCAGGAATTTCAATGTTTACTGGTCTCCACGCTAAGAACCATTTCGGACGGCCCAACTTCAAAGCTTTCTTCCAATTTATTCAGAGTGAACATAAGGAGGTTAGTTAAATGCTTTTTAACCTCTAAATAAAGCAAATTTGCAGCAATCCAAAATCGGAGTGTTCAGTTGTGGACCTGTAAACTTGAATGAAAGTATAGCTGAAGGATGTGCAGATGCCAACCGACAACGAGATGCTCCTTCATTTGCACATCGCTTTGAAACGTTCTAACCTTCCCTATATCATCATTATTATACATATTTTATGCTTCTTTGAGTATTCTGTGCCAGCTTTACATTTTCTGTCTAGACTTCATTTTTTTTCATTCACTGTTTTATGGGTAACAACAACAATGACTTTTAATTTTGAATAGATGTATATACAACTAAAAAGAAACAGCTCCTCCGAATAGGCTCCGCTTGTCGAGACCGGCAATTGAACGTGAGGCGGCGGTGGAGTAGAACTGGAAAAATAGGAAAAGCTTGTTGGAAGTAAGAAGTTGTGACTAATCAATAATTAGGGCCTATGCCTTGGGTATTTGGGTGTACATCTCTGATGAATCTAAATTTTTTTGGAATCATCGCTAGTAACCTTTCTCTACAATATTCATATTATGAAATACCGACCTTGTAATCAGGCTTGTCACTTTTTCGTTTTCGAATTTTCGTTTTTTCGTTATTTTCGGGTTTTTGGCGAAAATGATTTTTTCGTTTTCGTTTTCGAAAATTT"
# sequence = "TATTAGGTCTATGGAAGCCTAAGTTAAAAC"
list_sequence = list(sequence)

# model : to be discussed
# log values!
log_start_probability = {"N" : math.log(0.91), "E1" : math.log(pow(10, -30)), "E2" : math.log(pow(10, -30)), "E3" : math.log(pow(10, -30)), "I1" : math.log(0.03), "I2" : math.log(0.03), "I3": math.log(0.03)}
# start_probability = {"N" : 0.91, "E1" : pow(10, -30), "E2" : pow(10, -30), "E3" : pow(10, -30), "I1" : 0.03, "I2" : 0.03, "I3": 0.03}

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


def viterbi_w(obs, states, log_start_p, trans_p, emit_p):
    logV = [{}]
    for st in states:
        logV[0][st] = {"log_prob": log_start_p[st] + math.log(emit_p[st][obs[0]]), "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        logV.append({})
        for st in states:
            log_max_tr_prob = logV[t - 1][states[0]]["log_prob"] + math.log(trans_p[states[0]][st])
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                log_tr_prob = logV[t - 1][prev_st]["log_prob"] + math.log(trans_p[prev_st][st])
                if log_tr_prob > log_max_tr_prob:
                    log_max_tr_prob = log_tr_prob
                    prev_st_selected = prev_st

            log_max_prob = log_max_tr_prob + math.log(emit_p[st][obs[t]])
            logV[t][st] = {"log_prob": log_max_prob, "prev": prev_st_selected}

    for line in dptable(logV):
        print(line)

    opt = []
    log_max_prob = 0.0 - math.inf
    previous = None
    # Get most probable state and its backtrack
    for st, data in logV[-1].items():
        if data["log_prob"] > log_max_prob:
            log_max_prob = data["log_prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    # Follow the backtrack till the first observation
    for t in range(len(logV) - 2, -1, -1):
        opt.insert(0, logV[t + 1][previous]["prev"])
        previous = logV[t + 1][previous]["prev"]

    print ('The steps of states are ' + ' '.join(opt) + ' with highest log - probability of %s' % log_max_prob)

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["log_prob"]) for v in V)

def viterbi_w_g(states, log_start_p, trans_p, emit_p, gfa_file, segment_id):

    obs = list(gfa_file[0][segment_id - 1][1])

    logV = [{}]
	
    for st in states:
        logV[0][st] = {"log_prob": log_start_p[st] + math.log(emit_p[st][obs[0]]), "prev": None}
    
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        logV.append({})
        for st in states:
            log_max_tr_prob = logV[t - 1][states[0]]["log_prob"] + math.log(trans_p[states[0]][st])
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                log_tr_prob = logV[t - 1][prev_st]["log_prob"] + math.log(trans_p[prev_st][st])
                if log_tr_prob > log_max_tr_prob:
                    log_max_tr_prob = log_tr_prob
                    prev_st_selected = prev_st

            log_max_prob = log_max_tr_prob + math.log(emit_p[st][obs[t]])
            logV[t][st] = {"log_prob": log_max_prob, "prev": prev_st_selected}

    # for line in dptable(logV):
    #     # print(line)
    #     pass

    opt = []
    log_max_prob = 0.0 - math.inf
    previous = None
    # Get most probable state and its backtrack
    for st, data in logV[-1].items():
        if data["log_prob"] > log_max_prob:
            log_max_prob = data["log_prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    # Follow the backtrack till the first observation
    for t in range(len(logV) - 2, -1, -1):
        opt.insert(0, logV[t + 1][previous]["prev"])
        previous = logV[t + 1][previous]["prev"]

    # print ('The steps of states are ' + ' '.join(opt) + ' with highest log-probability of %s' % log_max_prob)
    
    end_state_log_prob = []

    # print(logV[-1])
    for st in logV[-1].items():
        # print(st[1]["log_prob"])
        end_state_log_prob.append(st[1]["log_prob"])

    print(tuple(end_state_log_prob))



# viterbi_w(list_sequence, states, log_start_probability, transition_probability, emission_probability)