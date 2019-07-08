# -*- coding: utf-8 -*-

'''
// 面试题28：对称的二叉树
// 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
// 它的镜像一样，那么它是对称的。

同LeetCode 101: https://leetcode.com/problems/symmetric-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: Iteratively
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        current = [ root ]
        
        while current:
            nextLevel = []
            value = []
            for node in current:
                if node:
                    value.append( node.val )
                    nextLevel.append( node.left )
                    nextLevel.append( node.right )
                else:
                    value.append( None )
            
            if value != value[::-1]:
                return False
            
            current = nextLevel
        
        return True


# Soluiton 2: Recursively
class Solution(object):
    def dfs(self, node1, node2):
        if not node1:
            return not node2
        if not node2:
            return False
        if node1.val != node2.val:
            return False
        
        return self.dfs( node1.left, node2.right ) and self.dfs( node1.right, node2.left )
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.dfs( root.left, root.right )
        