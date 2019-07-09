# -*- coding: utf-8 -*-

'''
// 面试题29：顺时针打印矩阵
// 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

同LeetCode 54: https://leetcode.com/problems/spiral-matrix/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        
        if not matrix or not matrix[0]:
            return ans
        
        m, n = len(matrix), len(matrix[0])
        
        i, j = 0, -1
        d = 0
        
        direct = [ [0,1], [1,0], [0,-1], [-1,0] ]
        
        while len(ans) < m*n:
            ii, jj = i + direct[d][0], j + direct[d][1]
            if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] != float('inf'):
                ans.append( matrix[ii][jj] )
                matrix[ii][jj] = float('inf')
                i, j = ii, jj
            else:
                d = (d+1)%4
        return ans