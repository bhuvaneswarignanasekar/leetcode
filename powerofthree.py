class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n%2==0 or n==0: return False
        while n%3==0:
            n=n/3
        if n==1:return True
        return False

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        hi_po=1162261467
        if n<=0:return False
        if hi_po%n==0:return True
        return False
        