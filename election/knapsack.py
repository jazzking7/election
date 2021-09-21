# Author: Jasper Wang
# Date: 20 Sep 2021
# Goal: calculate minimum votes needed to win an election using 0-1 knapsack
import sys
def getminvotes(data):
    winquota = gettotalweight(data)//2+1
    weight_and_score(data)
    i = 0
    return knapsack(data,winquota,i)

def knapsack(data, winquota, i):

    if winquota <= 0:
        return 0
    if i == len(data):
        return sys.maxsize
    return min(int(data[i][1]) + knapsack(data,winquota-int(data[i][0]),i+1), knapsack(data,winquota,i+1))


def gettotalweight(data):
    result = 0
    for state in data:
        result += int(state[0])
    return result

def weight_and_score(data):
    for state in data:
        state[1] = getminscore(int(state[1]),int(state[2]),int(state[3]))

def getminscore(myvotes,oppositionvotes,undecided):
    diff = oppositionvotes-myvotes
    if diff == 0:
        return sys.maxsize if undecided == 0 else undecided//2 + 1
    elif diff > 0:
        return sys.maxsize if undecided <= diff else ((undecided - diff)//2+1) + diff
    else:
        return 0 if undecided < -diff else (undecided+diff)//2 + 1
