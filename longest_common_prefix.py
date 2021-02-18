# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        if not strs:
            return ""
        min_len = min(len(ele) for ele in strs)
        if min_len==0:
            return ""
        for i in range(min_len):
            flag=0
            temp=strs[0][i]
            for j in strs:
                if j[i] is temp:
                    flag=1
                else:
                    flag=0
                    return res
            if flag==1:
                res+=temp
        return res