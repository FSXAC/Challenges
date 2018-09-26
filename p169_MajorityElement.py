# NOT SUBMITTED

class Solution:
    def MajorityElement(self, nums):
        """
        nums: list of numbers
        assuming nums is non empty and always contains a majority
        """

        count = {}

        # One way is to use a dictionary and increment the key value
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        # Get the key that has the most count
        firstFlag = True
        bigNum = 0
        for key in count:

            if firstFlag:
                firstFlag = False
                bigNum = key

            if (count[key] > count[bigNum]):
                bigNum = key
        
        return bigNum


s = Solution()
print(s.MajorityElement([3, 3, 1, 1, 1, 4]))
