# NOT SUBMITTED

class Solution:

    letterLookup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def excelSheetColumnNumber(self, s):
        """
        s is type string
        rtype: number
        """

        s = s.upper()

        out = 0

        for char in s:

            out *= 26

            index = self.letterLookup.index(char)
            out += index + 1

        return out

# s = Solution()
# print(s.excelSheetColumnNumber('AZ'))