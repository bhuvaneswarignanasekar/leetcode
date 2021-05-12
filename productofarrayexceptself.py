import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        pro=np.prod(nums)
        for idx,it in enumerate(nums):
            if it==0:
                nums[idx]=1
                res.append(np.prod(nums))
                nums[idx]=0
            else:
                res.append(int(pro/it))
        return res
                
            