# -*- coding: utf-8 -*-

'''
相关问题1：青蛙跳台阶问题

一直青蛙一次可以跳上一级or两级台阶。求上n级台阶的跳法。

同 LeetCode 70: https://leetcode.com/problems/climbing-stairs/

'''

class Solution1(object):
    def climbStair(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [ 0 ] * N
        dp[0] = 1
        dp[1] = 2

        for i in range(2, N):
        	dp[ i ] = dp[i-1] + dp[i-2]

        return dp[-1]