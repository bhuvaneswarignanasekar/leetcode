# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:59:43 2021

@author: shanm
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(nums)+1):
            com=combinations(nums,i)
            for j in com: 
                if sorted(j) not in res: res.append(sorted(j))
        return res
            