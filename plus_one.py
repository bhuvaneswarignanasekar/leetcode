# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ad_var="".join([str(i) for i in digits])
        ad_var=str(int(ad_var)+1)
        res=[]
        for i in ad_var:
            res.append(i)
        return res
        
        
        