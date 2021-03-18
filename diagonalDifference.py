# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:13:44 2021

@author: bhuvana
"""

def diagonalDifference(arr):
    # Write your code here
    l=len(arr[0])
    pri=[arr[i][i] for i in range(l)]
    print(pri)
    sec=[arr[l-1-i][i] for i in range(l-1,-1,-1)]
    print(sec)
    return (abs(sum(pri)-(sum(sec))))



