# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:33:03 2021

@author: bhuvana
"""
from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N==0:return False
        if N==1:return True
        l=[char for char in str(N)]
        orders=permutations(l)
        for per in orders:
            if per[0]=='0':continue
            temp=int(''.join(per))
            powerof2=self.check_power(temp)
            if powerof2 is True:
                return True
        return False
                
        
    def check_power(self,N):
        while N!=1:
            if N%2!=0:
                return False
            N=N/2
                
        return True
                       

