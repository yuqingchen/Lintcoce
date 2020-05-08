class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if root is None :
            return []
        self.results = []
        self.dfs(root, [root.val], target)
        return self.results
    
    def dfs(self, root, path, target ) :
        if not root.left and not root.right :
            if sum(path) == target :
                self.results.append(path[:])
            return
        if root.left :
            self.dfs(root.left, path + [root.left.val], target)
        if root.right :
            self.dfs(root.right, path + [root.right.val], target)