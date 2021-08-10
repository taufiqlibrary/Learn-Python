# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:08:45 2021

@author: taufiqlibrary
"""

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)