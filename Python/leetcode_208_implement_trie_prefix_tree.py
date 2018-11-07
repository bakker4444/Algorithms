## 208. Implement Trie (Prefix Tree)
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
#     trie.insert("apple");
#     trie.search("apple");   // returns true
#     trie.search("app");     // returns false
#     trie.startsWith("app"); // returns true
#     trie.insert("app");
#     trie.search("app");     // returns true
#
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
##


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currentNode = self
        if not word:
            return None
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = Trie()
            currentNode = currentNode.children[character]
        currentNode.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentNode = self
        if not word:
            return False
        for character in word:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return currentNode.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentNode = self
        if not prefix:
            return False
        for character in prefix:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return True



# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    word = "apple"
    prefix = "app"
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)