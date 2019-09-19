# -*- coding: utf-8 -*-

'''
Anagram Difference - https://www.hackerrank.com/challenges/anagram/problem
'''

class Solution(object):
	def anagram(self, s):
		if len(s)%2:
			return -1

		count1, count2 = Counter(s[:len(s)/2]), Counter(s[len(s)/2:])
		if count1 == count2:
			return 0

		for key in count1:
			if key in count2:
				count1[ key ] = max(0, count1[key] - count2[key])

		return sum( count1.values() )