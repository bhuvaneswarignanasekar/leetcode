class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1,str2="",""
        while l1 is not None or l2 is not None:
            if l1 is not None:
                str1+=str(l1.val)
                l1=l1.next
            if l2 is not None:
                str2+=str(l2.val)
                l2=l2.next
        
        str1=int(str1[::-1])
        str2=int(str2[::-1])
        Sum=str(str1+str2)[::-1]
        
        res=ListNode()
        l3=res
        for i in Sum:
            l3.next=ListNode(i)
            l3=l3.next
            print(l3)
        print(res)
        print(str1,str2,Sum)
        return res.next