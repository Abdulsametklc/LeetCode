class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = self.uzunluk(head)
        sira = length - n + 1
        if sira == 1:
            return head.next
        current = head
        count = 1

        while count < sira - 1:
            current = current.next
            count +=1
        
        current.next = current.next.next
        return head

    def uzunluk(self, head):
        count = 0
        current = head
        while current is not None:
            count +=1
            current = current.next
        return count    