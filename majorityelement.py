# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:31 2021

@author: bhuvana
"""
import collections
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic=dict(collections.Counter(nums))
        for k,v in dic.items():
            if v==1:
                return k
            
