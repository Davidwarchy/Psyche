# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:56:18 2021

@author: JOHN WARUTUMO
"""

#the perceptron
import numpy as np

class Perceptron():
    weights = ''
    inputs = 0
    output = 0
    bias = 0
    '''
    initialize perceptron. the defaults are three inputs at a go with each input weighted equally %in,weights, output%
    '''
    def __init__(self,input_streams=3, weights=[0.33,0.33,0.33],bias=0):
        self.weights = np.array(weights)
        self.input_streams = np.zeros((1,input_streams))#1 is the#of elements in the highest dimension
    
    '''
    returns output of the perceptron... which is the input x the weights %picture of inputs, weights, outputs%
    '''
    def calc(self,i):
        return (i*self.weights).sum() - self.bias
        

p = Perceptron(3)

#lets consider the best time to study
#noise(0,1)      timeof day(0,1)    timespent working
#0.1,0,0.125 --> 1
#0.1,3,0.125 --> 1
#1,1,1 --> 0
#noise: 0 represent lowest noise while 1 may represent the maximum noise (or 75percentile)
#timeofday: 0 represents 0000 hrs while 1 represents 2359hrs. or 0 may represented the time since waking as a fraction of average time spent awake
#timeworking: the fraction of time spent working until the current moment against the average total waketime.
#the decision to make might be whether to continue working,
#it might also be to measure productivity.