# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)
        