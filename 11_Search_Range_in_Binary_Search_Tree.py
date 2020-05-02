class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        self.results = []
        self.inorder(root, k1, k2)
        return self.results
    
    def inorder(self, root, k1, k2) :
        if root is None :
            return 
        if root.val >= k1 :
            self.inorder(root.left, k1, k2)
        if k1 <= root.val <= k2 :
            self.results.append(root.val)
        if root.val <= k2 :
            self.inorder(root.right, k1, k2)