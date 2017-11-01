def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    
    tree = TreeNode(None)
    
    def makeTree(root, nums):
        if len(nums) == 0:
            return
        
        # get index and value of the maximum number
        maxIndex = nums.index(max(nums))
        root.val = nums[maxIndex]
        
        root.left = makeTree(TreeNode(None), nums[:maxIndex])
        root.right = makeTree(TreeNode(None), nums[maxIndex + 1:])
        return root
    
    return makeTree(tree, nums)