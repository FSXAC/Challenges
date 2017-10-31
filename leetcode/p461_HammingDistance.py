class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hdist = 0
        xor = x ^ y
        while (xor != 0):
            if (xor % 2 == 1):
                hdist += 1
            xor = xor >> 1

        return hdist