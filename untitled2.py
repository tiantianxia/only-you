# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:22:18 2018

@author: f1434
"""

def isOdd(n):
    if n%2 == 1:
        return True
    else:
        return False
    
while True:
    n = eval(input("请输入一个整数："))
    if n == 0:
        print("程序结束!")
        break
    if isOdd(n):
        print("{} 是奇数".format(n))
    else:
        print("{} 是偶数".format(n))