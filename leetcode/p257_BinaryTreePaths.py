# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        paths = []
        startPath = ""

        def findPaths(root, currentPath):
            if root is None:
                return

            if root.left is None and root.right is None:
                paths.append(currentPath + str(root.val))
                return

            if root.left is not None:
                findPaths(root.left, currentPath + str(root.val) + '->')

            if root.right is not None:
                findPaths(root.right, currentPath + str(root.val) + '->')

        findPaths(root, startPath)
        return paths
