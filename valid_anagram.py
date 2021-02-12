# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        for i in t:
            if i not in s:
                return 0
            s=s.replace(i,"",1)
        return 1
        