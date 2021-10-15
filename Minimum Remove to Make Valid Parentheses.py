class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        t1,t2=0,0
        res=s
        i=0
        for t in s:
            if t=='(':
                t1+=1
            elif t==')':
                t2+=1
                if t2==t1:
                    t1,t2=0,0
                elif t2>t1:
                    res=res[:i]+res[i+1:]
                    i-=1
                    t2-=1
            i+=1
        if t1==t2:
            if res:
                return res
            else: return ""
        s=res
        i=0
        t1-=t2
        res=res[::-1]
        for t in s[::-1]:
            if t=="(":
                if t1>0:
                    res=res[:i]+res[i+1:]
                    i-=1
                    t1-=1
                else:
                    if res:
                        return res[::-1]
                    else: return ""
            i+=1
            
        if res:
            return res[::-1]
        else: return "" 
            
                    