# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:56:19 2021

@author: bhuvana
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=int(dividend/divisor)
        if res>=(2**31):
            if dividend<0:
                print("neg")
                return -(dividend+1)
        
        return res