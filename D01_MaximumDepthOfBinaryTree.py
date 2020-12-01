'''
Question Description :-
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.


Example 1:
                    3
                  /   \ 
                 9     20
                      /   \ 
                     15    7 
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Example 3:
    Input: root = []
    Output: 0

Example 4:
    Input: root = [0]
    Output: 1
 

Constraints:
    1) The number of nodes in the tree is in the range [0, 104].
    2) -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def helper(root):
            
            if root is None:
                return 0
            left_height = helper(root.left)+1
            right_height = helper(root.right)+1
            
            return max(left_height,right_height)
        
        return helper(root)