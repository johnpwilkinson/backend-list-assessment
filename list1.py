#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List1
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "John Wilkinson, Kenzie Lessons, and googleFu"

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(words):
    count = 0
    for word in words:
        #if word is 2 or more characters and the first and last characters are the same
        if len(word) > 1 and word[0] == word[-1]:
            # increase count variable
            count += 1
            # return count
    return count


# B. front_x
# Given a list of strings, return a list with the strings in
# sorted order, except group all the strings that begin with
# 'x' first.
# Example:
#   ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#   ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each
# of them before combining them.


def front_x(words):
    xwords = []
    allOtherWords = []

    for word in words:
        # if the word starts w X, send it to xwords list
        if word.startswith('x'):
            xwords.append(word)
        else:
            # all other words do to the other array
            allOtherWords.append(word)
    # sort both lists
    xwords.sort()
    allOtherWords.sort()
    #add the other words list to the x words list
    xwords.extend(allOtherWords)

    return xwords



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in
# increasing order by the last element in each tuple.
# Example
#   [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#   [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.


def sort_last(tuples):
    # take list of tuples and sort with the Key using the 2nd element in each tuple
    tuples.sort(key= lambda x: x[-1])
    return tuples


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\nfront_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\nsort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 9, 4), (2, 2)]),
         [(2, 2), (1, 3), (3, 9, 4), (1, 7)])


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
