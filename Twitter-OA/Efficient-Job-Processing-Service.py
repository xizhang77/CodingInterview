# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/374446/Twitter-or-OA-2019-or-Efficient-Job-Processing-Service
'''


class Solution(object):
	def maximumTotalWeight(self, weights, tasks, p):
		dp = [ [0]*(int(p/2)+1) for _ in range(len(tasks)+1) ]
		# print dp
		for i in range( 1, len(tasks)+1 ):
			for j in range( 1, p/2+1):
				if tasks[i-1] > j:
					dp[i][j] = dp[i-1][j]
				else:
					dp[i][j] = max( dp[i-1][j], dp[i-1][j - tasks[i-1]] + weights[i-1] )

		return dp[-1][p/2]

s = Solution()
print s.maximumTotalWeight( [2,4,4,5], [2,2,3,4], 15 )