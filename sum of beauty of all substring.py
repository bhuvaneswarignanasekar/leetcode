from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        # assign length of s to l, so l be the limit for 'for' loop
        l=len(s)
        res=0
        
        # iterate i from 2 to the length to the s (i.e l)
        #this is the for loop determining the length of the substring
        for i in range(2,l):
            #create dublicate string for s
            dubli_s= s
            
            # get all the possible subset of the string given the length of the substring
            # while length of dubli_s is greater than or equal to i
            j=i+1
            while (len(dubli_s)>=j):
                substring=dubli_s[:j]
                dubli_s=dubli_s[1:]
                count_res = Counter(substring)
                maxF=0
                minF=j
                for key in count_res:
                    v=count_res[key]
                    if v>maxF:maxF=v
                    if v<minF:minF=v
                diff=maxF-minF
                if diff>0:
                    res+=diff
        return res
