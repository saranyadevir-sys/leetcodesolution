# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to act as the head of the resulting list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Loop until both lists are empty and there is no remaining carry
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Create a new node with the calculated digit
            curr.next = ListNode(new_digit)
            
            # Move the pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
