class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root :
            return
        self.res = []
        self.node = set()
        self.inorder(root, n)
        return self.res
    
    def inorder(self, root, n) :
        if root is None :
            return 
        self.inorder(root.left, n)
        if root.val in self.node :
            self.res = [root.val, n - root.val]
        else :
            self.node.add(n - root.val)
        self.inorder(root.right, n)