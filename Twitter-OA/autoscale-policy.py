# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/376019/Twitter-or-OA-2019-or-Autoscale-Policy
'''

class Solution(object):
	def finalInstances(self, instance, averageUtil):
		minIns, maxIns = 1, 2 * 10^8
		idle = 10

		i = 0
		while i < len(averageUtil):
			if instance > minIns and averageUtil[i] < 25:
				instance = math.ceil( float(instance)/2 )
				i += idle
			elif instance < maxIns and averageUtil[i] > 60:
				instance *= 2
				i += idle
			else:
				i += 1

		return instance

s = Solution()
print s.finalInstances( 1, [5,10,80])