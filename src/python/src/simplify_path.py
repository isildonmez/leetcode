#  From https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def simplify_path(self, path: str) -> str:
        res = []
        paths = path.split("/")
        for i, p in enumerate(paths):
            if p == "..":
                if len(res) > 0:
                    res.pop()
            elif p != "." and p != "":
                res.append(p)
        return "/" + "/".join(res)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.simplify_path_solution("/home/") == "/home"
    assert s.simplify_path_solution("/../") == "/"
    assert s.simplify_path_solution("/home//foo/") == "/home/foo"
    assert s.simplify_path_solution("/a//./b//../../c/") == "/c"
    assert s.simplify_path_solution("/a//b////c/d//././/..") == "/a/b/c"
    assert s.simplify_path_solution("/.") == "/"
    print("Done!")
