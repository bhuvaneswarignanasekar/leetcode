# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:31 2021

@author: bhuvana
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res_row=[]
        res_row.append([1])
        c=1
        for i in range(numRows-1):
            c+=1
            res_row.append(self.each_row(res_row[i],c))
        return res_row
            
    def each_row(self,row,n):
        res=[]
        for i in range(n):
            if i==0 or i==n-1:
                res.append(1)
            else:
                temp=row[i-1]+row[i]
                res.append(temp)
        return res