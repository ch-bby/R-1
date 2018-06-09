#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018
Timing test example

Bill Smart
"""


from timer import timer
from string import ascii_letters
from random import choice

import palindrome


if __name__ == '__main__':
    # Figure out all the names of the palindrome functions.  This extracts all
    # the names in the palindrome package that start with 'palindrome_' and
    # then uses getattr to find the function pointers for them.
    functions = [getattr(palindrome, f) for f in dir(palindrome) if f[:11] == 'palindrome_']

    # Add in a direct lambda function that is the same as palindrome_d
    functions.append(lambda a: a == a[::-1])

    long_size = 1000000

    null_p = ''
    short_p = 'aa'
    medium_p = 'amanaplanacanalpanama'
    long_p = ''.join([choice(ascii_letters) for i in range(int(long_size / 2))])
    long_p = long_p + long_p[::-1]

    short_n = 'ab'
    medium_n = 'djaosdjednonejdedeoid'
    long_n = ''.join([choice(ascii_letters) for i in range(long_size)])

    for f in functions:
        print(f.__name__ + ':')
        print('    null_p: {0:.2f}'.format(timer(f, null_p) * 1000000))
        print('   short_p: {0:.2f}'.format(timer(f, short_p) * 1000000))
        print('  medium_p: {0:.2f}'.format(timer(f, medium_p) * 1000000))
        try:
            print('    long_p: {0:.2f}'.format(timer(f, long_p) * 1000000))
        except:
            print('    long_p: too much recursion')
        print()
        print('   short_n: {0:.2f}'.format(timer(f, short_n) * 1000000))
        print('  medium_n: {0:.2f}'.format(timer(f, medium_n) * 1000000))
        try:
            print('    long_n: {0:.2f}'.format(timer(f, long_n) * 1000000))     
        except:
            print('    long_p: too much recursion')
        print()