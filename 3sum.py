# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:41:31 2021

@author: bhuvana
"""
from itertools import combinations
import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        com=list(combinations(nums,3))
        res=[tuple(sorted(i)) for i in com if sum(i)is 0]
        return set(res)
        

