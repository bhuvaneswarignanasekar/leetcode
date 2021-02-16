# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:49:47 2021

@author: bhuvaneswari
"""
from collections import OrderedDict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        add_dict={}
        temp=0
        res=[]
        for index,i in enumerate(mat):
            for j in i:
                if j is 1:
                    temp=temp+1
            add_dict[index]=temp
            temp=0
        print(add_dict)
        sort_dict=list((dict(sorted(add_dict.items(), key=lambda item: item[1]))).keys())
        for i in range(k):
            res.append(sort_dict[i])
        return res
            