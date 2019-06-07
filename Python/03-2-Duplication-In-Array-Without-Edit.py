# -*- coding: utf-8 -*-

'''
面试题3（二）：不修改数组找出任意一个重复的数字

题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
输出是重复的数字2或者3。
'''

# Solution 1: Binary Search
# Time: O(nlogn); Space: O(1)
class Solution5(object):
    def countRange(self, nums, start, end):
        if start > end:
            return 0
        count = 0
        for num in nums:
            if start <= num <= end:
                count += 1

        return count

    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []

        l, r = 0, n - 1
        while l <= r:
            print l, r
            mid = l + (r-l)/2
            count = self.countRange( nums, l, mid )

            if l == r:
                if count > 1:
                    return start
                else:
                    break

            if count > mid - l + 1:
                r = mid
            else:
                l = mid + 1

        return ans


S = Solution()
print S.duplicationInArray( [2,3,1,0,2,5,3] )

