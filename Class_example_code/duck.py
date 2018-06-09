#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Duck typing example

Bill Smart
"""


from math import sin as mathsin


def abs_of_steel(l):
    try:
        return abs(l)
    except:
        return list(map(abs_of_steel, l))

def sin(n):
    try:
        return mathsin(n)
    except:
        return list(map(sin, n))
    
    
if __name__ == '__main__':
    a = [1, -2, 3, -4, [5, 6]]

    print(abs_of_steel(a))
    #print(sin(a))