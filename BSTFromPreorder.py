import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])

        for i in preorder[1:] :
            self.constructBST(root,i)
            print("Inserted {}".format(i))
            self.print_tree(root)
        return root

    def constructBST(self, root, data) :
        if root is None :
            
            root = TreeNode(data)
            return root

        if data < root.val :
            root.left = self.constructBST(root.left,data)
        else :
            root.right = self.constructBST(root.right, data)
        
        return root

    def bstFromPreorderApproach2(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        n = len(preorder)
        if n == 0 :
            return None
        
        root = TreeNode(preorder[0])
        if n == 1 :
            return root
        
        self.constructBSTApproach2(preorder, n, 1, root, -(sys.maxsize), sys.maxsize)
        #self.print_tree(root)
        return root


    def constructBSTApproach2(self, preorder, n, pos, cur, left, right):
        if n == pos or preorder[pos] < left or preorder[pos] > right :
            return pos
        
        if preorder[pos] < cur.val :
            cur.left = TreeNode(preorder[pos])
            pos += 1
            pos = self.constructBSTApproach2(preorder, n, pos, cur.left, left, cur.val-1)

        if n == pos or preorder[pos] < left or preorder[pos] > right :
            return pos

        cur.right = TreeNode(preorder[pos])
        pos += 1
        pos = self.constructBSTApproach2(preorder, n, pos, cur.right, cur.val + 1, right)

        return pos

    def print_tree(self, root ) :
        if root :
            self.print_tree(root.left)
            print(str(root.val)+"->", end="")
            self.print_tree(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root :
            print(str(root.val)+"->", end="")
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        

s = Solution()
root = s.bstFromPreorderApproach2([8,5,1,7,10,12])
s.print_tree(root)
print("Inverting")
s.invertTree(root)
print("Inverted Tree")
s.print_tree(root)