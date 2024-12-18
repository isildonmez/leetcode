# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# Hints: #44, # 777, # 732


def is_unique(word: str) -> bool:
    uniqe_chars = set()
    for letter in word:
        if letter in uniqe_chars:
            return False
        uniqe_chars.add(letter)
    return True


def is_unique_without_additional_data_structures(word: str) -> bool:
    for i in len(word):
        for j in len(word):
            if word[i] == word[j]:
                return False
    return True


def is_unique_allowed_to_change_the_input(word: str) -> bool:
    sorted_word = sorted(word)
    for i in len(sorted_word) - 1:
        if sorted_word[i] == sorted_word[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print("Testing...")
    assert is_unique("awedcvbg") is True
    assert is_unique("aakll") is False
    print("Done!")
