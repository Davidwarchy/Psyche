# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 09:56:06 2021

@author: JOHN WARUTUMO

A program that's part of a project to mate arcane mathematics to analysis of the behavior of world data.
This program aims to test whether data can be worked on as a topology.  %this sounds arcane in itself, me doing maths, but it's what am doing%

Consider a set X = {1,2,3,4} and a collection T which is a collection of the subsets of X. T may be T = {{},1,2,3,{1,2},{2,3}}. If T obeys the following rules, then it's considered a topology: 《don't ask what this is for, or why it's important. what is important is that it is a shot at trying to integrate maths to data, and perhaps to do that in a way that is quick and also lucky - ie it may lead to insights quicker than imagined before》
1. The empty set and X belong to T
2. The union of any members of T is in (or belongs to) T
3. The intersection of any finite number of members of T belongs to T
"""

'''
Tell whether sequence is a topology. 
The empty set is a member of every set. 202102040436: Test the conditions for a topology on X.
'''

import numpy as np

def createTopo(n):
    s = np.unique(n)#create a set.

"""
A power is the set of all subsets of a set. For example the power set of  X = {1,2} is P(X) = {{},1,2,{1,2}}. If a set has n members its power set has 2**n members.

The power set is a topology over a set. (202102040436: In literature the topology created by the power set is called the discrete topology. 《From wikipedia explanation of what a topology is》)
I think the problem with creating a topology from a power set is the massiveness of the size of the set. A set with 10 members has a power set of 2**10 members. If 16 bits are reserved for each member, we quickly run out of memory since 2**10*16/8 = 4GB is quite a big chunk of memory. 202102040559: I may be in error here actually. Refer to another file where I've written code that can test my suppostion. The file is count.py. 《weren't it much better is there could be a way of linking to the file directly so that the logic is followed》. The total number of basic elements for a powerset of 10 members is only 5120, which is actually quite small for a computer even if 64 bits are used to represent a single member... 320kbs.


I think there is a way of creating a minimal topology, or a complete topology using less memory...
《Should I list the problems I encounter while trying to integrate maths with computers... for example the problem of memory quickly running out if we decide to use the power set as a topology - remember what a topology is from our definition》
"""
 
""" Find out whether every intersection of members is also a member"""   
def intersectionsAreMember(s):
    l = list(s)
    N = len(l)
    for x in l:
        #check if each member's intersection with another is also member
        for n in range(N):
            I = set.intersection(set({x}),set({l[n]}))#make each member of list a set itself
            if I in s:
                return False
    return True

""" Find out whether every union of members is also a member"""
def unionsAreMembers(s):
    l = list(s)
    N = len(l)
    for x in l:
        #check if union with other members is also member
        for n in range(N):
            U = set.union(set({x}),set({l[n]}))
            if U in s:
                return False
    return True

def isTopology(s):
    #the empty set meets criteria for a topology but I dont think its of use to us now
    if type(s) != set:
        s = set(s)
    if len(s) == 0:
        print("null set")
        return True
    else:
        return intersectionsAreMember(s) & unionsAreMembers(s)
    
#sets on wikipedia page
#a topology is a set of subsets so it seems to me that they may be represented as T = {{},{1},{2,3}} and not as {1,2,3} whose children members aren't denoted as subsets
tops =  frozenset({1,2,3}),        frozenset({1}), frozenset({1,2,3}),        frozenset({1}),frozenset({2}),frozenset({1,2}),frozenset({1,2,3}),         frozenset({2}),frozenset({1,2}),frozenset({2,3}),frozenset({1,2,3}),        frozenset({2}),frozenset({3}),frozenset({1,2,3}),        frozenset({1,2}),frozenset({2,3}),frozenset({1,2,3})

import pdb
for x in tops:
    print(x)
    if x == {2,(1,2),(2,3)}:
        pdb.set_trace()
    if isTopology(x):
        print("Topology\n")
    else:
        print("Not topology\n")

def intersectionsPresent(s):
    for ss in s:#every subset in s
        pass
    
    
'''
202101301206:
I am exploring how data and information can interact with topology. I've thought that data comes primarily in two forms: ``serial data`` and ``parallel data``. serial data can be from perhaps the temperature of a single location collected once a day for many years. 《One year?》 parallel data may be the temperature from 2 or more locations collected over time. 

how can topology be implemented here? Maybe there is a hidden manner in which some kinds of data may flow along a topology's subset. the order of this flow may follow patterns or may be decipherable via another tool. I imagine some discretized data 《This may be difficult to get for some, but it's a fairly simple concept which can be linked for explanation wrt to our study》 falling into one or more levels. I further imagine that the categories can be serialized... after that they may be subsetted... for example
'''
n  = np.random.randint(0,50,50)#form a stream of 50 values randomly occuring btw 0 and 50
'''
array([43,  7, 41, 10, 38, 19, 22, 45, 24, 15, 12, 21, 16, 21, 25, 19, 17,
       31, 45,  3, 10, 22, 31, 26,  2, 21, 33,  1, 33, 23,  7, 18, 44, 23,
       43, 16, 12, 44, 44,  1, 34,  9, 29, 36, 20,  2, 14, 23, 23, 29])

if we decide to create bins of size 10, the random values can now only take specified values. the specified values are called bins
'''
bins = np.linspace(0,50,6)#6 bins
'''
array([ 0., 10., 20., 30., 40., 50.])

make the serial stream be discrete... the returned values are the bin numbers

'''
stream = np.digitize(n,bins)
'''
array([5, 1, 5, 2, 4, 2, 3, 5, 3, 2, 2, 3, 2, 3, 3, 2, 2, 4, 5, 1, 2, 3,
       4, 3, 1, 3, 4, 1, 4, 3, 1, 2, 5, 3, 5, 2, 2, 5, 5, 1, 4, 1, 3, 4,
       3, 1, 2, 3, 3, 3], dtype=int64)

test potential flow on the topology. put otherwise (meaning another way), can we find distinct topologies 《this is actually weirdly satisfying in some way... maybe it's because of it's fundamentality or maybe I have a clear conceptual grasp of sets. I don't know,...》 《20210204080827: rereading this doesn't quite elicit the same feelings I had earlier and my previous comment seems bland, though I shouldn't assume it meant such at the time of its writing》

basically what we are looking for are subsets through which the flow of data passes. The set under question is X = {1,2,3,4,5} where X is a name we've assigned it so we can latter refer to the set without writing all the numbers. The subsets of X are 《... no maybe just say or describe a set instead of subsets》... ok a subset of X is a unique collection of members of X in any arbitrary number. The subset of all possible subsets of X is usually monikered the Powerset of X. A topology is a set of subsets satisfying the conditions of closure under intersection, closure under union and membership of the nullset & X.

so given the stream above how can we get the subsets being traversed by the stream:
Δoutput of the streamΔ   --> {5},{1,5},{2,4},{2,3,5},{3,2},{3,2},{2,3},....

one way to go about it would be take each number one by one and start forming a subset from it, adding consecutive numbers to the subset until %% the first number is encountered again. 《won't we miss on those that fulfill the criteria for being topologies?《What was I visualizing here? I must have had an idea in mind whose expression wasn't fully made thus making it difficult to decipher my comment. I think I may have meant that the set of subsets obtained from the described algorith may not form a topology. I don' think that's a big problem though as a topology can be formed by adding intersections and unions by the rules of what a topology is.》》 --> 《I think an attempt can be afterwards be made to consider only those sets meeting conditions for being topologies on the set of the stream》
'''

L=[]#empty list to contain the set of subsets
l = [stream[0]]#stream is the discretized series of values

for x in stream[1:]:
    if x in l:
        L.append(l)
        l = [x]
    else:
        l.append(x)
        
'''
%used a proper flowchart, without which I was shooting in the dark. those old fashioned flow charts are quite helpful at crystalizing concepts... 《Lincoln》

[[5, 1],
 [5, 2, 4],
 [2, 3, 5],
 [3, 2],
 [2, 3],
 [2, 3],
 [3, 2],
 [2, 4, 5, 1],
 [2, 3, 4],
 [3, 1],
 [3, 4, 1],
 [4, 3, 1, 2, 5],
 [3, 5, 2],
 [2, 5],
 [5, 1, 4],
 [1, 3, 4],
 [3, 1, 2],
 [3],
 [3]]

That's the result for our subsets.
We can create a function of it
{202102091150: there are many ways of subsetting the stream, including making each membere of the stream a subset or maybe taking the stream members 2 by 2}
'''
'''
we can further order the subsets 《What for?》 --> 《I don't know? Why not order?》... if our consideration is how the stream flows over the topology, then ordering the subset doesn't infact give us a sense of direction or flow. I think a better way would be to not order the subsets, but to order the members of the subsets, to better see what subsets are traversed. 

Δlooking at the array result aboveΔ --> 《It just occured to me that a topology T can be easily made by getting the intersections of given subsets, as well as their unions, and also the union of all of them %X & null% 》
'''
M = []
for x in L:
    n = np.array(x)
    n.sort()
    M.append(list(n))
    print(x)
'''
[[1, 5],
 [2, 4, 5],
 [2, 3, 5],
 [2, 3],
 [2, 3],
 [2, 3],
 [2, 3],
 [1, 2, 4, 5],
 [2, 3, 4],
 [1, 3],
 [1, 3, 4],
 [1, 2, 3, 4, 5],
 [2, 3, 5],
 [2, 5],
 [1, 4, 5],
 [1, 3, 4],
 [1, 2, 3],
 [3],
 [3]]

We can further label the unique subsets so we can quickly glimpse the transitions
We've seen that given a set of subsets, we can sort the elements of the subsets, not the subsets themselves... let's create a function from that
'''
def sortSubsets(L, axis=0):
    '''the name is rather confusing and may be easily mistaken for sorting the subsets maybe in the order of their members or of their first elements (this can easily be accomplished via list.sort())
    
    this sorting sorts the elements of the subsets, not the subsets
    '''
    if axis ==1:
        M = []
        for x in L:
            n = np.array(x)
            n.sort()
            M.append(list(n))
            L = M
    elif axis ==0:
        L.sort()

def top(L):
    '''
    given a set of subsets this should issue forth a topology from it...
    a list of lists may be used,,, and maybe consider adding numpy arrays for future' sake
    assume given the list of list meets conditions for a set..., ie, no repeating members 《I'm a repeating member myself... 202102040844: what dost thou mean? 202102091150: maybe since I retook my third year in college》
    '''
    T = list.copy(L)
    for l in L:
        for l_ in T:
            i = list(set.intersection( set(l),set(l_) ))#get intersection
            if i not in T:
                T.append(i)
            u = list(set.union( set(l),set(l_) ))#get union
            if u not in T:
                T.append(u)
    mems123 = list({x for l in L for x in l})
    '''
    such short forms of code are actually beautiful and impressive to me, the ```{}``` converts the flattened (I don't understand how its flattened though) list into a set.
    '''
    if mems123 not in L:
        T.append(mems123)
    return T
'''

tested this with L = [[2,3],[2,1],[1,2,3,4]]
and it gave T as [[2, 3], [2, 1], [1, 2, 3, 4], [2], [1, 2, 3], [1, 2]] which appears to be a topology.
I've thought that there is weakness in this function given that because other elements are being added (the intersections and unions of members of L), there may be these new members for whom there exists no intersection in T with members of T. one way to go about resolving this would be to perform regression -- to ensure that the new union that's formerly absent in T ... this is bound to get confusing... Lets backtrack a little... we want to ensure that introducing an intersection or a union still maintains the integrity of a topoloy. For a set to be a topology, any union of its members must be present in the set, and so also its intersection... Does the intersection and union of all present members (and the addition of the null & full set over X - where x is the original set {1,2,3,4} ) form a topology... I feel we need a little math here so we don't do unnecessary work if the question has an affirmative answer. How can we disprove or vindicate the statement?

By way of example:
    given a set of subsets: {{1},{2},{2,3}} adding the unions and intersections of members gives
    {{1},{1,2},{1,2,3},{2},{2,3}}
    
    I've got little time to prove that... I'll try a counterexample
    {{2},{2,3,4},{5,6,3}}... the intersection of {2,3,4} and {5,6,3} gives {3}..
    Of note is the absence of the union of {2} and {3}

Can this problem be resolve by first finding the intersections then finding the unions as we did before... we would indeed be lucky if we'd done 《Why am I using the word we? 》 but to challenge that:
    a set of subsets: {{},{1},{2},{3},{4},{5}}
    intersection is taken care of as the only intersection results in the null set
    the unions that come forth of our algorithm are 
    {{1,2},{1,3},{1,4},{1,5}...} from which it's quite easy to see doesn't meet the conditions for being a topology: where is the union of {1,2} and {1,3} which is {1,2,3}... 

'''

#get unique values
def unique(L):
    U = []
    for x in L:
        if x not in U:
            U.append(x)
    return U


'''
I think I now have a general flow for processing series for topologies. One flow we could follow is:
    Given a series, test to see it's a topology. If this first time test is positive (i.e. it's a top), flag the series -->
    Discretize and test if series is topology. If test outcome is positve, give a 2nd grade flag, or a flag whose value is lower than that of the first test.-->
    Create topology through intersections and unions.
    The process can be summarized in a schematic as below. ``^`` denotes path after evaluation of test if true

    
                    Flag                      Flag
X = {1,2,7,8,...} ---^---> discretize --> top? ^ --> form top
'''

'''
get the series
'''
def getStream(mn=0,mx=100,N=100):
    return np.random.randint(mn, mx, N)
'''
discretize a stream
'''
def discretize(n, bins=np.linspace(n.min(),n.max(), 11)):
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
given a collection of subsets, return a set
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
'''
some functional part of this code has been moved to the topology.py in topology folder
'''
'''
now I can implement the flags portion of the system. it's desirable that when an external data stream has forms a topology when subsetted we are able to capture that in the system, raising a flag for noticing by us or servicing by another system. This may be easily accomplished by the discretizing function.
'''
import warnings#for displaying positive warnings

def discretize(n, bins=10):
    bins = np.linspace(0,n.max(),7)
    n = np.digitize(n,bins)
    
    #-------------------------------------capture--------------------------------------------#
    #capture indicates mechanisms put in place to serve as serendipitous anchors.
    #check if subsetting and testing if topology is possible
    if isTop(subset(n)):
        #special case
        warnings.warn("Discovered a series that flows along a full topology. When the series is discretized and subsetted it's quite interesting if it forms a topology by itsefl. Worth looking into")
    #-------------------------------------capture--------------------------------------------#
    return n

