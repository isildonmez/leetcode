# https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def paddings(line_len: int, line: list[str], last_line: bool) -> list[int]:
            total = maxWidth - line_len
            num_of_blanks = len(line) - 1
            if num_of_blanks == 0 or last_line:
                return [total]
            default, remainder = divmod(total, num_of_blanks)
            res = [default] * num_of_blanks + [0]
            for i in range(remainder):
                res[i] += 1
            return res

        if len(words) == 1:
            return [words[0] + " " * (maxWidth - len(words[0]))]
        line = [words[0]]
        result = []
        line_length = len(words[0])
        for w in words[1:]:
            if line_length + 1 + len(w) <= maxWidth:
                line.append(f" {w}")
                line_length += 1 + len(w)
            else:
                pads = paddings(line_length, line, False)
                res = ""
                for i in range(len(line)):
                    res += line[i] + " " * pads[i]
                result.append(res)
                line = [w]
                line_length = len(w)
        pads = paddings(line_length, line, True)
        res = "".join(line) + " " * pads[0]
        result.append(res)
        return result


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    r1 = ["This    is    an", "example  of text", "justification.  "]
    r2 = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
    assert (
        s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
        == r1
    )
    assert (
        s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )
    ) == r2
    print("Done!")
