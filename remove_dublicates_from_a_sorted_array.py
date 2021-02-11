# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_set=sorted(set(nums))
        
        for i,j in enumerate(temp_set):
            nums[i]=j
        return len(temp_set)
            
        