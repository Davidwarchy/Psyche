# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:00:19 2021

@author: JOHN WARUTUMO
"""

'''
returns the factorial of a number. factorial(n) = n*(n-1)*...*1 ()
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

'''
given a set x with n members, returns the number of unique subsets with k members.
'''
def com(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

'''
Given a set X = {1,2,3...,n} whose powerset is X = {{},{1},...,{1,2,3,4}}, basic_count(n) returns the number of all basic elements (i.e. those within the subsets) in the powerset.
The logic is there are nC0 = 1 subsets with 0 members, nC1 subsets with 1 member, etc. so the total number of basic elements is nC0*0 + nC1*1 + ... nCn*n
'''
def basic_count(n):
    N = 0
    for x in range(n):
        N += com(n,x)*x
    return N        

