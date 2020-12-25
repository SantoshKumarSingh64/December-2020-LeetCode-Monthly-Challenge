'''
Question Description :-
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.
 
Example 1:
    1 --> 2 --> 3 --> 4 --> None
    Input: head = [1,2,3,4]
    2 --> 1 --> 4 --> 3 --> None
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]
 

Constraints:
    1) The number of nodes in the list is in the range [0, 100].
    2) 0 <= Node.val <= 100
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        prevNode = head
        currNode = head.next
        prev = None
        head = currNode
        
        while True:
            
            if prev != None:
                prev.next =  currNode
            nextNode = currNode.next
            currNode.next = prevNode
            
            if not nextNode or nextNode.next is None:
                prevNode.next = nextNode
                break
            
            prev = prevNode
            prevNode.next = nextNode
            prevNode = prevNode.next
            currNode = prevNode.next
            
            
        return head