# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:44:16 2022

@author: think
"""

# this code is used to support small functions
import numpy as np
import math
from scipy import signal

def rmean(x):
    y = x - np.mean(x)
    return y

def taper(x,n,N,F1,F2,SR,order):
    nn = len(x)
    if n==1:
        w = math.pi/N
        F0=0.5
        F1=0.5
    elif n==2:
        w = math.pi/N/2
        F0=1
        F1=1
    win = np.ones((nn,1))
    for i in range(N):
        win[i]=(F0-F1*math.cos(w*(i-1)))
    win1 = np.flipud(win)
    data1 = x*win.reshape(win.shape[0],)
    data1 = data1*win1.reshape(win1.shape[0],)
    return data1
def bpfilt(data1,F1,F2,SR,order):
    semiSR = SR*0.5
    low = F1/semiSR
    hi = F2/semiSR
    b,a = signal.butter(order,[low,hi],'bandpass')
    data2 = signal.filtfilt(b,a,data1)
    return data2

def stalta(x,nst,nlt):
    y =np.zeros(x.shape[0])
    for i in range(nlt,x.shape[0]-nst):
        s1 = np.sum(np.abs(x[i-nlt:i]))
        s2 = np.sum(np.abs(x[i:i+nst]))
        y[i] = s2/s1
    return y
    
    
    
    
    
    
    
    
    
    
    