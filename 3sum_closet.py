# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:41:31 2021

@author: bhuvana
"""
from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difference=[]
        sums=[]
        combi=list(combinations(nums,3))
        for i in combi:
            add=sum(i)
            dif=add-target
            sums.append(add)
            difference.append(abs(dif))
            if difference is 0:
                return target
        posi=difference.index(min(difference))
        return sums[posi]

