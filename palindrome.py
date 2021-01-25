class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            rev=self.rev_num(x)
            print(rev)
            if x==rev:
                print("palindrome")
                return 1
            else:
                return 0
        else:
            return 0
    def rev_num(self,x):
        num=0
        while x>0:
            num=num*10+x%10
            x=int(x/10)
        return num