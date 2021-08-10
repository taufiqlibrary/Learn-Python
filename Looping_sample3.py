# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:17:45 2021

@author: taufiqlibrary
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
