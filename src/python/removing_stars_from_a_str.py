# from: https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def remove_stars(self, s: str) -> str:
        reversed = ""
        contiguous_stars = 0
        for idx in range(1, len(s)+1):
            if s[-idx] == "*":
                contiguous_stars += 1
            elif contiguous_stars > 0:
                contiguous_stars -= 1
            else:
                reversed += s[-idx]
        return reversed[::-1]

    def refactored_remove_stars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
            else:
                continue
        return ''.join(stack)
    
if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.remove_stars("leet**cod*e") == "lecoe"
    assert s.remove_stars("erase*****") == ""
    assert s.refactored_remove_stars("leet**cod*e") == "lecoe"
    assert s.refactored_remove_stars("erase*****") == ""
    print("All passed")

