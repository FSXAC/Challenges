# NOT SUBMITTED
# REFER TO V2

class Solution:
    def houseRobber(self, houses):

        # General ideas:
        # - Some kind of recursive function like opposite of merge sort
        # - Exit case to be if adjascent houses have been robbed
        # - Takes in index (and compare with index - 1 and index + 1)

        # Exit cases
        if len(houses) < 1:
            return 0
        elif len(houses) == 1:
            return houses[0]

        # In each recursion, we find the maximum value index that separates the sub-array

        # Find the maximum valued house
        maxVal = max(houses)
        total = maxVal
        indexMax = houses.index(maxVal)

        # Edge cases:
        # - single house
        # - two houses
        # - three houses and the max in the middle
        # Test the cases:
        # - Check if +2 or -2 is out of bound
        # - +-2 Because we can't rob the house adjacsent

        if indexMax - 2 >= 0:
            total += self.houseRobber(houses[:indexMax - 2])
        
        if indexMax + 2 <= len(houses) - 1:
            total += self.houseRobber(houses[indexMax + 2:])

        return total

s = Solution()
print(s.houseRobber([1,3,2,1]))
