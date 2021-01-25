# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sort=ListNode()
        l3=sort
        if l1==[] and l2==[]:
            return []
    
        
        while l1 !=None and l2 !=None:
            if l1.val<=l2.val:
                print(l1.val)
                l3.next=ListNode(l1.val)
                l1=l1.next
            else:
                print(l2.val)
                l3.next=ListNode(l2.val)
                l2=l2.next
            l3=l3.next
            print(l3)
            
        if l1==None and l2!=None:
            l3.next=l2
    
        if l1!=None and l2==None:
            l3.next=l1
            
        return sort.next
        