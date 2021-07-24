class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        if len(s)<3:
            return 0
        while s:
            if len(s)==3:
                count+= self.reoccur(s)
                return count
                
            count+= self.reoccur(s[:3])
            s=s[1:]
            
    def reoccur(self,sub):
        while sub:
            if sub[0] in sub[1:]:
                return 0
            sub=sub[1:]
            
        return 1
                