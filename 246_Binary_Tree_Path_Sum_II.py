class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        self.results = []
        if root is None :
            return self.results
        self.dfs(root, [], 0, target)
        return self.results
    
    def dfs(self, root, path, l, target) :
        if root is None :
            return
        path.append(root.val)
        tmp = target
        for i in range(l, -1, -1) :
            tmp -= path[i]
            if tmp == 0 :
                self.results.append(path[i:])
        self.dfs(root.left, path, l + 1, target)
        self.dfs(root.right, path, l + 1, target)
        path.pop()