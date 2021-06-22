class Solution:
    def singleNumber(self, n: List[int]) -> int:
        while n:
            i=n[0]
            n.remove(i)
            if i in n:
                n=self.remove_all_occ(n,i)
            elif i not in n:
                return i
            
    
    def remove_all_occ(self,n,item):
        return [i for i in n if i != item]