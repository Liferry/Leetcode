# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:07:18 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def get_depth(self, root):
        
        if not root:
            return 0
        
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
        
        