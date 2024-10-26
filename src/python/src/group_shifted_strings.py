from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        pattern_to_strings = defaultdict(list)
        mod = ord("z") - ord("a") + 1
        for s in strings:
            pattern = ""
            normaliser = ord(s[0])
            for c in s:
                curr = (ord(c) - normaliser) % mod
                pattern += chr(curr)
            pattern_to_strings[pattern].append(s)
        return list(pattern_to_strings.values())


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.groupStrings(["a"]) == [["a"]]
    print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    # [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    print("Done!")
