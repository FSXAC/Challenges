# NOT SUBMITTED

# 1. 1
# 2. 11
# 3. 21
# 4. 1211
# 5. 111221
# Count and say the n-1th term

# Probably want to do something recursive

class Solution:
    # count and say is a recursive function
    def countAndSay(self, n):

        # Base case
        if n <= 1:
            return '1'
        
        # Other cases
        prevStr = countAndSay(n - 1)

        # Easy case
        if len(prevStr) == 1:
            return '1' + prevStr

        retStr = ''
        count = 0
        index = 0
        while True:
            current = prevStr[index]
            count += 1

            if index == len(prevStr) - 1:
                # current is the last char of the string
                retStr += str(count)
                retStr += current
                break

            if current != prevStr[index + 1]:
                # Next character is different
                retStr += str(count)
                retStr += current
                count = 0
            
            index += 1
        
    return retStr