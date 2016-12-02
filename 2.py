# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        sub_sum = 0
        power = 0
        while(l1 != None or l2 != None):
            if l1 == None:
                sub_sum = l2.val
                l2 = l2.next
            elif l2 == None:
                sub_sum = l1.val
                l1 = l1.next
            else:
                sub_sum = l1.val + l2.val
                l1 = l1.next;l2 = l2.next
            sum += sub_sum * pow(10 ,power)
            power += 1
        if sum == 0:
            return ListNode(0)
        ret = ListNode(-1)    #head node
        p = ret
        while sum != 0:
            p.next = ListNode(sum % 10)
            sum = sum / 10
            p = p.next
        return ret.next
            
        
        
