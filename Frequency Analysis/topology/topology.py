# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:30:21 2021

@author: JOHN WARUTUMO
"""

'''
I think I now have a general flow for processing series for topologies. One flow we could follow is:
    Given a series, test to see it's a topology. If this first time test is positive (i.e. it's a top), flag the series -->
    Discretize and test if series is topology. If test outcome is positve, give a 2nd grade flag, or a flag whose value is lower than that of the first test.-->
    Create topology through intersections and unions.
    The process can be summarized in a schematic as below. ``^`` denotes path after evaluation of test if true. 
    
    
                    Flag                      Flag
X = {1,2,7,8,...} ---^---> discretize --> top? ^ --> form top

{202102080326:above notion was erroneous. First the set members (or the members of the series comming in) would have to be placed in subsets. a topology is described only over a set. We may subset the incoming series and after determining a collection of subsets belonging we can 《word topology is used with the assumption that a collection of subsets over X yield a topology - this isn't always the case and that is what we are about to test》 test whether its a topology. 《Strained logic here》n
A more correct notion would be
    
    
                                                   Flag
X = {1,2,7,8,...} --> discretize --> subset --> top? ^ --> form top
}
{202102100437: I think my beginner's mind was a little different from now - am not an expert but the point is my view and perception has changed. For example, I have doubts as to whether a discretized series would form a series without additional processing done on it. This is especially true if the series has multiple discrete levels being present since this means a lot of unions won't be represented without the series being processed into subsets. What I mean is if the series is X = {1,2,7,8}, {{1},{2},{7},{8}} doesn't form a top since the unions of arbitrary elements are missing. ΔLooking at the sentences in the first 4 lines of commentsΔ A good thing would be to decide upon a criterion of subsetting. This may be:
     Subsetting one member by one member.
     Subsetting two members whenever possible.
     Subsetting 3 members whenever possible.
     ...
     
For example, given 
array([ 8,  2,  4,  9,  1,  8,  4,  5,  5,  6,  2,  2,  1,  3,  7,  9,  2,
        7,  1,  6,  1,  9,  5,  4,  8,  6,  6,  3,  3,  1,  5,  9,  2,  3,
        7,  1,  3,  3,  2,  3,  1,  9,  1,  5,  9,  5,  8,  7,  7,  2,  5,
        1,  2,  1,  2,  4,  9,  7,  9,  5,  6,  6,  5,  9,  2,  3,  8,  3,
        7,  4,  4, 10,  2,  9,  4,  2,  8,  3,  4,  8,  6,  4,  6,  4,  2,
        3,  2,  5,  2,  9,  2,  1,  9,  3,  4,  2,  8,  3,  2, 10],

subsetting to one member whenever possible is relatively easy.
array([[8], [2], [4], [9], [1], [8], [4], [5], [5], [6], [2], [2], [1],[3], [7], [9],[2], [7], [1], [6], [1], [9], [5], [4], [8], [6], [6], [3], [3], [1], [5], [9], [2], [3], [7], [1], [3], [3], [2], [3], [1], [9], [1], [5], [9], [5], [8], [7], [7], [2], [5], [1], [2], [1], [2], [4], [9], [7], [9], [5], [6], [6], [5], [9], [2], [3], [8], [3], [7], [4], [4], [10], [2], [9], [4], [2], [8], [3], [4], [8], [6], [4], [6], [4], [2], [3], [2], [5], [2], [9], [2], [1], [9], [3], [4], [2], [8], [3], [2], [10]], dtype=int64)}
      
The resulting series has not union of any two member of itself.
Subsetting two by two can also be done, keeping in mind that the members of a subset are unique wrt each other.
'''
'''
returns subsets of N units whenever possible from a stream of data
'''
def subset(n,units=3):
    L = []
    l = []        

    for x in n:
        if len(l)>=units:
            L.append(l)
            l = []
            l = [x]
        elif x in l:
            L.append(l)
            l = []
            l = [x]
        else:
            l.append(x)
    L.append(l)#append the very last l since its not appended in the loop
    return L
'''
I've noticed that a very good way of confirming that a method of function works correctly is through testing. For example I noted that an initial version of    ``subset`` function was leaving out values by inspecting the values of initial array. By observing that the numbers were skipped at regular intervals I came to the conclusion that some sytematic error was being made by the computer. That is one such mistake I easily get from inspecting the output and input. There is less likelihood of error if the method I'm using for feedback is highly trusted... ie I trust that a number I've seen a second ago is still the same number and hasn't changed while I looked away. In the context of discovering the mistake, what I mean is that I'm certain that a number is missing from a position I wish to have it.

The second error was encountered when for no obvious reasons but an abiding curiousity to test out a piece of code I wrote the following

>>> s = subset(n,2)
>>> [x for l in s for x in l]

and discovered that ``len(s)`` and len([x for l in s for x in l]) differed when they should have been the same. the second expression meerely flattens out the list so we can count all the single members of the series. the discovery by inspection was that the last two numbers were missing, which gave me the idea that the last small list wasn't being added to the big one.

For subsetting a series into fixed length subsets whenever possible has some interesting things of note:
Given n = 
array([ 8,  2,  4,  9,  1,  8,  4,  5,  5,  6,  2,  2,  1,  3,  7,  9,  2,
        7,  1,  6,  1,  9,  5,  4,  8,  6,  6,  3,  3,  1,  5,  9,  2,  3,
        7,  1,  3,  3,  2,  3,  1,  9,  1,  5,  9,  5,  8,  7,  7,  2,  5,
        1,  2,  1,  2,  4,  9,  7,  9,  5,  6,  6,  5,  9,  2,  3,  8,  3,
        7,  4,  4, 10,  2,  9,  4,  2,  8,  3,  4,  8,  6,  4,  6,  4,  2,
        3,  2,  5,  2,  9,  2,  1,  9,  3,  4,  2,  8,  3,  2,  2],
      dtype=int64)

subset(n,6) == subset(n,7) == subset(n,8) == subset(n,9) == subset(n,10) == subset(n,10)

Attempting to subset the array for any N > 5 returns the same results. Queer indeed... but I think favorable explanations may lean on the fact that the numbers of ``n`` were randomly generated and that they lie between 1 and 10.

##Other way of creating subsets.
Creating fixed-length subsets whenever possible has been tackled. What of the case where many subsets of any lengths are admissible? A combination of subsets of different lengths is also a sound supposition as we know nothing about the behaviour of the data series or it's flow on the topology we're investigating.
}
'''
import numpy as np
'''
get the series
function returns a random stream of N numbers whose values are between mn and mx
'''
def getStream(mn=0,mx=100,N=100):
    return np.random.randint(mn, mx, N)
'''
discretize a stream
'''
def discretize(n, bins=np.linspace(0,10,11)):
    bins = np.linspace(n.min(),n.max(),10)
    return np.digitize(n,bins)

'''
create subsets
'''
def subset(stream):
    L=[]#empty list to contain the set of subsets
    l = [stream[0]]#stream is the discretized series of values
    
    for x in stream[1:]:
        if x in l:
            L.append(l)
            l = [x]
        else:
            l.append(x)
    return L
'''
test if set of subsets forms a top
'''
def isTop(Ll):
    L = list.copy(Ll)
    L = makeSet(L)
    L = sortSubsets(L,axis=1)
    if unisPresent(L) & intsPresent(L):
        return True
    else:
        return False
'''
check if any intersection of subsets is missing
'''
def intsPresent(L):
    for l0 in L:
       for l1 in L:
           l = list(set.intersection( set(l0), set(l1) ))
           l.sort()
           if l not in L:
               return False
    return True
'''
check if a union of any two subsets is missing
'''
def unisPresent(L):
    for l0 in L:
       for l1 in L:
           l = list(set.union( set(l0), set(l1) ))
           l.sort()
           if l not in L:
               return False
    return True
'''
sort subsets. Is sorted in axis 1 (the second axis), only the elements inside any subset are sorted. The order of the subsets isn't affected. If axis is zero, the order of subsets changes depending on the first value of each subset.
'''
def sortSubsets(L, axis=0):
    def sort1():
        M = []
        for x in L:
            n = np.array(x)
            n.sort()
            M.append(list(n))
        return M
    
    if axis ==1:#sorts the second axis
        return sort1()
    elif axis ==0:#sorts the first axis, ie, the subsets
        return sorted(L)
    elif axis ==-1:#sort both axis
        return sorted(sort1())
'''
given a collection of subsets, return a set. the null set is included in new set.
'''
def makeSet(Ll):
    M = [[]]
    L = sortSubsets(Ll,axis=-1)
    
    for l in L:
        if l not in M:
            M.append(l)
    return M
'''
make a topology given a collection of subsets. 
💢《I feel as though this looping through the subsets twice is quite inefficient and I should seek help in optimizing for performance》
'''
def makeTop(L):
    Ll = L
    while not isTop(Ll):
        Ll = makeSet(Ll)#sorts both axis and makes it collection a set

        for l0 in Ll:
            for l1 in Ll:
                I = list(set.intersection( set(l0), set(l1) ))
                I.sort()
                if I not in Ll:
                    Ll.append(I)
                    
        for l0 in Ll:
            for l1 in Ll:
                U = list(set.union( set(l0), set(l1) ))
                U.sort()
                if U not in Ll:
                    Ll.append(U)       
                    
                    
        return Ll
    
'''
worth noting that creating the top from the collection {{},{1},{2},{3},{4}} creates the powerset.
'''