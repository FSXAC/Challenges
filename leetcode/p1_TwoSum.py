class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        for i in range(l):
            n = nums[i]
            diff = target - n
            
            if diff in nums[i + 1:l]:
                return [i, i + 1 + nums[i + 1:l].index(diff)]