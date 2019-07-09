# -*- coding: utf-8 -*-

'''
// 面试题32（一）：不分行从上往下打印二叉树
// 题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

同LeetCode 102: https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        
        stack = [ root ]
        
        while stack:
            node = stack.pop(0)
            ans.append( node.val )
            if node.left:
            	stack.append( node.left )
            if node.right:
            	stack.append( node.right )
        
        return ans