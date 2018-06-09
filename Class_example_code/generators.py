#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Generator example

Bill Smart
"""


def not_a_generator(n):
    return list(range(n))


def my_range(n):
    next_number = 0
    
    while next_number < n:
        yield next_number
        
        next_number += 1
        
def circular_range(n):
    next_number = 0
    
    while True:
        yield next_number
        
        next_number = (next_number + 1) % n
        
        
if __name__ == '__main__':
    for x in not_a_generator(10):
        print(x)
        
    print()

    for x in my_range(10):
        print(x)

    for x in circular_range(5):
        if input() == 'q':
            break
        
        print(x)