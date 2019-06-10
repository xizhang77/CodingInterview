# -*- coding: utf-8 -*-

'''
// 面试题14：剪绳子
// 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
// 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
// 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
// 时得到最大的乘积18。

同LeetCode 343: https://leetcode.com/problems/integer-break/
'''

class Solution(object):
	def cuttingRope(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [ 0 ] * (n+1)
		dp[ 0 ] = 0
		dp[ 1 ] = 1
		dp[ 2 ] = 1 

		for i in range(3, n+1):
			temp = 0
			for j in range( i/2 + 1 ):
				temp = max(temp, dp[j]*dp[i-j], j *(i-j), j * dp[i-j], (i-j) * dp[i]  )
			dp[i] = temp
		return dp[-1]

s = Solution()
print s.cuttingRope( 10 )
print s.cuttingRope( 50 ) # 86093442