# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]=(i for i in nums if i!=val)