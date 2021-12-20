
# remove 1 element from anywhere

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        #set prev
        prev=nums[0]
        flag=-1
        temp=nums
        
        #time complexity O(N)
        for ind,item in enumerate(nums[1:]):
            
            try:
                nxt=nums[ind+1]
            except:
                continue
            if prev>item:
                if item<nxt:
                    flag+=1
                    del temp[ind-1]
                elif item>nxt:
                    flag+=1
                    del temp[ind]

                
            # if more than one element removed return False
            if flag==1:
                return False
            # update prev
            prev=item
        
        # if flag>=0 return true
        return True