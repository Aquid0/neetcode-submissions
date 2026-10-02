class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')

            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def b(word, node):
            curr = node

            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children:
                        if child is not None and b(word[i + 1:], child):
                            return True
                    return False
                else: 
                    index = ord(c) - ord('a')

                    if curr.children[index] is None:
                        return False
                    
                    curr = curr.children[index]
            
            return curr.isEndOfWord

        return b(word, self.root)
                

        
