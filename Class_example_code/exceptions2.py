#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Another exception example

Bill Smart
"""

if __name__ == '__main__':
    while True:
        number = input('Number? ')
        
        if number == 'q':
            break
        
        try:
            value = float(number)
            print('{0} squared is {1}'.format(value, value * value))
        except ValueError:
            print('Please enter a number!')
            
    

