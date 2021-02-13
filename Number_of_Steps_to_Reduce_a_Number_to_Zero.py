# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        while num>0:
            if num%2==0:
                num=num/2
            else:
                num-=1
            count+=1
        return count
        
        