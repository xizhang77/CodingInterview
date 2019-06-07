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

        return [ num for num in count if count[ num ] > 1 ]


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
                hashMap[ num ] += 1

        return [ key for key in hashMap if hashMap[ key ] > 1 ]

# Solution 3: Sorting
# Time: O(nlogn); Space: O(1)
class Solution3(object):
    def duplicationInArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort( reverse = False )
        ans = []
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                ans.append( nums[i])
                while nums[i] == nums[i+1]:
                    i += 1
            i += 1

        return ans

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
        ans = []
        while i < n:
            if nums[ nums[i] ] != nums[i]:
                nums[ nums[i] ], nums[i] = nums[i], nums[ nums[i] ]
                continue
            elif nums[ nums[i] ] == nums[i] and i != nums[i]:
                ans.append( nums[i] )
            
            i += 1

        return ans

S = Solution4()
print S.duplicationInArray( [2,3,1,0,2,5,3] )

