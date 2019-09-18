# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/378237/Twitter-or-OA-2019-or-Authentication-Tokens
'''

class Solution(object):
	def numberOfTokens(self, expiryLimit, commands):
		hashmap = {}
		for command in commands:
			token_id, time = command[1], command[2]
			if command[0] == 0:
				hashmap[ token_id ] = time + expiryLimit
			else:
				if token_id in hashmap:
					if hashmap[ token_id ] >= time:
						hashmap[ token_id ] = time + expiryLimit
					else:
						del hashmap[ token_id ]

		ans = sum(1 for i in hashmap.values() if i >= time)

		return ans



s = Solution()
print s.numberOfTokens( 4, [[0,1,1], [0,2,2], [1,1,5], [2,2,7]])