# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Seperate into two lists, reverse the second one, and merge
        # O(n) O(1)
        
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            # if odd, fast = None, STOP
            # if even, fast.next = None, STOP
            slow = slow.next
            fast = fast.next.next
        
        # Seperate
        second = slow.next
        slow.next = None
        
        # Reverse
        prev = None
        while second:
            tem = second.next
            second.next = prev
            prev = second
            second = tem
        
        # Merge
        first, second = head, prev
        while second:
            tem1, tem2 = first.next, second.next
            first.next = second
            second.next = tem1
            first, second = tem1, tem2