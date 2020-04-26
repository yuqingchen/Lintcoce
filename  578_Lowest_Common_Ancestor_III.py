class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if root is None :
            return None 
        self.findA = False 
        self.findB = False 
        lca = self.findlca(root, A, B)
        if self.findA and self.findB :
            return lca 
        return None 
    
    def findlca(self, root, A, B) :
        if root is None :
            return None 
        
        leftlca = self.findlca(root.left, A, B)
        rightlca = self.findlca(root.right, A, B)
        
        if root == A :
            self.findA = True
        if root == B :
            self.findB = True
        if root in (A, B) or (leftlca and rightlca) :
            return root
        return leftlca or rightlca or None 