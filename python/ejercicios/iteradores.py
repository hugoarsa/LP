#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:31:11 2023

@author: hugo.aranda
"""

def count_unique(L):
    return len(set(L))

def remove_duplicates(L):
    return list(set(L))

from functools import reduce

def flatten(L):
    return reduce(lambda acc, l: acc + l, L, [])

def flatten_rec(L):
    func = lambda acc, l: acc + flatten_rec(l) if isinstance(l, list) else acc + [l]
    return reduce(func, L, [])