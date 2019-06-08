# -*- coding: utf-8 -*-

'''
// 面试题10：斐波那契数列
// 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。

同 LeetCode 509: https://leetcode.com/problems/fibonacci-number/
'''

# Solution 1: Recursive
class Solution1(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        return self.fib(N-1) + self.fib(N-2)

# Solution 2: DP
# Time and Space: O(N)
# Can be improved to Space O(1) (only capture the last 2 values)
class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [ 0, 1 ]
        
        
        for i in range(2, N+1):
            dp.append( dp[i-1] + dp[i-2] )
        
        return dp[N]