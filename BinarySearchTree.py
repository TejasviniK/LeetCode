class Node :
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST :

    def __init__(self) :
        self.root = None
    
    def insert(self, data) :
        if self.root is None :
            self.root = Node(data)
        else :
            self._insert(data,self.root)

    def _insert(self, data, cur_node) :
        if data < cur_node.data :
            if cur_node.left is None :
                cur_node.left = Node(data)
            else :
                self._insert(data, cur_node.left)
        
        elif data > cur_node.data :
            if cur_node.right is None :
                cur_node.right = Node(data)
            else :
                self._insert(data, cur_node.right)
        
        else :
            print("Value is already there")
    
    def find(self, data) :
        if self.root :
            is_found = self._find(data, self.root)
            if is_found :
                return True
            return False
        else :
            return None


    def _find(self, data, cur_node) :
        if data > cur_node.data and cur_node.right is not None :
            return self._find(data,cur_node.right)
        elif data < cur_node.data and cur_node.left is not None :
            return self._find(data,cur_node.left)
        if data == cur_node.data :
            return True

    def traverse(self) :
        if self.root :
            self._traverse(self.root)
        else :
            print("None")

    def _traverse(self, cur_node) :
        if cur_node:
            self._traverse(cur_node.left)
            print(str(cur_node.data)+"->", end="")
            self._traverse(cur_node.right)

    def kthSmallest(self, root, k) -> int:
        if root :
            self._kthSmallest(root, k, 0)
        else :
            return None
    
    def _kthSmallest(self, cur_node, k, counter) :
        if cur_node :
            self._kthSmallest(cur_node.left, k, counter)
            counter += 1
            if counter == k :
                return cur_node.val
            self._kthSmallest(cur_node.right, k, counter)

b = BST()
b.insert(10)
b.insert(8)
b.insert(2)
print(b.find(10))
print(b.find(5))
print(b.find(8))
print(b.traverse())
