class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for n in nums:
            diff = target - n
            i = nums.index(n)
            if diff in nums[i, len(nums)]:
                return [i, nums.index(diff)]