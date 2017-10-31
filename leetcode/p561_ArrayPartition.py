def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # The idea is that we want the lowest to be paired together, and highest to be paired together
    sum = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        sum += nums[i]
    return sum
