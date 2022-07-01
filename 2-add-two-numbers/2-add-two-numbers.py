# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        val = 0
        while (l1 != None or l2!= None or carry != 0):
            if l1:
                l1_val = l1.val
            else: l1_val = 0
            if l2:
                l2_val = l2.val
            else: l2_val = 0
            sum = l1_val + l2_val + carry
            newList = ListNode(sum%10)
            carry = sum // 10
            if l1:
                l1 = l1.next
            else: None
            if l2:
                l2 = l2.next
            else: None
            curr.next = newList
            curr = newList
        return head.next
            
        