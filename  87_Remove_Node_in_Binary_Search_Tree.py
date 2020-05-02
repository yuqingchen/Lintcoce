class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        # null case
        if root is None :
            return None 
        if value < root.val :
            root.left = self.removeNode(root.left, value)
        elif value > root.val :
            root.right = self.removeNode(root.right, value)
        else :
            if root.left and root.right :
                min = self.findmin(root)
                root.val = min
                root.right = self.removeNode(root.right, min)
            elif root.left :
                root = root.left
            elif root.right :
                root = root.right 
            else :
                root = None 
        return root
    
    def findmin(self, root) :
        node = root.right
        while node.left :
            node = node.left
        return node.val