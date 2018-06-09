#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018
Palindrome example

Bill Smart
"""


def palindrome_i(text):
    '''
    Iterative function to determine if a string is a palindrome.
    '''
    for i in range(int(len(text) / 2)):
        if text[i] != text[-1 - i]:
            return False
    return True
    
def palindrome_r(text):
    '''
    Recursive function to determine if a string is a palindrome.
    '''
    if len(text) < 2:
        return True
    else:
        return text[0] == text[-1] and palindrome_r(text[1:-1])
    
def palindrome_d(text):
    '''
    A more direct way of determining if a string is a palindrome.
    '''
    return text == text[::-1]


if __name__ == '__main__':
    # Tests go here.
    palindromes = ['', 'a', 'aa', 'aba', 'amanaplanacanalpanama']
    not_palindromes = ['ab', 'asdq21', 'adsawdd12dasd']
    
    failed = 0
    functions = [palindrome_i, palindrome_r, palindrome_d]
    for f in functions:
        for word in palindromes:
            if not f(word):
                print(word)
                failed += 1
            
            for word in not_palindromes:
                if f(word):
                    print(word)
                    failed += 1

        if failed == 0:
            print('{0}: all tests passed'.format(f.__name__))
        else:
            print('{0}: failed {1} of {2} tests'.format(f.__name__, failed,
                  len(palindromes) + len(not_palindromes)))