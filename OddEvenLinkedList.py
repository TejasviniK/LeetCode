# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None :
            return head
        cur = head
        head_next = head.next
        n = 0
        even_check = False
        while cur.next :
            #print("Updating : ",cur.val)
            next_node = cur.next
            if next_node.next is None and n%2 == 0 :
                cur.next = head_next
                even_check = True
            else :
                cur.next = next_node.next
            n += 1
            cur = next_node
        if not even_check :
            cur.next = head_next
        #print("Updating : ", cur.val)
        return head

    def oddEvenListMethod2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None :
            return head

        odd = head
        even = evenhead = head.next
        
        while even is not None and even.next is not None :
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenhead
        
        return head
    


s = Solution()
print(s.oddEvenList([1,2,3,4,5])