# -*- coding: utf-8 -*-

'''
相关问题2：矩形覆盖问题

用 2*1 的小矩形横着或者竖着去覆盖一个 2*N 的矩形，请问一共有多少种覆盖方法？
'''

class Solution1(object):
    def coverArea(self, N):
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