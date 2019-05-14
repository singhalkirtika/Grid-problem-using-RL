# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# 1 DOWN
# 2 UP
# 3 Right
# 4 Left
import numpy as np
import sys
from operator import add

# %%
stateTransition = [[-1,3,1,-1],
                 [-1,-1,2,0],
                 [-1,5,-1,1],
                 [0,6,-1,-1],
                 [1,7,5,3],
                 [2,8,-1,-1],
                 [3,9,7,-1],
                 [-1,10,8,6],
                 [5,11,-1,7],
                 [6,-1,10,-1],
                 [7,-1,11,9],
                 [8,-1,-1,10]]
r = 1
R = [[-sys.maxsize,r,r,-sys.maxsize],
    [-sys.maxsize,-sys.maxsize,r,r],
    [-sys.maxsize,r,-sys.maxsize,r],
    [r,r,-sys.maxsize,-sys.maxsize],
    [r,r,r,r],
    [r,r,-sys.maxsize,-sys.maxsize],
    [r,r,r,-sys.maxsize],
    [-sys.maxsize,-1,r,r],
    [r,1,-sys.maxsize,r],
    [r,-sys.maxsize,-1,-sys.maxsize],
    [r,-sys.maxsize,1,-sys.maxsize],
    [r,-sys.maxsize,-sys.maxsize,-1]] 

action = [[0,1,1,0],[0,0,1,1],[0,1,0,1],[1,1,0,0],
         [0,0,0,0],[1,1,0,0],[1,1,1,0],[0,1,1,1],
          [1,1,0,1], [1,0,1,0],[1,0,1,1],[1,0,0,1]]

discountFactor = 0.8

policy = [0 for i in range(12)]

# %%
def transition(T, s, a):
    p_move = 0.8
    sExpected = []
    prob = []
    actions = []

    if T[s][a] != -1:
        sExpected.append(T[s][a])
        prob.append(p_move)
        actions.append(a)
        
    if a < 2:
        if T[s][2] != -1:
            sExpected.append(T[s][2])
            prob.append((1 - p_move) / 2)
            actions.append(2) 
            
        if T[s][3] != -1:
            sExpected.append(T[s][3])
            prob.append((1 - p_move) / 2)
            actions.append(3)
        
    else:
        if T[s][0] != -1:
            sExpected.append(T[s][0])
            prob.append((1 - p_move) / 2)
            actions.append(0)
            
        if T[s][1] != -1:
            sExpected.append(T[s][1])
            prob.append((1 - p_move) / 2)
            actions.append(1)
            
    return sExpected, actions, prob

# %%
VS = [0 for i in range(12)]
prevVS = [1 for i in range(12)]

while VS != prevVS:
    VS = prevVS
    actionsTaken = []
    for i in range(12):
        possibleActions = [k for k in range(4) if action[i][k]!=0 ]
        values = []
        for j in range(len(possibleActions)):
            sExpected, actions, prob = transition(stateTransition, i, possibleActions[j])
            reward = [R[i][a] for a in actions]
            expected = [discountFactor*VS[k] for k in sExpected]
            innerValue = [a+b for a,b in zip(expected, reward)]
            action_value = sum([a*b for a, b in zip(innerValue, prob)])
            values.append(action_value)

        if len(values)>0:
            prevVS[i] = max(values)
            actionsTaken.append(possibleActions[values.index(max(values))])
        else:
            actionsTaken.append(-1)


# %%
print(VS)

# %%

