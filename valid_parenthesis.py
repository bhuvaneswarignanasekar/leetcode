# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:29:14 2021

@author: bhuvana
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        is_bal=0
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}' and stack!=[]:
                temp=stack.pop()
                is_bal=self.check_valid(temp,i)
                print(is_bal,temp,i)
                if is_bal==0:
                    return False
            else:
                return False
        if is_bal==1 and stack==[]:return True
        return False
    
    def check_valid(self,c2,c1):
        if c1=='}' and c2=='{':return True
        if c1==')' and c2=='(':return True
        if c1==']' and c2=='[': return True
        return False

