# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:50:16 2021

@author: bhuvana
"""
#method 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        res=''
        print(a,b)
        if len(a)>=len(b):
            s_1=a[::-1]
            s_2=b[::-1]
        if len(b)>len(a):
            s_1=b[::-1]
            s_2=a[::-1]
        for i in s_1:
            if s_2:
                temp=int(i)+int(s_2[0])+carry
                s_2=s_2[1:]
            else:
                temp=int(i)+carry
            r,carry=self.car(temp)
            res+=r
        if carry==1:
            res+=str(carry)
        return res[::-1]
    def car(self,s):
        if s==0:return '0',0
        if s==1:return '1',0
        if s==2:return '0',1
        if s==3:return '1',1
        
#method 2
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        integer_sum = int(a, 2) + int(b, 2)
        binary_sum = bin(integer_sum)
        return (str(binary_sum))[2:]

