# -*- coding: utf-8 -*-

'''
// 面试题38扩展：8皇后问题

同LeetCode 51: https://leetcode.com/problems/n-queens/
'''

class Solution(object):
    def perm(self, nums, path, ans, n ):
        for i in range( len(path) ):
            for j in range(i+1, len(path)):
                if j + path[j] == i + path[i] or j - path[j] == i - path[i]:
                    return
        if not nums:
            ans.append( path )
            return
        
        for i in range( len(nums) ):
            self.perm( nums[:i]+nums[i+1:], path + [ nums[i] ], ans, n )
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        position = []
        self.perm( range(n), [], position, n )
        
        ans = []
        for pos in position:
            temp = []
            for i in range(n):
                temp.append( '.'*pos[i] + 'Q' + '.'*( n - pos[i] - 1 ) )
            ans.append( temp )
        
        return ans