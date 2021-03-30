# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:59:43 2021

@author: shanm
"""

print(pow(7,8))class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        B=int("".join(map(str, b)))
        return pow(a,B,1337)