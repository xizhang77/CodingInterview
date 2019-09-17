# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/376581/Twitter-or-OA-2019-or-Unique-Twitter-User-Id-Set
'''

class Solution(object):
	def uniqloID(self, arr):
		arr = sorted(arr, reverse = False)

		ans = 0

		currmin = 0

		for a in arr:
			currmin = max( currmin + 1, a )
			ans += currmin

		return ans

s = Solution()
print s.uniqloID( [3,2,1,2,7] )

