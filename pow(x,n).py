# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:31 2021

@author: bhuvana
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        ans=self.myPow(x,n//2)
        ans*=ans
        if n&1:
            return x*ans
        return ans