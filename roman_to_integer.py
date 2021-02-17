# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sums=0
        for ind,it in enumerate(s):
            if ind-1>=0:
                if (it is 'V' or it is 'X') and s[ind-1] is 'I':
                    sums+=roman_dict[it]-2
                elif (it is 'C' or it is 'L') and s[ind-1] is 'X':
                    sums+=roman_dict[it]-20
                elif (it is 'D' or it is 'M') and s[ind-1] is 'C':
                    sums+=roman_dict[it]-200
                else:
                    sums+=roman_dict[it]
                
            else:
                sums+=roman_dict[it]
        return sums