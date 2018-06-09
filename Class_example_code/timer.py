#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018
Simple timing code

Bill Smart
"""


from time import time


def timer(f, *a):
    '''
    Time how long it takes to run a function, with a given set of arguments.
    This function returns the wall clock time, in seconds.  It discards the
    return value of the function that is passed in.
    '''
    start_time = time()
    f(*a)
    end_time = time()
    return end_time - start_time
    
    
if __name__ == '__main__':
    # We should put some more rigorous tests here.
    print(timer(max, 1, 2, 3))
