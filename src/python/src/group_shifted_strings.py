from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        pattern_to_strings = defaultdict(list)
        normaliser = ord("a")
        mod = ord("z") - ord("a") + 1
        for s in strings:
            pattern = ""
            difference = ord(s[0]) - normaliser
            for c in s:
                ascii_num = ord(c) - difference
                if ascii_num < ord("a"):
                    ascii_num += mod
                pattern += chr(ascii_num)
            pattern_to_strings[pattern].append(s)
        return pattern_to_strings.values()


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.groupStrings(["a"]) == [["a"]]
    print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    # [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    print("Done!")
