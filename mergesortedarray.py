# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:28 2021

@author: bhuvana
"""
#method1
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l=sorted(nums1[:m]+nums2)
        for i in range(len(nums1)):
            nums1[i]=l[i]

#method2
class Solution2:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:]=nums2
        nums1.sort()
