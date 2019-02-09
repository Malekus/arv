from __future__ import division
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from math import log
from math import sin
from math import fabs
from PIL import Image
"""from PIL.Image import *"""
from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np


ex1 = lambda x : [i for i in range(1, x+1)]
ex2 = np.array(list(Image.open("bob.jpg").getdata()))[:,0].tolist()
ex3 = lambda x : [math.sin( 2 * math.pi * x) for x in range(1, x // 2)] + [ 1/2 + math.sin( 2 * math.pi * x) for x in range((x // 2)+1, x)]


def tsfd_quad(u):
    v=[]
    n = len(u)
    for l in range(0,n):
        v.append(u[l])
    w=[]
    i=0
    for i in range(0,n):
        w.append(0)     
    l = int(log(len(v))/log(2))  
    for i in range(0,l):
        n=n/2
        k = 0
        for k in range(0,n):        
            w[k] = ((v[2*k] + v[2*k+1])/2.0 )          
            if k==0 and k==n-1:
                w[k+n] = v[2*k] - ( w[k] - ((v[2*n-2] + v[2*n-1])/2.0 - (v[0] + v[1])/2.0)/8 )           
            elif k==0:
                w[k+n] = v[2*k] - ( w[k] - ((v[2*n-2] + v[2*n-1])/2.0 - (v[2] + v[3])/2.0)/8 )
            elif k==n-1 :
                w[k+n] = v[2*k] - ( w[k] - ((v[2*k-2] + v[2*k-1])/2.0 - (v[0] + v[1])/2.0)/8 )
            else:
                w[k+n] = v[2*k] - ( w[k] - ((v[2*k-2] + v[2*k-1])/2.0 - (v[2*k+2] + v[2*k+3])/2.0)/8 )
        for k in range(0,2*n):
            v[k]=w[k]        
        print (v)
    return v





def tsfi_quad(u):
    v=[]
    n = len(u)
    for l in range(0,n):
        v.append(u[l])
    n=1
    lon = len(u)
    w=[]
    for i in range(0,lon):
        w.append(0)
    l = int(log(len(v))/log(2))

    for i in range(0,l):
        for k in range(0,n):
            w[2*k]=v[k]+v[k+n]
            w[2*k+1]=v[k]-v[k+n]
            
            if k == 0 and k == n-1:
                w[2*k] = v[k] - (v[k] - v[k] ) /8 + v[k+n]
                w[2*k+1] = v[k] + (v[k] - v[k]) /8 - v[k+n]
            elif k == 0:
                w[2*k] = v[k] - (v[k+n - 1] - v[k+1]) /8 + v[k+n]
                w[2*k+1] = v[k] + (v[k+n-1] - v[k+1]) /8 - v[k+n]
            elif k == n-1:
                w[2*k] = v[k] - (v[k-1] - v[0]) /8 + v[k+n]
                w[2*k+1] = v[k] + (v[k-1] - v[0]) /8 - v[k+n]
            else:
                w[2*k] = v[k] - (v[k-1] - v[k+1]) /8 + v[k+n]
                w[2*k+1] = v[k] + (v[k-1] - v[k+1]) /8 - v[k+n]
        n=2*n
        for k in range(0,n):
            v[k] = w[k]
     
    return v


def seuillage(detail, x):
    for index, el in enumerate(detail[0]):
        if abs(el) <= abs(x):
            detail[index] = 0
    return detail

def seuillage2(detail, x):
    for i in range(len(detail[0])):
        if abs(detail[0][i]) <= abs(x):
            detail[0][i] = 0
    return detail



def erreur(x, T):
    a = tsfd_quad(x)
    s = seuillage(b, T)
    print(tsfi_quad(a,s))


def quest3(x, T):
    a = []
    x = tsfd_quad([x])
    for j in range(len(x[0])):
        if x[0][j] > T :
            a.append(x[0][j])
    return a 

def quest4(x, T):
    a = []
    tmp2 = tsfi_quad(seuillage2(tsfd_quad([x]),T))
    for j in range(len(x)):
        tmp = x[j] - tmp2[0][j]
        print(tmp)
    return tmp2

