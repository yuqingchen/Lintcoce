class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.node = None 
        self.totalsum = -sys.maxsize
        self.helper(root)
        return self.node 
    
    def helper(self, root) :
        if root is None :
            return 0
        leftsum = self.helper(root.left)
        rightsum = self.helper(root.right)
        totalsum = leftsum + rightsum + root.val
        if self.node is None or totalsum < self.totalsum :
            self.node = root 
            self.totalsum = totalsum
        return totalsum