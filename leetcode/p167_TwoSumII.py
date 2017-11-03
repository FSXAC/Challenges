class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binarySearch(nums, target):
            imin = 0
            imax = len(nums) - 1
            
            while True:
                if imax < imin:
                    return -1
                
                i = (imin + imax) // 2
                n = nums[i]
                if n > target:   # try smaller
                    imax = i - 1
                elif n < target: # try bigger
                    imin = i + 1
                else:
                    return i
        
        l = len(numbers)
        for i in range(l):
            n = numbers[i]
            diff = target - n
            
            i2 = binarySearch(numbers[i + 1:l], diff)
            
            if i2 != -1:
                return [i + 1, i + 2 + i2]