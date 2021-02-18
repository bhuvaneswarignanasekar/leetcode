# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp=s.split()
        if not sp:
            return 0
        l_sp=len(sp)-1
        return len(sp[l_sp])