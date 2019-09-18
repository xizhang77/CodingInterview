# -*- coding: utf-8 -*-

'''
Get set go
'''

class Solution(object):
    def combinationSum(self, calories, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        calories.sort()

        check = set( [0] )


        for cal in calories:
        	if cal == target or target - cal in check:
        		return True
        	if cal + min( check ) > target:
        		break
        	temp = [ ]
        	for val in check:
        		temp.append( val + cal )
        	print temp
        	check = check.union( set( temp ) )

        return False


s = Solution()
print s.combinationSum( [2,9,5,1,6], 12 )
print s.combinationSum( [2,3,15,1,16], 8)