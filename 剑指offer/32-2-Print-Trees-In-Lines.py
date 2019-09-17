# -*- coding: utf-8 -*-

'''
// 面试题32（二）：分行从上到下打印二叉树
// 题目：从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层
// 打印到一行。

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
        
        current = [ root ]
        
        while current:
            nextLevel = []
            val = []
            for node in current:
                val.append( node.val )
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            ans.append( val )
            current = nextLevel
        
        return ans