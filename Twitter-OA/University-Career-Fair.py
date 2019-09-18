# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/374846/Twitter-or-OA-2019-or-University-Career-Fair
'''


class Solution(object):
	def maxEvents(self, arrival, duration):
		newList = []
		for i in range( len(arrival) ):
			newList.append( [arrival[i], arrival[i] + duration[i]])

		newList.sort( key=lambda x: x[1], reverse = False )

		endtime = newList[0][1]
		ans = 1

		for event in newList[1:]:
			if event[0] >= endtime:
				ans += 1
				endtime = event[1]
		return ans

s = Solution()
print s.maxEvents( [1,3,3,5,7], [2,2,1,2,1] )