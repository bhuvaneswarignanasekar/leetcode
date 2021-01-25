# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sort=[]

        for i in lists:
            while i != None:
                sort.append(i.val)
                i=i.next
        sort=sorted(sort)
        res=ListNode()
        l1=res
        
        for i in sort:
            l1.next=ListNode(i)
            l1=l1.next
        
        return res.next