# -*- coding: utf-8 -*-

'''
Twitter OA: new office design
https://leetcode.com/discuss/interview-question/373110/Twitter-or-OA-2019-or-New-Office-Design

'''

class Solution(object):
	def height(self, dist, height1, height2 ):
		# print dist, height1, height2
		minH, maxH = min( height1, height2 ), max( height1, height2 )
		if dist == 0:
			return 0
		if dist == 1:
			return minH + 1
		diff = maxH - minH 
		if dist <= diff:
			return minH + dist - 1
		else:
			# print (dist - diff)/2
			return maxH + (dist - diff)/2

	def maxHeight(self, n, tablePositions, tableHeights):
		ans = 0
		for i in range( n - 1 ):
			temp = self.height( tablePositions[i+1] - tablePositions[i], tableHeights[i], tableHeights[i+1] )
			ans = max( ans, temp )

		return ans


s = Solution()
print s.maxHeight( 4, [1, 2, 4, 7], [4, 5, 7, 11] )
print s.maxHeight( 2, [1, 10], [1, 5] )
print s.maxHeight( 3, [1, 3, 7], [4, 3, 3] )