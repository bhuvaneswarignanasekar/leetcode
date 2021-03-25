# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:10:53 2021

@author: bhuvana
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=''
        for i in (s.lower()):
            if i.isalpha() or i.isdigit():temp+=i
                
        if temp==temp[::-1]:return True
        return False

