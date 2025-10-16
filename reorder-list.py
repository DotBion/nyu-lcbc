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
        #split linked list into two - first find mid
        #reverse the latter list
        #merge alternatively

        #find mid
        mid = head
        fast = head
        while fast and fast.next != None :
            mid = mid.next
            fast = fast.next.next

        #split the two lists to avoid cycles
        ll2 = mid.next
        mid.next = None
        #ll1 = head
        

        #reverse the second ll
        prev = None
        curr = ll2
        while curr!=None :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #merge the two lists
        ll1, ll2 = head, prev
        while ll2:
            t1 = ll1.next
            ll1.next = ll2
            
            t2 = ll2.next
            ll2.next = t1

            ll1 = t1
            ll2 =t2
