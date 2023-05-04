#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:49:03 2023

@author: hugo.aranda
"""

def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b
        
def roots(x):
    yield x
    nu_x = x
    while True:
        nu_x =  0.5 * (nu_x + (x/nu_x))
        yield nu_x
        
def primes():
    x = 2
    while True:
        if isPrime(x):
            yield x
        x += 1
        
#fast search done
def isPrime(x):
    if x<2:
        return False
    c = 2
    while c * c <= x:
        if x % c == 0:
            return False
        c += 1
    return True

def primes_better():
    L = []
    acc = 2
    
    while True:
        yield acc
        L.append(acc)
        while divisors(acc,L):
            acc += 1
        
        
def divisors(x,L):
    for elem in L:
        if x % elem == 0:
            return True
    return False

def isHamming(x):
    if x == 1:
        return True
    elif x % 2 == 0:
        return isHamming(x / 2)
    elif x % 3 == 0:
        return isHamming(x / 3)
    elif x % 5 == 0:
        return isHamming(x / 5)
    return False

def hammings():
    a = 1
    yield a
    while True:
        a += 1
        if isHamming(a):
            yield a
        
    