from collections import defaultdict

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        patterns = defaultdict(list)
        mod = ord('z') - ord('a') + 1
        for s in strings:
            baseline = ord(s[0])
            pattern = ""
            for i in range(1, len(s)):
                pattern += f"{(ord(s[i]) - baseline) % mod}-"
            patterns[pattern].append(s)
        return list(patterns.values())


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.groupStrings(["a"]) == [["a"]]
    print(s.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
    # [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    print("Done!")
        
                