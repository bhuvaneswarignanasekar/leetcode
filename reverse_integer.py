class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            num=self.rev_num(x)
        else:
            x=x*-1
            num=self.rev_num(x)
            num=num*-1
        return num
    def rev_num(self,x):
        num=0
        while x>0:
            num=num*10+x%10
            x=int(x/10)
            if num> 2147483647:
                num=0
        return num
                