# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self, root ) :
        if root :
            self.print_tree(root.left)
            print(str(root.val)+"->", end="")
            self.print_tree(root.right)
        
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        x_parent = self.findParent(root,x)
        y_parent = self.findParent(root,y)

        x_depth = self.findDepth(root,x,1)
        y_depth = self.findDepth(root,y,1)

        if (x_depth == y_depth) and (x_parent != y_parent) :
            return True
        else :
            return False
        
    def findDepth(self, root, x, level) :
        if root is None :
            return -1
        if root.val == x:
            return level

        #print("level : {}".format(level))
        
        leftlevel = self.findDepth(root.left, x, level+1)
        #print("leftlevel : {}".format(leftlevel))
        if leftlevel > 0 :
            return leftlevel
        rightlevel = self.findDepth(root.right, x, level+1)
        return rightlevel
    
    def findParent(self, root, x) :
        
        if root is None :
            return -1
        if (root.left and root.left.val == x) or (root.right and root.right.val == x) :
            return root.val

        leftval = self.findParent(root.left, x)
        if leftval > 0 :
            return leftval
        rightval = self.findParent(root.right, x)
        return rightval

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(5)
tree.print_tree(tree)
print("\n")

s = Solution()
print(s.findDepth(tree, 4, 1))
print(s.findParent(tree, 5))
print(s.isCousins(tree,1,3))
            