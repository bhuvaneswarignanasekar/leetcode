class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        external_help=''
        cur=head
        while cur!=None:
            external_help+=str(cur.val)
            cur=cur.next
        return external_help==external_help[::-1]
        