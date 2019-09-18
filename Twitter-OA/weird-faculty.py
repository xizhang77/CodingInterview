# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/374440/Twitter-or-OA-2019-or-Weird-Faculty
'''

class Solution(object):
	def exam(self, answers):
		total_sum = 0
		for i in answers:
			total_sum += 1 if i == 1 else -1

		if total_sum < 0:
			return 0

		temp = 0
		for i in range( len(answers) ):
			if answers[i] == 1:
				temp += 1
				total_sum -= 1
			else:
				temp -= 1
				total_sum += 1

			if temp > total_sum:
				return i + 1

s = Solution()
print s.exam([1,0,0,1,0])
print s.exam([1, 0, 0, 1, 1])
print s.exam([1, 1, 1, 0, 1])