'''
Question Description :-
Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in 
the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
                            5                         1
                        /       \                      \ 
                      3           6                     2
                   /     \         \     --------->      \ 
                  2       4         8                     3    
                 /                /   \                    \ 
                1                7     9                    4
                                                             \ 
                                                              5
                                                               \ 
                                                                6 
                                                                 \ 
                                                                  7
                                                                   \ 
                                                                    8
                                                                     \ 
                                                                      9
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]


Example 2:  
               5                 1
            /     \    ---->      \ 
           1       7               5 
                                    \ 
                                     7
    Input: root = [5,1,7]
    Output: [1,null,5,null,7]
 

Constraints:
    1) The number of nodes in the given tree will be in the range [1, 100].
    2) 0 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        root_list = []
        
        queue = [root]
        
        while len(queue) > 0:
            root_list.append([queue[0].val,queue[0]])
            
            if queue[0].left:
                queue.append(queue[0].left)
            
            if queue[0].right:
                queue.append(queue[0].right)
            
            queue = queue[1:]
        
        root_list.sort()
        
        root = root_list[0][1]
        temp = root
        
        for x in root_list[1:]:
            temp.right = x[1]
            temp.left = None
            temp = temp.right
        temp.right = None
        temp.left = None
        return root
        
