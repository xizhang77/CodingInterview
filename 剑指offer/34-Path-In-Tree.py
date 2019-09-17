# -*- coding: utf-8 -*-

'''
// 面试题34：二叉树中和为某一值的路径
// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

同LeetCode 113: https://leetcode.com/problems/path-sum-ii/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursively
class Solution(object):
    def dfs(self, root, path, target, ans):
        if not root.left and not root.right:
            if sum( path + [ root.val ] ) == target:
                ans.append( path + [ root.val ] )
            return
        if root.left:
            self.dfs( root.left, path + [ root.val ], target, ans )
        if root.right:
            self.dfs( root.right, path + [ root.val ], target, ans )
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        
        if not root:
            return ans
        
        self.dfs( root, [], sum, ans )
        return ans