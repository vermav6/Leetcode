class Solution(object):

    # The easiest solution to this problem (no need DP, no brute force, or D&C)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        init = nums[0]
        currSum = nums[0]
        
        for i in range(1, len(nums)):
            if init < 0:
                init = nums[i]
            else:
                init += nums[i]
            if currSum < init:
                currSum = init
        return currSum