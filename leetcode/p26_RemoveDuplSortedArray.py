class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        prev = None

        l = len(nums)
        i = 0

        while i < l:
            n = nums[i]
            if prev is None or prev != n:
                count += 1
                i += 1
            else:
                del nums[i]
                l -= 1
            prev = n

        return count
