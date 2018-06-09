#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 File I/O example

Bill Smart
"""


from math import factorial


if __name__ == '__main__':
    # Open a file and w
#    with open('fac', 'w') as f:
#        for n in range(10):
#            f.write('{0} {1}\n'.format(n, factorial(n)))
#            
#    with open('fac', 'r') as f:
#        for line in f:
#            print(line)
    
    
    # Beware cacheing filesystems!
    f = open('foo', 'w')
    f.write('This is a line of text')
    
    g = open('foo', 'r')
    print('=====')
    for line in g:
        print(line)
    print('=====')
    