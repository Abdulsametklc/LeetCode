class Solution(object):
    def deleteDuplicates(self, head):
        if not head:  
            return head

        count = 0
        a=0
        curr = head
        liste = []
        while curr:
            count += 1
            curr = curr.next

        curr = head
        liste.append(curr.val)
        curr = curr.next

        while curr:
            if liste[a] != curr.val:
                liste.append(curr.val)
                a += 1
            curr = curr.next

        dummy = ListNode(0) 
        curr = dummy
        for val in liste:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next             