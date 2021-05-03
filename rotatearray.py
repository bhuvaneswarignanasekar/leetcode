class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)<k:
            temp=self.if_great(nums,k)
        else:
            l=len(nums)-k
            temp=nums[l:]
            temp+=nums[:l]
        for idx,i in enumerate(temp):
            nums[idx]=i
            
    def if_great(self,nums,k):
        temp=[]
        temp+=nums
        print(temp)
        if k==0:
            return
        
        for i in range(k):
            temp1=[]

            temp1.append(temp.pop())
            temp1+=temp
            temp=temp1
        return temp1
   
        