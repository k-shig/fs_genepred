#!/usr/bin/env python
# -*- coding:utf-8 -*-

states = ("Rainy", "Sunny")
observations = ("walk", "shop", "clean", "walk", "shop", "clean")
start_probability = {"Rainy" : 0.6, "Sunny" : 0.4}
transition_probability = {
    "Rainy" : {"Rainy" : 0.7, "Sunny" : 0.3},
    "Sunny" : {"Rainy" : 0.4, "Sunny" : 0.6},
    }
emission_probability = {
    "Rainy" : {"walk" : 0.1, "shop" : 0.4, "clean" : 0.5},
    "Sunny" : {"walk" : 0.6, "shop" : 0.3, "clean" : 0.1},
    }

def print_dptable(V):
    print("         ", end = "")
    for i in range(len(V)):
        print(i, end = "      ")
    print("\n")

    for st in V[0].keys():
        print(st, end = " ")
        for ob in range(len(V)):
            print('{:.10f}'.format(V[ob][st]), end = " ")
        print("\n")

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # initialize base cases
    for st in states:
        V[0][st] = start_p[st] * emit_p[st][obs[0]]
        path[st] = [st]

    # run viterbi for t > 0
    for ob in range(1, len(obs)):
        V.append({})
        newpath = {}

        for st in states:
            (prob, state) = max([(V[ob - 1][st0] * trans_p[st0][st] * emit_p[st][obs[ob]], st0) for st0 in states]) 
            V[ob][st] = prob
            newpath[st] = path[state] + [st]

        path = newpath
    
    print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][st], st) for st in states])

    # opt = []
    # max_prob = 0.0
    # previous = None
    # # Get most probable state and its backtrack
    # for st, data in V[-1].items():
    #     if data["prob"] > max_prob:
    #         max_prob = data["prob"]
    #         best_st = st
    # opt.append(best_st)
    # previous = best_st 
    # # Follow the backtrack till the first observation
    # for t in range(len(V) - 2, -1, -1):
    #     opt.insert(0, V[t + 1][previous]["prev"])
    #     previous = V[t + 1][previous]["prev"] 
    # print ('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob) 
    return (prob, path[state])

print(viterbi(observations, states, start_probability, transition_probability, emission_probability))