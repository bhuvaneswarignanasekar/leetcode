class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        #O(NM)
        for i in words:
            
            flag=0
            for j in i:
                if j not in allowed:
                    flag=1
            if flag==0:
                count+=1
        return count