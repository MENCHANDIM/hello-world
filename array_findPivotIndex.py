class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        amount = sum(nums)
        leftSum = 0
        rightSum = amount
        length = len(nums)
        
        for i in range(length):
            rightSum = rightSum - nums[i]
            leftSum = amount - rightSum - nums[i]
            if leftSum == rightSum:
                return i
        return -1