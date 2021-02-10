import numpy as np

#assume binary levels, we need a probability representation for transitions
#between permutations... for reels of length n, we need probabilities of tra
#nsition from each permutation to the others which is a n*n matrix including
#the probability of remaining in its current permutation.

def __init__(n):
    v = int(np.sqrt(n))
    M = np.zeros((v,v))
    return M

def produce_reel(array,pitch,levels):
    #sampling frequency and pitch (duration between pickings)
    f
    z
    #get audio & convert it to array a
    #segment it into portions
    a = np.array( [a[x:x+pitch] for x in range(0,len(n),pitch)] )
    #average over: the time distance between any two entries is the pitch
    a = a.sum(axis=1)
    #produce that sequence of averages
    #assign probability of transition to current row
    #go to the row to which the sequence of averages matches
    