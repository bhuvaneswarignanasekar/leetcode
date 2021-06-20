class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        #super-palindrome is a 
        # palindrome with a square root to be a palindrome
        left=int(left)
        right=int(right)
        res=[]
        while left<=right:
        #if left is a sq number and is palindrome:
            sq=sqrt(left)
            if sq.is_integer() and self.palindrome(left) and self.palindrome(int(sq)):
            #check whether its parent is a palindrome
            # if true add to list
                res.append(left)
            #increment left
            left+=1
        #if limit exceeds stop
        #return length of list
        return len(res)
    
    def palindrome(self,s):
        s=str(s)
        if s==s[::-1]:return True
        return False
class Solution1:
    res=[]
    l=0
    r=0
    def superpalindromesInRange(self, left: str, right: str) -> int:
        self.l=int(left)
        self.r=int(right)
        self.res=[]
        self.superpali_rec(self.l,self.r)
        return len(self.res)
        
        
    def superpali_rec(self,m1,m2):
        print(m1,m2)
        if m1==m2:
            self.is_super(m1)
            
            return 
        m=int((m1+m2)/2)
        n1=self.superpali_rec(m1,m)
        n2=self.superpali_rec(m+1,m2)
        
    def is_super(self,m):
        print(m)
        sq=sqrt(m)
        if sq.is_integer() and self.palindrome(m) and self.palindrome(int(sq)):
            self.res.append(m)
    def palindrome(self,s):
        s=str(s)
        if s==s[::-1]:return True
        return False