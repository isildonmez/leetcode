# https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-interview-150


class Node:
    def __init__(self, char: str):
        self.char = char
        self.nodes = {}


class Trie:
    def __init__(self):
        self.nodes = {}
        self.words = set()

    def insert(self, word: str) -> None:
        current_nodes = self.nodes
        for char in word:
            next_node = None
            if not current_nodes:
                next_node = Node(char)
                current_nodes[next_node.char] = next_node
            elif char in current_nodes.keys():
                next_node = current_nodes[char]
            else:
                next_node = Node(char)
                current_nodes[next_node.char] = next_node
            current_nodes = next_node.nodes
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        current_nodes = self.nodes
        if not current_nodes:
            return False
        for char in prefix:
            if not char in current_nodes.keys():
                return False
            current_nodes = current_nodes[char].nodes
        return True


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class AlternativeTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    t = Trie()
    t.insert("at")
    t.insert("and")
    print("Testing...")
    assert t.search("and") == True
    assert t.search("app") == False
    assert t.startsWith("an") == True
    assert t.startsWith("and") == True
    assert t.startsWith("ad") == False
    print("Done!")
