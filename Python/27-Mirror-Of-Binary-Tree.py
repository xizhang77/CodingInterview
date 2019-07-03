# -*- coding: utf-8 -*-

'''
// 面试题27：二叉树的镜像
// 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

同LeetCode 226: https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iteractive
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        stack = [ root ]
        
        while stack:
            node = stack.pop( 0 )
            
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append( node.left )
            if node.right:
                stack.append( node.right )
        
        return root


# Recursive
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree( root.left )
        
        return root