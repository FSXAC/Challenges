# SUBMITTED

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # Go through all columns
        for rowIndex in range(len(A)):

            # Swap
            for colIndex in range(len(A[rowIndex]) // 2):
                revIndex = len(A[rowIndex]) - colIndex - 1

                temp = A[rowIndex][colIndex]
                A[rowIndex][colIndex] = A[rowIndex][revIndex]
                A[rowIndex][revIndex] = temp


            # Invert
            for colIndex in range(len(A[0])):
                A[rowIndex][colIndex] = 0 if A[rowIndex][colIndex] == 1 else 1

        return A