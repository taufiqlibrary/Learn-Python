# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:47:24 2021

@author: taufiqlibrary
"""

# For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))