# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #find the middle el
        mid = head
        fast = head
        
        while fast and fast.next!=None :
            mid = mid.next
            fast = fast.next.next

        #if fast = None : odd, if fast!= None : even
        #when odd, mid needs to shift one right
        if fast :
            mid = mid.next
        
        #break and reverse the second half
        prev = None
        curr = mid
        #need to do for all nodes from mid to end
        while curr != None :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        #compare the two lists
        left, right = head, prev
        while right :
            if left.val!=right.val :
                return False
            left = left.next
            right = right.next

        return True 
