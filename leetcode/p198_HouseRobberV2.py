# Version 2 (using dynamic programming)

# THEORY
# Notice the pattern that we can do one of two things:
# 1. include the highest index house 'n'
#   In which case, the answer is houses[n] + table[n - 2]
# 2. Don't include the highest index
#   In which case the answer is table[n - 1]
# 
# BAES CASES
# Index 0
#   There is only 1 element, return houses[0]
#   table[0] = houses[0]
# 
# Index 0-1
#   return max(houses[0], houses[1])
#   table[1] = ^^
#
# UTILIZE PATTERN IN RECURSIVE STEPS
# Index 0-2
#   return max(houses[2] + table[0], table[1])
#   table[2] = ^^
# 
#   ... so on

# NOT SUBMITTED

class Solution:
    def houseRobber(self, houses):

        # Helper function
        def getTableValue(index):
            return self.houseRobber(houses[:index + 1])

        # Edge case
        if len(houses) == 0:
            return 0

        # Base cases
        nHouses = len(houses)
        if nHouses == 1:
            return houses[0]
        
        elif nHouses == 2:
            return max(houses)

        # Recursive
        else:
            return max(houses[nHouses - 1] + getTableValue(nHouses - 1 - 2), getTableValue(nHouses - 1 - 1))

s = Solution()
print(s.houseRobber([1, 4, 4, 3])) # expect 7

