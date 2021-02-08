# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""

import numpy as np
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        char_ind=[]
        res=[]
        
        for index in range(len(s)):
            if c is s[index]:
                char_ind.append(index)
        for i in range(len(s)):
            closest=self.nearest(char_ind,i)
            res.append(abs(i-closest))
        return res
        
    def nearest(self,array,val):
        array = np.asarray(array)
        ind = (np.abs(array - val)).argmin()
        return(array[ind])
            
                    