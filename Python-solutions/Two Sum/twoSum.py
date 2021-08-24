class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hMap = {}
        
        for i in range(0,(len(nums))):
            hMap[nums[i]] = i
                
        print(hMap) 
        
        indexArray = []
        for j in range(0,(len(nums))):
            if ((target - nums[j]) in hMap) and (hMap[target - nums[j]] != j):
                indexArray.append(j)
                indexArray.append(hMap[target-nums[j]])
                break
                
        return indexArray