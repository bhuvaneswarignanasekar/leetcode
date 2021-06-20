class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        n=n+1
        for i in range(n):
            temp=self.binary(i)
            res.append(self.count_ones(temp))
            
        return res
    def count_ones(self,s):
        count=0
        for i in s:
            if i=="1":
                count+=1
        return count
                
    
    def binary(self,n):
        return bin(n)[2:]