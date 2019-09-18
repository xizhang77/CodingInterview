# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/375262/Twitter-or-OA-2019-or-Partitioning-array
'''
from collections import Counter
class Solution(object):
	def solve(self, k, numbers):
		if len(numbers)%k != 0:
			return False

		count = Counter( numbers )
		for val in count.values():
			if val > len(numbers)//k:
				return False

		return True

s = Solution()
print s.solve( 3, [1,2,2,3] )