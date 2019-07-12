# -*- coding: utf-8 -*-

'''
// 面试题47：礼物的最大价值
// 题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
// （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或
// 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
// 算你最多能拿到多少价值的礼物？


Similar to LeetCode 64: https://leetcode.com/problems/minimum-path-sum/
'''

class Solution(object):
    def maxPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        
        dp = [ [0]*n for _ in range(m) ]
        
        for i in range(m):
            dp[i][0] = grid[i][0]
            if i > 0:
                dp[i][0] += dp[i-1][0]
        
        for j in range(n):
            dp[0][j] = grid[0][j]
            if j > 0:
                dp[0][j] += dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max( dp[i-1][j], dp[i][j-1] ) + grid[i][j]
        
        return dp[-1][-1]