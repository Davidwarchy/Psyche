# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:49:17 2020

@author: David Warutumo
"""
import pyaudio
import numpy as np
# import matplotlib.pyplot as plt
import time

def son():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))
    
    n = np.hstack(frames)
    i = abs(n).mean()
    #create file where to write log info
    f = open('son.psy', 'a')
    f.write(time.strftime('%Y%m%d%H%M%S',time.gmtime())+":"+str(i)+'\n')
    f.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # plt.plot(n)
    # plt.show()
while True:
    son()
    time.sleep(60)