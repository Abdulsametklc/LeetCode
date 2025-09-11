class Solution(object):
    def getDecimalValue(self, head):
        binary = []
        while head: 
            binary.append(head.val) 
            head = head.next

        binary_str = "".join(str(b) for b in binary)
        decimal = int(binary_str, 2)   
        return decimal    