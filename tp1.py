from __future__ import division
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import pi
from scipy.spatial import distance


""" Exercice 1,2,3 """
ex1 = lambda x : [i for i in range(1, x+1)]
ex2 = np.array(list(Image.open("bob.jpg").getdata()))[:,0].tolist()
ex3 = lambda x : [math.sin( 2 * math.pi * x) for x in range(1, x // 2 + 1)] + [ 1/2 + math.sin( 2 * math.pi * x) for x in range((x // 2)+1, x+1)]

""" Ecrire la fonction directe """
def easyHaar(x):
    r = []
    d = []
    for i in range(0, len(x), 2):
        r.append((x[i] + x[i+1]) / 2)
        d.append((x[i] - x[i+1]) / 2)
    return r, d

def directe(x):
    detail = []
    while len(x) != 1:
        a, b = easyHaar(x)
        detail = detail + b
        x = a
    return a, detail[::-1]


""" Ecrire la fonction inverse """
def easyHaarInv(x, y):
    r = []
    d = []
    for index, i in enumerate(x):        
        r.append(i + y[index])
        r.append(i - y[index])
    return r, y[len(x):]

def inverse(x, y):
    r = []
    arret = (len(y) + 1) / 2
    while len(y) != 0:
        a, b = easyHaarInv(x, y)
        r = a
        x, y = a, b
    return r

""" Verifier que x = inverse(directe(x)) pour ex1 et ex3"""
x = ex1(8)
a,b = directe(x)
print(x == inverse(a,b))
x = ex3(8)
a,b = directe(x)
print([round(a, 2) for a in x] == [round(a, 2) for a in inverse(a,b)])

""" Ecrire les fonctions dicrecte et inverse avec for """
def directeFor(x):
    detail = []
    for i in range(int(math.log(len(x)) // math.log(2)) + 1):
        a, b = easyHaar(x)
        detail = detail + b
        x = a
    return a, detail[::-1]

def inverseFor(x, y):
    r = []
    arret = (len(y) + 1) / 2
    for i in range(int(math.log(len(y)) // math.log(2)) + 1):
        a, b = easyHaarInv(x, y)
        r = a
        x, y = a, b
    return r

""" Ecrire une fonction de seuillage """
def seuillage(detail, x):
    r = []
    for index, el in enumerate(detail):
        if abs(el) <= abs(x):
            r.append(0)
        else:
            r.append(el)
    return r



""" Visualiser les valeurs y superieur a T=128 et T=12"""
x = ex1(1024)
_, y = directe(x)
print(seuillage(y, 128))
print(seuillage(y, 12))



""" Erreur """
def erreur(x, T):
    a,b = directe(x)
    s = seuillage(b, T)
    i = inverse(a,s)
    return distance.euclidean(x,i)

x = ex1(1024)
print(erreur(x, 128))
print(erreur(x, 12))

displayPlot(e)

def displayPlot(x):
    plt.figure()
    plt.plot(x)
    plt.show()
    
""" Etude qualite reconstruction """
def etudeRecon(x, nbFois=128, seuil=1):
    r = []
    for i in range(nbFois):
       r.append([seuil*i, erreur(x, seuil*i)])
    return r


r = etudeRecon(ex1(128), 32+1, 1)
plt.figure()
plt.title("Erreur en fonction du Seuil = 1")
plt.plot(np.array(r)[:,0], np.array(r)[:,1])
plt.xlabel("Seuil")
plt.ylabel("Erreur")
plt.show()
