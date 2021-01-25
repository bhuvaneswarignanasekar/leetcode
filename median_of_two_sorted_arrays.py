class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=sum([nums1,nums2],[])
        merged=sorted(merged)
        print(merged)
        print(len(merged))
        median_in=len(merged)/2
        print(median_in)
        if len(merged)%2==0:
            median_in=int(median_in)
            median=(merged[median_in-1]+merged[median_in])/2
            print(median)
        
        else:
            median=merged[int(median_in-0.5)]
            
        return median