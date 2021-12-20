#best solution

class Solution:
    def isThree(self, n: int) -> bool:
        div=2
        l=n//2
        if n>2:
            for i in range(2,l+1):
                if n%i==0:
                    div+=1
                if div>3:
                    return False
        if div==3:
            return True
#recursive solution

class Solution:
    def isThree(self, n: int) -> bool:
        div=2
        l=n//2
        
        if n>2:
            div=self.helper(n,l,2)
        if div==3:
            
            return True
    def helper(self,num,lim,d):
        if lim<2:
            return d
        if num%lim==0:
            d+=1
        return self.helper(num,lim-1,d)