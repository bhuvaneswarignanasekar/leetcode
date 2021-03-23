# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:29:14 2021

@author: bhuvana
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if nums==[] or max(nums)<0:
            return 1
        lst=nums[len(nums)-1]
        print(lst)
        for i in range(1,lst,1):
            print(i)
            if i not in nums:
                return i
        return lst+1
                
        

