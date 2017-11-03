class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        maxCount = 0
        for n in nums:
            if n == 0:
                if maxCount < count:
                    maxCount = count
                count = 0
            else:
                count += 1

        if maxCount < count:
            maxCount = count

        return maxCount