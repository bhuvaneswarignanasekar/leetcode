# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:02:31 2021

@author: bhuvana
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        s=self
        return str(s.str2int(num1)*s.str2int(num2))
 
    def str2int(self,num):
        n=0
        for ind,i in enumerate(num[::-1]):
            temp=int(i)*(10**ind)
            n+=temp
        return n
