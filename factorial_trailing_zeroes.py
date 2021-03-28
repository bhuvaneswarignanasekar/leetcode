# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:31 2021

@author: bhuvana
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=str(factorial(n))
        c=0
        for i in fact[::-1]:
            if i!='0':return c
            c+=1
            
