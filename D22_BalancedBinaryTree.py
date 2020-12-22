'''
Question Description :-
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:
               3
            /     \ 
           9       20
                 /     \ 
                15      7      
    Input: root = [3,9,20,null,null,15,7]
    Output: true

Example 2:
            1
          /   \ 
         2     2
       /   \    
      3     3
    /   \ 
   4     4 
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

Example 3:
    Input: root = []
    Output: true
 
Constraints:
    1) The number of nodes in the tree is in the range [0, 5000].
    2) -104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        def helper(root):
            
            if root is None:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)
        
            if left_height == None or right_height == None:
                return None
            
            if abs(left_height - right_height) > 1:
                return None

            return max(left_height,right_height)+1    
        
        
        return True if helper(root) != None else False