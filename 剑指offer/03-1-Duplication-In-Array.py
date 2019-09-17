# -*- coding: utf-8 -*-

'''
面试题3（一）：找出数组中重复的数字
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
那么对应的输出是重复的数字2或者3。
'''


# Solution 1: Using Counter
# Time & Space: O(n)
from collections import Counter
class Solution1(object):
    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count = Counter( nums )

        return [ num for num in count if count[ num ] > 1 ][0]


# Solution 2: Hash Table
# Time & Space: O(n)
class Solution2(object):
    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[ num ] = 1
            else:
                return num


# Solution 3: Sorting
# Time: O(nlogn); Space: O(1)
class Solution3(object):
    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort( reverse = False )
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                return nums[i]
            i += 1


# Solution 4: Sort + Compare
# Time: O(n); Space: O(1)
class Solution4(object):
    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len( nums )
        i = 0
        while i < n:
            if nums[ nums[i] ] != nums[i]:
                nums[ nums[i] ], nums[i] = nums[i], nums[ nums[i] ]
                continue
            elif nums[ nums[i] ] == nums[i] and i != nums[i]:
                return nums[i]
            
            i += 1



S = Solution4()
print S.duplicationInArray( [2,3,1,0,2,5,3] )

