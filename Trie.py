class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.isLast = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for w in word :
            print("hashmap : ", node.hashmap, node.isLast)
            if w not in node.hashmap :
                print("{} not in hashmap".format(w))
                node.hashmap[w] = Trie()
                print("Added {}".format(w))
            else :
                print("{} in hashmap".format(w))
            node = node.hashmap[w]
        #node.hashmap['*'] = {}
        node.isLast = True

        print("hashmap : ", node.hashmap)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for w in word :
            if w not in node.hashmap :
                print("{} not in hashmap".format(w))
                return False
            else :
                print("{} in hashmap".format(w))
            node = node.hashmap[w]
        print("hashmap : ", node.hashmap)
        return node.isLast

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        word_len = len(prefix)
        n = 0
        for w in prefix :
            if w not in node.hashmap :
                print("{} not in hashmap".format(w))
                return False
            else :
                print("{} in hashmap".format(w))
            node = node.hashmap[w]
            n += 1
        print("hashmap : ", node.hashmap)
        if word_len == n :
            return True
        


    def printTrie(self) :
        if '*' in self.hashmap :
            return
        print("Node details ", self.hashmap)
        for j in self.hashmap.values() :
            #print("Node value", i)
            j.printTrie()



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
obj.insert("abd")
obj.insert("bcd")
obj.printTrie()
print("abc in trie :", obj.search("abc"))
print("ab in trie :", obj.search("ab"))
print("abd in trie :", obj.search("abd"))
print("bcd in trie :", obj.search("bcd"))
print("If word start with a : ", obj.startsWith(""))
#print(help(obj))
#param_2 = obj.search(word)
#param_3 = obj.startsWith(prefix)