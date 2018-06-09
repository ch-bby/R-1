#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018
Exception example code

Bill Smart
"""

from math import cos


def circle_area_old(radius):
    if radius < 0:
        return None
    else:
        return pi * radius * radius

def circle_area(radius):
    if radius < 0:
        raise ValueError('circle radius cannot be negative')
    else:
        return pi * radius * radius
    
def exception_example():
    print('before try block')
    try:
        print('in try block')
        #a = cos(None)
    except:
        print('Caught an exception')
        #raise
    else:
        print('else clause')
    finally:
        print('finally clause')
    print('all done')
    
if __name__ == '__main__':
    area = circle_area_old(-1)
    if area > 10:
        print('large circle')
    else:
        print('small circle')
        
    
    #exception_example()
    
    