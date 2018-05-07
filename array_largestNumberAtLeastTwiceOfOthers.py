# #best solution
# class Solution:
#     def dominantIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) <= 1:
#             return 0
#         m = max(nums)
#         ind = nums.index(m)
#         del nums[ind]
#         m_2 = max(nums)
#         return ind if m >= 2*m_2 else -1

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstBig = 0
        secondBig = 0
        thatIndex = 0
        
        for index,item in enumerate(nums):
            if item > firstBig:
                secondBig = firstBig
                firstBig = item
                thatIndex = index
            elif item > secondBig:
                secondBig = item
        
        if len(nums) == 1:
            return 0
        elif firstBig >= 2*secondBig:
            return thatIndex
        else:
            return -1