'''
Question Description :-
Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 
Example 1:
                2
              /   \  
             3     1
           /  \     \ 
          3    1     1   
        Input: root = [2,3,1,3,1,null,1]
        Output: 2 
        Explanation: The figure above represents the given binary tree. 
                    There are three paths going from the root node to leaf nodes: 
                    the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. 
                    Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3]
                    can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
                     2
                  /     \ 
                 1       1 
              /     \   
             1       3
                      \ 
                       1
        Input: root = [2,1,1,1,3,null,null,null,null,null,1]
        Output: 1 
        Explanation: The figure above represents the given binary tree. 
                    There are three paths going from the root node to leaf nodes: 
                    the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. 
                    Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
    Input: root = [9]
    Output: 1
 

Constraints:
    1) The given binary tree will have between 1 and 10^5 nodes.
    2) Node values are digits from 1 to 9.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        def findPaths(root,sb,res):
            
            if root.right is None and root.left is None:
                res.append(''.join(str(x) for x in sb))
            
            if root.left:
                sb.append(root.left.val)
                findPaths(root.left,sb,res)
            
            if root.right:
                sb.append(root.right.val)
                findPaths(root.right,sb,res)
            
            sb.pop()
        
        def canFormPalindrome(string):
            arr = []
            for x in string:
                if x in arr:
                    arr.remove(x)
                else:
                    arr.append(x)
            
            if len(arr) == 0 or len(arr) == 1:
                return True
            return False
        
        
        path = []
        sb = []
        sb.append(root.val)
        findPaths(root,sb,path)
        count = 0
        for x in path:
            if canFormPalindrome(x):
                count += 1
            
        return count
    
#Reference :- https://www.programmersought.com/article/95885891362/
#Reference :- https://medium.com/algorithm-and-datastructure/pseudo-palindromic-paths-in-a-binary-tree-17a53e72776e