# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        s = ListNode(0)
        c = s
        of = 0
        
        done = False
        while not done:
            n1 = 0
            n2 = 0
            
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
                
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            
            # add
            a = n1 + n2
            
            # check overflow
            if of > 0:
                a += of
                of = 0
            
            # add overflow
            if a >= 10:
                a = a % 10
                of = 1
            
            # assign digit
            c.val = a
            
            
            if of > 0 or l1 is not None or l2 is not None:
                c.next = ListNode(0)
                c = c.next
            else:
                done = True
                
        return s