class TrieNode:
    def __init__(self) -> None:
        self.chars = {}  # {char: TrieNode()}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i, char in enumerate(word):
            if char not in current.chars:
                current.chars[char] = TrieNode()
            current = current.chars[char]
            if i == len(word) - 1:
                current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for i, char in enumerate(word):
            if char not in current.chars:
                return False
            current = current.chars[char]
            if i == len(word) - 1:
                return current.is_word

    def search_prefix(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.chars:
                return False
            current = current.chars[char]
        return True
