# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/363036/Twitter-or-OA-2019-or-Activate-Fountain
'''

class Solution(object):
	def fountainActivation(self, a):
		if not a:
			return 0

		n = len(a)

		interval = []

		for i in range( len(a) ):
			temp = [ max(i-a[i]+1, 1), min(i+a[i]+1, n ) ]
			interval.append( temp )
		
		interval.sort( key=lambda x:( x[0], -x[1]))
		print interval
		
		ans = 1
		l, r = interval[0][0], interval[0][1]

		for itv in interval[1:]:
			if itv[1] <= r:
				continue
			ans += 1
			r = itv[1]

		return ans



s = Solution()
print s.fountainActivation( [2,1,2,1,2,4] )