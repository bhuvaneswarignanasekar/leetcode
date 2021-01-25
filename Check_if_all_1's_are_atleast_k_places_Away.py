class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        counter,index=0,0
        
        for i in nums:

            if i==0:
                counter+=1
                
            if i==1 and index!=0:
                if counter<k:
                    return 0
                
                else:
                    counter=0
            index+=1
        return 1