from __future__ import division
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt



ex1 = lambda x : [i for i in range(1, x+1)]
ex2 = np.array(list(Image.open("bob.jpg").getdata()))[:,0].tolist()
ex3 = lambda x : [math.sin( 2 * math.pi * x) for x in range(1, x // 2)] + [ 1/2 + math.sin( 2 * math.pi * x) for x in range((x // 2)+1, x)]


def easyHaar(x):
    r = []
    d = []
    for i in range(0, len(x), 2):
        r.append((x[i] + x[i+1]) / 2)
        d.append((x[i] - x[i+1]) / 2)
    return r, d

def easyHaarInv(x, y):
    r = []
    d = []
    for index, i in enumerate(x):        
        r.append(i + y[index])
        r.append(i - y[index])
    return r, y[len(x):]

def directe(x):
    detail = []
    while len(x) != 1:
        a, b = easyHaar(x)
        detail = detail + b
        x = a
    return a, detail[::-1]


def inverse(x, y):
    r = []
    arret = (len(y) + 1) / 2
    while len(y) != 0:
        a, b = easyHaarInv(x, y)
        r = a
        x, y = a, b
    return r

def seuillage(detail, x):
    for index, el in enumerate(detail):
        if abs(el) <= abs(x):
            detail[index] = 0
    return detail


def erreur(x, T):
    a,b = directe(x)
    s = seuillage(b, T)
    
    print(inverse(a,s))
    
a,b = directe(ex1(128))
erreur(ex1(128), 10)
