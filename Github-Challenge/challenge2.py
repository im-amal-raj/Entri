# QUESTION

"""Coding Challenge  Question 2

 Problem : Write a Python program to reverse the elements of a list without using the built-in reverse() method or slicing ([::-1]). You must use a loop to solve this problem.
Input:

A list of integers (for example: [10, 20, 30, 40, 50]).

Output:

A new list with the elements in reverse order (for the above example: [50, 40, 30, 20, 10]).
"""


# CODE

a = [10, 20, 30, 40, 50]


def rev(l):
    temp = []
    for i in l:
        temp.insert(0, i)

    print(f"Original list: {l} \nReversed list {temp}")


rev(a)
