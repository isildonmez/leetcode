class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        r = b[::-1]
        return int(r, 2)


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.reverseBits(43261596) == 964176192
    assert s.reverseBits(4294967293) == 3221225471
    print("Done!")
