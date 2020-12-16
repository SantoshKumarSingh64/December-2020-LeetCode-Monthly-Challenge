'''
Question Description :-
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
 

Example 1:
                2
               / \ 
              1   3 
    Input: root = [2,1,3]
    Output: true

Example 2:
                5
              /   \ 
             1     4
                 /   \ 
                3     6 
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:
    1) The number of nodes in the tree is in the range [1, 104].
    2) -231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root,left,right):
            if root is None:
                return True
            
            if left != None and root.val <= left.val:
                return False
            
            if right != None and root.val >= right.val:
                return False
            
            return helper(root.left,left,root) and helper(root.right,root,right)
                       
        return helper(root,None,None)
