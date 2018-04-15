# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:36:11 2018

@author: f1434
"""

def isNum(str):
    try:
        n = eval(str)
    except:
       return False
    return True

n = input("Enter a string:")
if isNum(n):
    print("{} is a number".format(n))
else:
    print("{} is not a number".format(n))    