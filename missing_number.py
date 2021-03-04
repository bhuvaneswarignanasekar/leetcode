# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:56:19 2021

@author: bhuvana
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        length=len(nums)+1
        for i in range(length):
            if i not in nums:
                return i